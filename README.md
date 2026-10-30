# agent-collab

共用工作目录：Grok Bot（调度）· Codex（分支开发/测试）· Claude Code（只读审查）。

## 角色
- **Grok Bot**：建任务卡、盯进度、汇总结果；不直接改主分支业务代码。
- **Codex**：在独立分支实现与自测，提交变更/PR。
- **Claude Code**：只读审查差异，输出意见；默认不写生产分支。
- **你**：合并、部署、密钥与购买必须人工批准。

## 目录约定
- `TASKS/` 任务卡（Markdown）
- `docs/workflow.md` 半自动闭环说明
- 代码变更只在 feature 分支进行

## 工具入口（本机）
- Codex CLI：已在 PATH（`codex`）
- Claude Code：见 `tools/claude.cmd` 或用户 PATH 中的 `claude`
- Git：`git`

不要在此仓库直接启动试跑任务，除非用户明确要求。
