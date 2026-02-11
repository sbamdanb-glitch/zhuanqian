# 💰 GitHub Bounty Hunter

> 自动发现和追踪 GitHub 悬赏任务的命令行工具

[![GitHub Sponsors](https://img.shields.io/badge/Sponsor-GitHub-pink?logo=github)](https://github.com/sponsors/sbamdanb-glitch)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 项目简介

**GitHub Bounty Hunter** 是一个专为开发者设计的命令行工具，帮助您快速发现和追踪 GitHub 上的悬赏任务（Bounty Issues），让赚钱机会不再错过！

### 为什么需要这个工具？

- 🔍 **自动发现**：实时扫描 GitHub 上带有悬赏标签的 Issues
- 💵 **按金额排序**：优先显示高价值悬赏任务
- 📊 **难度评估**：根据项目复杂度和技术栈评估任务难度
- 🔔 **实时通知**：新悬赏任务发布时立即通知您
- 📈 **收入追踪**：记录您完成的悬赏和累计收入

## 🚀 快速开始

### 安装

```bash
# 使用 pip 安装
pip install github-bounty-hunter

# 或使用 npm 安装
npm install -g github-bounty-hunter
```

### 基本使用

```bash
# 查看当前所有开放的悬赏任务
bounty-hunter list

# 按金额排序
bounty-hunter list --sort-by amount

# 过滤特定技术栈
bounty-hunter list --tech python,react

# 设置金额过滤
bounty-hunter list --min-amount 50

# 订阅新悬赏通知
bounty-hunter watch --notify
```

## ✨ 核心功能

### 1. 悬赏任务搜索

自动搜索 GitHub 上所有带有悬赏标签的 Issues，支持多种过滤条件：

- 按悬赏金额过滤
- 按技术栈过滤
- 按项目星标数过滤
- 按任务发布时间过滤

### 2. 智能推荐

基于您的技能和历史记录，智能推荐最适合您的悬赏任务。

### 3. 收入统计

追踪您完成的悬赏任务和累计收入，生成可视化报表。

### 4. 实时通知

支持多种通知方式：
- 邮件通知
- Slack 通知
- Discord 通知
- 桌面通知

## 📦 技术栈

- **语言**: Python 3.8+
- **依赖**: 
  - `requests` - HTTP 请求
  - `click` - 命令行界面
  - `rich` - 终端美化输出
  - `PyGithub` - GitHub API 封装

## 🤝 贡献指南

欢迎贡献代码、报告 Bug 或提出新功能建议！

1. Fork 本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

## 💖 支持项目

如果这个工具对您有帮助，请考虑：

- ⭐ 给项目点个 Star
- 💰 [通过 GitHub Sponsors 赞助](https://github.com/sponsors/sbamdanb-glitch)
- 📢 分享给更多开发者

## 📄 开源协议

本项目采用 MIT 协议开源 - 查看 [LICENSE](LICENSE) 文件了解详情

## 🔗 相关链接

- [Algora 悬赏平台](https://algora.io/)
- [GitHub Sponsors](https://github.com/sponsors)
- [开源项目挣钱实用手册](https://github.com/wizicer/FinancialSupportForOpenSource)

---

**Made with ❤️ by developers, for developers**
