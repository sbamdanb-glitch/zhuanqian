#!/usr/bin/env python3
"""
GitHub Bounty Hunter - 自动发现和追踪 GitHub 悬赏任务的命令行工具
"""

import re
import requests
from typing import List, Dict, Optional
from dataclasses import dataclass
from datetime import datetime
import click
from rich.console import Console
from rich.table import Table
from rich.progress import Progress

console = Console()


@dataclass
class BountyIssue:
    """悬赏任务数据类"""
    title: str
    url: str
    repo: str
    amount: float
    labels: List[str]
    created_at: str
    comments: int
    state: str
    
    def __str__(self):
        return f"[{self.repo}] {self.title} - ${self.amount}"


class GitHubBountyHunter:
    """GitHub 悬赏猎人主类"""
    
    def __init__(self, github_token: Optional[str] = None):
        self.github_token = github_token
        self.base_url = "https://api.github.com"
        self.headers = {
            "Accept": "application/vnd.github.v3+json"
        }
        if github_token:
            self.headers["Authorization"] = f"token {github_token}"
    
    def extract_bounty_amount(self, issue: Dict) -> float:
        """从 issue 中提取悬赏金额"""
        # 检查标签中的金额
        for label in issue.get('labels', []):
            label_name = label.get('name', '')
            # 匹配 $15, $100 等格式
            match = re.search(r'\$(\d+(?:,\d{3})*(?:\.\d{2})?)', label_name)
            if match:
                amount_str = match.group(1).replace(',', '')
                return float(amount_str)
        
        # 检查标题和正文中的金额
        text = f"{issue.get('title', '')} {issue.get('body', '')}"
        matches = re.findall(r'\$(\d+(?:,\d{3})*(?:\.\d{2})?)', text)
        if matches:
            # 返回找到的最大金额
            amounts = [float(m.replace(',', '')) for m in matches]
            return max(amounts)
        
        return 0.0
    
    def search_bounty_issues(
        self, 
        min_amount: float = 0,
        tech_stack: Optional[List[str]] = None,
        sort_by: str = "created",
        max_results: int = 50
    ) -> List[BountyIssue]:
        """搜索悬赏任务"""
        
        # 构建搜索查询
        query = 'is:open label:"💎 Bounty"'
        
        if tech_stack:
            # 添加技术栈过滤
            tech_query = ' OR '.join([f'"{tech}"' for tech in tech_stack])
            query += f' ({tech_query})'
        
        params = {
            'q': query,
            'sort': sort_by,
            'order': 'desc',
            'per_page': max_results
        }
        
        console.print(f"[cyan]🔍 正在搜索悬赏任务...[/cyan]")
        console.print(f"[dim]查询: {query}[/dim]")
        
        try:
            response = requests.get(
                f"{self.base_url}/search/issues",
                headers=self.headers,
                params=params,
                timeout=30
            )
            response.raise_for_status()
            data = response.json()
            
            bounties = []
            for item in data.get('items', []):
                amount = self.extract_bounty_amount(item)
                
                # 过滤低于最小金额的任务
                if amount < min_amount:
                    continue
                
                bounty = BountyIssue(
                    title=item['title'],
                    url=item['html_url'],
                    repo=item['repository_url'].split('/')[-2] + '/' + item['repository_url'].split('/')[-1],
                    amount=amount,
                    labels=[label['name'] for label in item.get('labels', [])],
                    created_at=item['created_at'],
                    comments=item.get('comments', 0),
                    state=item['state']
                )
                bounties.append(bounty)
            
            # 按金额排序
            bounties.sort(key=lambda x: x.amount, reverse=True)
            
            return bounties
            
        except requests.exceptions.RequestException as e:
            console.print(f"[red]❌ 搜索失败: {e}[/red]")
            return []
    
    def display_bounties(self, bounties: List[BountyIssue]):
        """以表格形式显示悬赏任务"""
        
        if not bounties:
            console.print("[yellow]⚠️  未找到符合条件的悬赏任务[/yellow]")
            return
        
        table = Table(title=f"🎯 发现 {len(bounties)} 个悬赏任务", show_lines=True)
        
        table.add_column("仓库", style="cyan", no_wrap=True)
        table.add_column("任务标题", style="white")
        table.add_column("金额", style="green", justify="right")
        table.add_column("评论数", style="yellow", justify="center")
        table.add_column("发布时间", style="magenta")
        
        for bounty in bounties:
            # 格式化时间
            created = datetime.fromisoformat(bounty.created_at.replace('Z', '+00:00'))
            time_str = created.strftime("%Y-%m-%d")
            
            # 截断标题
            title = bounty.title[:60] + "..." if len(bounty.title) > 60 else bounty.title
            
            table.add_row(
                bounty.repo,
                f"[link={bounty.url}]{title}[/link]",
                f"${bounty.amount:.0f}" if bounty.amount > 0 else "未知",
                str(bounty.comments),
                time_str
            )
        
        console.print(table)
        
        # 显示统计信息
        total_amount = sum(b.amount for b in bounties if b.amount > 0)
        console.print(f"\n[bold green]💰 总悬赏金额: ${total_amount:.0f}[/bold green]")


@click.group()
def cli():
    """GitHub Bounty Hunter - 发现和追踪 GitHub 悬赏任务"""
    pass


@cli.command()
@click.option('--min-amount', default=0, help='最小悬赏金额')
@click.option('--tech', help='技术栈过滤（逗号分隔），如: python,react')
@click.option('--sort-by', default='created', type=click.Choice(['created', 'updated', 'comments']), help='排序方式')
@click.option('--max-results', default=50, help='最大结果数')
@click.option('--token', envvar='GITHUB_TOKEN', help='GitHub Personal Access Token')
def list(min_amount, tech, sort_by, max_results, token):
    """列出所有开放的悬赏任务"""
    
    tech_stack = tech.split(',') if tech else None
    
    hunter = GitHubBountyHunter(github_token=token)
    bounties = hunter.search_bounty_issues(
        min_amount=min_amount,
        tech_stack=tech_stack,
        sort_by=sort_by,
        max_results=max_results
    )
    
    hunter.display_bounties(bounties)


@cli.command()
def stats():
    """显示悬赏统计信息"""
    console.print("[cyan]📊 统计功能开发中...[/cyan]")


@cli.command()
def watch():
    """监控新的悬赏任务"""
    console.print("[cyan]🔔 监控功能开发中...[/cyan]")


if __name__ == '__main__':
    cli()
