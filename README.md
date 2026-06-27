# 造梦司 DreamForge Studio

**造梦司**是一个面向中文小说、网文、AI 短剧创作的 Agent 团队 Skill。它不是“随机写一章”的玩具，而是把立项、世界观、人设、大纲、正文、审稿、伏笔和短剧改编拆成可复用工作流。毕竟写作已经够痛苦了，没必要再让文件散得像灾难现场。

## 核心能力

| Agent | 职位名 | 职责 |
|---|---|---|
| 爆款编辑 Agent | 掌题使 | 题材定位、卖点、金手指、前三章钩子 |
| 世界观 Agent | 造界师 | 世界观圣经、力量体系、势力结构、隐藏真相 |
| 人物 Agent | 塑魂师 | 主角、配角、反派、人物关系矩阵、秘密与欲望 |
| 大纲 Agent | 织卷师 | 分卷大纲、章节卡、追读节奏、转折点 |
| 正文 Agent | 执笔官 | 按章节卡扩写正文、控制对话和画面感 |
| 审稿 Agent | 照妖镜 | 检查 AI 味、逻辑漏洞、节奏拖沓、人物动机 |
| 伏笔 Agent | 藏线人 | 登记伏笔、追踪状态、规划回收章节 |
| 短剧改编 Agent | 分镜使 | 小说改短剧、分集、分镜、AI 视频提示词 |

## 仓库结构

```text
dreamforge-studio/
├── SKILL.md                         # Codex / Agent Skills 主入口
├── AGENTS.md                        # Codex 项目级指令
├── INSTALL-Codex-Marvis.md          # Codex / Marvis 安装说明
├── MARVIS_SINGLE_PROMPT.md          # Marvis 单提示词版本
├── scripts/init_novel_project.py     # 初始化小说项目目录
├── examples/urban-mystic-novel-start.md
├── LICENSE
└── README.md
```

## Codex 安装

### 用户级安装

把整个仓库文件夹复制到：

```bash
~/.agents/skills/dreamforge-studio
```

Windows PowerShell：

```powershell
New-Item -ItemType Directory -Force "$HOME\.agents\skills"
Copy-Item -Recurse ".\DreamForge-Studio--" "$HOME\.agents\skills\dreamforge-studio"
```

macOS / Linux：

```bash
mkdir -p ~/.agents/skills
cp -R ./DreamForge-Studio-- ~/.agents/skills/dreamforge-studio
```

### 项目级安装

```bash
mkdir -p .agents/skills
cp -R ./DreamForge-Studio-- .agents/skills/dreamforge-studio
```

调用示例：

```text
$dreamforge-studio 我要写一本都市玄学爽文，主角是被直播平台封杀的落魄相师，帮我做爆款立项、世界观、人设矩阵和前三章章节卡。
```

## Marvis 使用

| Marvis 支持能力 | 使用方式 |
|---|---|
| 支持 Skill 文件夹 | 直接导入整个仓库文件夹 |
| 只支持单提示词 | 复制 `MARVIS_SINGLE_PROMPT.md` |
| 支持多 Agent | 按 `SKILL.md` 内的 8 个 Agent 拆分创建 |

## 初始化小说项目

在 Skill 根目录运行：

```bash
python scripts/init_novel_project.py "我的小说名"
```

会生成：

```text
novel_projects/我的小说名/
├── project-bible.md
├── characters.md
├── worldbuilding.md
├── outline-volumes.md
├── outline-chapters.md
├── foreshadowing-ledger.md
├── review-notes.md
└── chapter-drafts/
```

## 推荐调用

```text
$dreamforge-studio 帮我做一个都市玄学爽文立项，要求强设定、强反转、短剧感、适合改编成 AI 短剧。
```

```text
$dreamforge-studio 把这个创意拆成五卷大纲，每卷 30 章，并标出每卷高潮反转和伏笔回收点。
```

```text
$dreamforge-studio 根据第 1 章章节卡写 2500 字正文，要求强冲突、多对话、少解释、结尾留钩子。
```

## 许可证

默认使用 MIT License。商业使用前请自行确认你接入的平台、模型和素材来源授权。是的，版权仍然存在，哪怕 AI 圈有些人装作没看见。
