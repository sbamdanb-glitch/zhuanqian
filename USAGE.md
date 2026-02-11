# 使用指南

## 安装

### 方式一：直接运行（推荐）

```bash
# 克隆仓库
git clone https://github.com/sbamdanb-glitch/zhuanqian.git
cd zhuanqian

# 安装依赖
pip install -r requirements.txt

# 运行工具
python3 bounty_hunter.py list
```

### 方式二：安装为命令行工具

```bash
# 克隆仓库
git clone https://github.com/sbamdanb-glitch/zhuanqian.git
cd zhuanqian

# 安装
pip install -e .

# 使用
bounty-hunter list
```

## 基本命令

### 列出所有悬赏任务

```bash
python3 bounty_hunter.py list
```

### 过滤高价值悬赏（≥$50）

```bash
python3 bounty_hunter.py list --min-amount 50
```

### 按技术栈过滤

```bash
python3 bounty_hunter.py list --tech python,react
```

### 限制结果数量

```bash
python3 bounty_hunter.py list --max-results 20
```

### 使用 GitHub Token（提高 API 限制）

```bash
# 设置环境变量
export GITHUB_TOKEN=your_github_token_here

# 或直接在命令中指定
python3 bounty_hunter.py list --token your_github_token_here
```

## 高级用法

### 组合多个过滤条件

```bash
python3 bounty_hunter.py list \
  --min-amount 100 \
  --tech python,typescript \
  --max-results 10 \
  --sort-by comments
```

## 获取 GitHub Token

1. 访问 https://github.com/settings/tokens
2. 点击 "Generate new token (classic)"
3. 选择 `public_repo` 权限
4. 生成并复制 token
5. 设置环境变量：`export GITHUB_TOKEN=your_token`

## 常见问题

### Q: 为什么有些任务显示金额为 0？

A: 某些悬赏任务的金额可能没有在标签或描述中明确标注，需要手动查看 issue 详情。

### Q: 如何提高搜索速度？

A: 使用 GitHub Personal Access Token 可以提高 API 请求限制，从而加快搜索速度。

### Q: 支持哪些排序方式？

A: 目前支持按创建时间（created）、更新时间（updated）和评论数（comments）排序。

## 贡献

欢迎提交 Issue 和 Pull Request！
