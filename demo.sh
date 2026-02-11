#!/bin/bash
# GitHub Bounty Hunter 演示脚本

echo "==================================="
echo "GitHub Bounty Hunter 演示"
echo "==================================="
echo ""

echo "📋 示例 1: 列出所有悬赏任务"
echo "命令: python3 bounty_hunter.py list --max-results 5"
echo ""
python3 bounty_hunter.py list --max-results 5
echo ""
echo "-----------------------------------"
echo ""

echo "💰 示例 2: 只显示高价值悬赏 (≥$50)"
echo "命令: python3 bounty_hunter.py list --min-amount 50 --max-results 5"
echo ""
python3 bounty_hunter.py list --min-amount 50 --max-results 5
echo ""
echo "-----------------------------------"
echo ""

echo "🎯 示例 3: 按评论数排序（热门任务）"
echo "命令: python3 bounty_hunter.py list --sort-by comments --max-results 5"
echo ""
python3 bounty_hunter.py list --sort-by comments --max-results 5
echo ""
echo "-----------------------------------"
echo ""

echo "✅ 演示完成！"
echo ""
echo "更多用法请参考 USAGE.md"
