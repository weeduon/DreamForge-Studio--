# 安装说明：Codex / Marvis

## 1. Codex 用户级安装

把本仓库复制到：

```bash
~/.agents/skills/dreamforge-studio
```

Windows PowerShell：

```powershell
New-Item -ItemType Directory -Force "$HOME\.agents\skills"
git clone https://github.com/weeduon/DreamForge-Studio-- "$HOME\.agents\skills\dreamforge-studio"
```

macOS / Linux：

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/weeduon/DreamForge-Studio-- ~/.agents/skills/dreamforge-studio
```

## 2. Codex 项目级安装

在目标项目根目录执行：

```bash
mkdir -p .agents/skills
git clone https://github.com/weeduon/DreamForge-Studio-- .agents/skills/dreamforge-studio
```

调用：

```text
$dreamforge-studio 帮我创建一个都市玄学爽文项目，并生成前三章章节卡。
```

## 3. Marvis 使用

### 方式 A：支持 Skill 文件夹

直接导入整个仓库文件夹。

### 方式 B：只支持单提示词

复制 `MARVIS_SINGLE_PROMPT.md` 的全部内容，作为系统提示词或角色设定。

### 方式 C：支持多 Agent

按 `SKILL.md` 中的 8 个 Agent 拆成独立 Agent：

- 掌题使
- 造界师
- 塑魂师
- 织卷师
- 执笔官
- 照妖镜
- 藏线人
- 分镜使

## 4. 初始化小说项目

```bash
python scripts/init_novel_project.py "我的小说名"
```

生成目录：

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
