# 造梦司 DreamForge Studio 项目指令

本仓库是一个中文小说、网文、AI 短剧创作 Agent 团队 Skill。

当用户在本项目中请求小说创作、网文策划、章节扩写、短剧改编、伏笔检查、AI 味审稿时，优先使用 `SKILL.md` 中定义的造梦司工作流。

## 工作原则

- 中文优先。
- 表格优先。
- 先推进，少追问。
- 默认商业网文/短剧节奏：强钩子、强冲突、强反转、少废话。
- 不复刻在世作者文风，不照搬版权作品。
- 输出必须可直接复制到小说项目、Codex、Marvis 或其他 Agent 工具中。

## 项目资产建议

每个小说项目建议维护：

```text
project-bible.md
characters.md
worldbuilding.md
outline-volumes.md
outline-chapters.md
foreshadowing-ledger.md
review-notes.md
chapter-drafts/
```

可运行：

```bash
python scripts/init_novel_project.py "小说名"
```
