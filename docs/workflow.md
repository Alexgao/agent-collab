# 半自动闭环（来自 Codex 语音会话「搭建 Agent 协作流程」）

1. 你提出目标 → Grok Bot 整理需求与验收标准，写入 `TASKS/`。
2. Grok Bot 交给 Codex：在独立分支开发并测试。
3. Codex 提交 PR / 变更结果。
4. Claude Code 只做独立审查。
5. 有问题 → 回 Codex；测试通过 → 你确认合并或部署。

权限边界：Grok 可建任务和读结果；Codex 可在独立分支写代码；Claude 默认只读；合并/部署/删除/购买/密钥必须你批准。
