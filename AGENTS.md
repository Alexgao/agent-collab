# AGENTS

三方：Grok Bot（Kibo，默认组长）· Codex · Claude Code。共享仓库，异步「工作群」见 `TASKS/TEAM_CHAT.md`。

## 可见协同（像聊天群）
- 所有任务派发、讨论、结果、异议，**必须追加**到 `TASKS/TEAM_CHAT.md`（格式：`[时间] [发言人] 内容`）。
- 人类主要看：① 本文件的连续记录 ② Grok Bot 聊天里自动转发的新气泡（不必自己翻 git）。
- 不要把协同过程只写在各自私有会话里而不回写群聊。

## 分工（按任务类型动态认领，非死锁工种）
- 小范围代码实现 → 优先 Codex
- 长约束/文档/边界遵守 → 优先 Claude Code
- 编排、状态、push、@ 派活 → 默认 Grok Bot；拍板按任务类型，可异议
- **禁止**两人同时改同一路径；交叉校验默认只读

## Git / 自动 push（无需人类每次点头）
- 工作分支：任务相关 `codex/*` / `claude/*` / `grok/*`；演示稳定后合 `main`
- Agent **可以且应当**在完成有效 commit 后自动 `git push -u origin <当前分支>`（已存在则 `git push`）
- 开工前：`git pull --ff-only`（失败则停，写进 TEAM_CHAT，不 force）
- **禁止**对共享分支 `push --force` / `reset --hard` 已推送历史
- **不要** commit：auth 临时文件、密钥、大日志（见 `.gitignore`）
- 人类仍是仓库主人；说「停 push / 回滚」立即服从

## 调用约定
- 组长可用本机 headless：`codex exec …`、`claude -p "…"`（Claude 进程需带代理环境变量，见 TEAM_CHAT 已记录配方）
- 每次被调用：先读 `TEAM_CHAT.md` 末尾，再动手；结束时追加发言并 commit+push
