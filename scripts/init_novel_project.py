#!/usr/bin/env python3
"""Initialize a local novel project workspace.

Usage:
    python scripts/init_novel_project.py "项目名"
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path.cwd()

TEMPLATES = {
    "project-bible.md": """# 项目圣经\n\n## 基本信息\n\n- 项目名：{name}\n- 题材：\n- 目标平台：\n- 目标读者：\n- 字数目标：\n\n## 一句话卖点\n\n\n## 核心爽点\n\n1. \n2. \n3. \n\n## 主角\n\n- 身份：\n- 欲望：\n- 弱点：\n- 金手指：\n- 限制/代价：\n- 成长线：\n\n## 核心敌人\n\n- 表面敌人：\n- 深层敌人：\n- 资源：\n- 动机：\n- 底牌：\n\n## 长线秘密\n\n\n""",
    "characters.md": """# 人物表\n\n| 角色 | 表面身份 | 真实身份 | 欲望 | 恐惧 | 秘密 | 与主角关系 | 后续变化 |\n|---|---|---|---|---|---|---|---|\n""",
    "worldbuilding.md": """# 世界观设定\n\n## 时代背景\n\n\n## 力量体系\n\n| 等级/能力 | 表现 | 限制 | 代价 | 剧情用途 |\n|---|---|---|---|---|\n\n## 势力结构\n\n| 势力 | 目标 | 资源 | 与主角关系 | 隐藏秘密 |\n|---|---|---|---|---|\n\n## 隐藏真相\n\n- 前期误解：\n- 中期真相：\n- 后期反真相：\n""",
    "outline-volumes.md": """# 分卷大纲\n\n| 卷 | 主线目标 | 核心敌人 | 情绪主题 | 关键事件 | 高潮反转 | 结尾悬念 |\n|---|---|---|---|---|---|---|\n""",
    "outline-chapters.md": """# 章节卡\n\n| 章 | 标题 | 开局钩子 | 主要冲突 | 爽点 | 信息增量 | 人物变化 | 结尾钩子 |\n|---|---|---|---|---|---|---|---|\n""",
    "foreshadowing-ledger.md": """# 伏笔台账\n\n| ID | 出现章节 | 伏笔内容 | 类型 | 当前状态 | 回收建议 | 最佳回收章节 |\n|---|---|---|---|---|---|---|\n""",
    "review-notes.md": """# 审稿记录\n\n| 日期 | 章节 | 问题 | 修改建议 | 状态 |\n|---|---|---|---|---|\n""",
}


def slugify(name: str) -> str:
    cleaned = re.sub(r"[\\/:*?\"<>|]+", "-", name.strip())
    cleaned = re.sub(r"\s+", "-", cleaned)
    return cleaned or "untitled-novel"


def main() -> int:
    if len(sys.argv) < 2:
        print('Usage: python scripts/init_novel_project.py "项目名"')
        return 1

    name = sys.argv[1].strip()
    slug = slugify(name)
    target = ROOT / "novel_projects" / slug
    target.mkdir(parents=True, exist_ok=True)
    (target / "chapter-drafts").mkdir(exist_ok=True)

    for filename, template in TEMPLATES.items():
        path = target / filename
        if not path.exists():
            path.write_text(template.format(name=name), encoding="utf-8")

    print(f"Created novel project: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
