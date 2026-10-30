# Agent Collab — 给 Claude Code 的任务说明

> 读者：Claude Code（本机 CLI 或 Desktop 新会话）  
> 仓库：`E:\workspace\agent-collab`（远程 https://github.com/Alexgao/agent-collab）  
> 人类负责人：Alex（GitHub: Alexgao）  
> 协同方：Grok Bot（Kibo）· Codex · Claude Code

请先读完本文再动手。不要改与当前任务无关的文件，不要改账户/授权设置，不要往无关的旧会话里写东西。

---

## 我们在做什么

搭建一个 **Grok Bot / Codex / Claude Code** 共用的本机协作仓库：同一工作区、同一 Git 远程，按角色分工完成小任务并推送到 GitHub。

当前进行中的是一次 **端到端演示（E2E）**：

1. **Codex**（已完成）：在分支 `codex/word-freq-demo` 上写词频脚本。  
   - 提交：`4c93adb` — `codex: add word frequency counter script`  
   - 文件：`tools/wordfreq/count_words.py`、`sample.txt`、`sample.txt.wordfreq.json`
2. **Claude Code**（待你完成）：为该脚本写 Markdown README，并单独提交。  
3. **Grok Bot**：协调、开仓库/远程、汇报；**不要**代替 Claude 写 README（除非人类明确改口）。

远程目前只有 `main`（`c43a9ca`）；词频分支尚未 push。README 提交后由 Grok 或人类 push `codex/word-freq-demo`。

---

## 角色边界

| 角色 | 负责 | 不要做 |
|------|------|--------|
| Grok Bot | 编排、GitHub 连接器、状态汇报 | 不擅自往你的旧 Desktop 会话塞指令 |
| Codex | 实现脚本/工具代码 | 不写本次 README |
| Claude Code | `tools/wordfreq/README.md` + 仅含该文件的 commit | 不改 `.py` / sample、不改 `AGENTS.md`、不动授权 |

---

## 请你现在执行的具体任务

**工作目录**：`E:\workspace\agent-collab`  
**分支**：`codex/word-freq-demo`（若未检出，先 `git checkout codex/word-freq-demo`）

1. 阅读 `tools/wordfreq/count_words.py`，文档必须与真实 CLI 一致。  
2. **新建** `tools/wordfreq/README.md`（短文即可），包含：  
   - 要求：Python 3  
   - 参数：位置参数 `input`；可选 `-o` / `--output`（默认 `<input>.wordfreq.json`）  
   - 可复制示例：对 `sample.txt` 运行并得到 `sample.txt.wordfreq.json`  
   - 简述 JSON 字段：`source`、`total_words`、`unique_words`、`counts`  
3. **不要**修改 Python 脚本或 sample 相关文件。  
4. **只**提交 README：

```bash
git add tools/wordfreq/README.md
git commit -m "claude: add wordfreq README"
```

5. 完成后打印：README 路径 + 一行摘要 + 提交 hash。  
   **先不要** `git push`，除非人类或 Grok 明确要求。

---

## 脚本行为速览（写 README 用）

- 从 UTF-8 文本中用 Unicode 词模式提取单词，**大小写不敏感**（`casefold`）。  
- 输出 JSON：按频次降序，同频按词序。  
- 示例：`python tools/wordfreq/count_words.py tools/wordfreq/sample.txt`

---

## 环境与已知问题（供你知情，不必你修）

- Grok Bot 的 GitHub 连接器已可用；本机 `gh` CLI 可能仍未登录（与连接器无关）。  
- 独立 `claude` CLI 的 OAuth 可能因 Cloudflare 对换 token 返回 **403** 失败；**Claude Desktop 已登录**可用。  
- 若用 Desktop：请在 **新会话** 中打开本仓库目录执行，**不要**接在无关旧对话后面。  
- 不要触发或重复 GitHub/Claude 授权弹窗循环。

---

## 成功标准

- [ ] 存在 `tools/wordfreq/README.md` 且内容与 CLI 一致  
- [ ] 最新提交信息为 `claude: add wordfreq README` 且仅含该文件  
- [ ] 工作区无未提交的 README 改动；脚本与 sample 未被改动  

---

## 协作约定（请遵守）

1. 只动任务范围内的路径。  
2. 需要更大权限或 push/改远程时，先说明再等确认。  
3. 本说明由 Grok Bot（Kibo）根据 2026-10-30 会话整理；有冲突以人类最新口头指示为准。
