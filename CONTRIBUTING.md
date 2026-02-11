# 贡献指南

感谢您对 GitHub Bounty Hunter 项目的关注！我们欢迎任何形式的贡献。

## 如何贡献

### 报告 Bug

如果您发现了 Bug，请：

1. 检查 [Issues](https://github.com/sbamdanb-glitch/zhuanqian/issues) 中是否已有相同问题
2. 如果没有，创建一个新的 Issue，包含：
   - Bug 的详细描述
   - 复现步骤
   - 预期行为
   - 实际行为
   - 环境信息（操作系统、Python 版本等）

### 提出新功能

如果您有新功能的想法：

1. 先创建一个 Issue 讨论这个功能
2. 说明为什么需要这个功能
3. 描述您期望的实现方式

### 提交代码

1. **Fork 本仓库**

2. **创建您的特性分支**
   ```bash
   git checkout -b feature/AmazingFeature
   ```

3. **进行您的修改**
   - 确保代码符合 PEP 8 规范
   - 添加必要的注释
   - 如果添加新功能，请更新文档

4. **提交您的更改**
   ```bash
   git commit -m 'feat: 添加某个很棒的功能'
   ```
   
   提交信息格式：
   - `feat:` 新功能
   - `fix:` Bug 修复
   - `docs:` 文档更新
   - `style:` 代码格式调整
   - `refactor:` 代码重构
   - `test:` 测试相关
   - `chore:` 构建过程或辅助工具的变动

5. **推送到您的 Fork**
   ```bash
   git push origin feature/AmazingFeature
   ```

6. **创建 Pull Request**
   - 清楚地描述您的更改
   - 引用相关的 Issue（如果有）

## 开发环境设置

```bash
# 克隆您 fork 的仓库
git clone https://github.com/YOUR_USERNAME/zhuanqian.git
cd zhuanqian

# 安装开发依赖
pip install -r requirements.txt

# 运行测试
python3 bounty_hunter.py list --max-results 5
```

## 代码规范

- 遵循 PEP 8 代码风格
- 使用有意义的变量名和函数名
- 为复杂的逻辑添加注释
- 保持函数简洁，单一职责

## 测试

在提交 PR 之前，请确保：

- 代码能够正常运行
- 没有引入新的错误
- 所有功能都按预期工作

## 文档

如果您的更改涉及用户可见的功能：

- 更新 README.md
- 更新 USAGE.md
- 添加必要的示例

## 行为准则

- 尊重所有贡献者
- 接受建设性的批评
- 专注于对项目最有利的事情
- 对社区其他成员表示同理心

## 许可证

通过贡献代码，您同意您的贡献将在 MIT 许可证下发布。

## 问题？

如果您有任何问题，请随时：

- 创建 Issue
- 发送邮件至项目维护者

感谢您的贡献！🎉
