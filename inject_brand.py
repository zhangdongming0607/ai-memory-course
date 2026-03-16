#!/usr/bin/env python3
"""Inject brand CSS and navigation into all chapter HTML files."""

import re
from pathlib import Path

BUILD_DIR = Path(__file__).parent

CHAPTERS = [
    ("01-what-is-llm", "LLM 是什么"),
    ("02-talk-to-llm", "和 LLM 对话"),
    ("03-extract-structured-info", "让 AI 提取结构化信息"),
    ("04-memory-storage", "记忆的存储"),
    ("05-memory-update", "记忆的更新"),
    ("06-memory-in-prompt", "记忆的应用"),
    ("07-hands-on-mem0", "实战：联系人记忆"),
    ("08-streaming-sse", "流式输出"),
    ("09-async-tasks", "后台任务"),
    ("10-your-system", "回到你们的系统"),
]

BRAND_CSS = """
<style id="youyou-brand">
/* === YouYou AI Brand Theme === */
:root {
  --yy-purple: #B07CD8;
  --yy-mint: #5DE8C8;
  --yy-yellow: #F5D56E;
  --yy-bg-start: #fdf2f8;
  --yy-bg-mid: #ede9fe;
  --yy-bg-end: #fef3c7;
  --yy-text: #1e1b2e;
  --yy-text-secondary: #6b7280;
}

body.jp-Notebook {
  background: linear-gradient(135deg, var(--yy-bg-start) 0%, var(--yy-bg-mid) 50%, var(--yy-bg-end) 100%) !important;
  background-attachment: fixed !important;
  padding-top: 64px !important;
  font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "PingFang SC", "Noto Sans SC", sans-serif !important;
}

body.jp-Notebook > main {
  max-width: 820px !important;
  margin: 0 auto !important;
  padding: 0 20px 80px !important;
}

/* Navigation bar */
.yy-nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  background: rgba(255,255,255,0.82);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 1px solid rgba(176, 124, 216, 0.1);
  padding: 0 20px;
  height: 52px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "PingFang SC", sans-serif;
}

.yy-nav a {
  text-decoration: none;
  color: var(--yy-text);
  font-size: 0.85em;
  font-weight: 500;
  padding: 6px 12px;
  border-radius: 10px;
  transition: all 0.2s;
}

.yy-nav a:hover {
  background: rgba(176, 124, 216, 0.1);
  color: var(--yy-purple);
}

.yy-nav-title {
  font-size: 0.85em !important;
  font-weight: 600 !important;
  color: var(--yy-text) !important;
  text-align: center;
  flex: 1;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  padding: 0 8px !important;
}

.yy-nav-left, .yy-nav-right {
  min-width: 80px;
}

.yy-nav-right {
  text-align: right;
}

.yy-nav a.disabled {
  opacity: 0.3;
  pointer-events: none;
}

/* Cards / Cells */
.jp-Cell {
  background: rgba(255, 255, 255, 0.72) !important;
  backdrop-filter: blur(10px) !important;
  -webkit-backdrop-filter: blur(10px) !important;
  border-radius: 16px !important;
  margin-bottom: 16px !important;
  border: 1px solid rgba(255,255,255,0.6) !important;
  box-shadow: 0 2px 12px rgba(140, 100, 180, 0.06) !important;
  overflow: hidden;
}

.jp-Cell:hover {
  box-shadow: 0 4px 20px rgba(140, 100, 180, 0.1) !important;
}

/* Headings */
.jp-RenderedHTMLCommon h1 {
  background: linear-gradient(135deg, var(--yy-purple) 0%, #8b5cf6 50%, var(--yy-mint) 100%) !important;
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  background-clip: text !important;
  font-weight: 800 !important;
  margin-top: 8px !important;
}

.jp-RenderedHTMLCommon h2 {
  color: #4c1d95 !important;
  font-weight: 700 !important;
  border-bottom: 2px solid rgba(176, 124, 216, 0.15) !important;
  padding-bottom: 8px !important;
}

.jp-RenderedHTMLCommon h3 {
  color: #5b21b6 !important;
  font-weight: 650 !important;
}

/* Hide anchor links */
.anchor-link { display: none !important; }

/* Code blocks */
.jp-Cell.jp-CodeCell {
  border-left: 3px solid var(--yy-purple) !important;
}

.jp-InputPrompt, .jp-OutputPrompt {
  color: var(--yy-purple) !important;
  font-weight: 600 !important;
}

/* Tables */
.jp-RenderedHTMLCommon table {
  border-radius: 12px !important;
  overflow: hidden !important;
  border: none !important;
  box-shadow: 0 1px 6px rgba(140, 100, 180, 0.08) !important;
}

.jp-RenderedHTMLCommon th {
  background: linear-gradient(135deg, #ede9fe, #fdf2f8) !important;
  color: #4c1d95 !important;
  font-weight: 600 !important;
  border: none !important;
  padding: 10px 14px !important;
}

.jp-RenderedHTMLCommon td {
  border: none !important;
  border-top: 1px solid rgba(176, 124, 216, 0.1) !important;
  padding: 10px 14px !important;
}

.jp-RenderedHTMLCommon tr:nth-child(even) {
  background: rgba(237, 233, 254, 0.2) !important;
}

/* Blockquotes */
.jp-RenderedHTMLCommon blockquote {
  border-left: 4px solid var(--yy-purple) !important;
  background: rgba(237, 233, 254, 0.3) !important;
  border-radius: 0 12px 12px 0 !important;
  padding: 12px 16px !important;
  margin: 12px 0 !important;
}

/* Links */
.jp-RenderedHTMLCommon a {
  color: #7c3aed !important;
  text-decoration-color: rgba(124, 58, 237, 0.3) !important;
}

.jp-RenderedHTMLCommon a:hover {
  color: var(--yy-purple) !important;
  text-decoration-color: var(--yy-purple) !important;
}

/* Inline code */
.jp-RenderedHTMLCommon code:not(.highlight code) {
  background: rgba(237, 233, 254, 0.5) !important;
  color: #7c3aed !important;
  border-radius: 6px !important;
  padding: 2px 6px !important;
  font-size: 0.9em !important;
}

/* Bottom navigation */
.yy-bottom-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 24px 0;
  margin-top: 32px;
  font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "PingFang SC", sans-serif;
}

.yy-bottom-nav a {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 10px 20px;
  background: rgba(255,255,255,0.75);
  border: 1px solid rgba(255,255,255,0.6);
  border-radius: 12px;
  text-decoration: none;
  color: var(--yy-text);
  font-size: 0.9em;
  font-weight: 500;
  box-shadow: 0 2px 12px rgba(140, 100, 180, 0.08);
  transition: all 0.2s;
}

.yy-bottom-nav a:hover {
  box-shadow: 0 4px 16px rgba(140, 100, 180, 0.16);
  transform: translateY(-1px);
  color: #7c3aed;
}

.yy-bottom-nav a.disabled {
  opacity: 0.3;
  pointer-events: none;
}

/* Responsive */
@media (max-width: 600px) {
  body.jp-Notebook > main { padding: 0 12px 60px !important; }
  .jp-Cell { border-radius: 12px !important; }
  .yy-nav { padding: 0 12px; }
  .yy-nav-left, .yy-nav-right { min-width: 56px; }
}
</style>
"""


def build_nav_html(chapter_idx):
    prev_link = ""
    next_link = ""
    title = CHAPTERS[chapter_idx][1]

    if chapter_idx > 0:
        prev_file = CHAPTERS[chapter_idx - 1][0]
        prev_link = f'<a href="{prev_file}.html">&lsaquo; 上一课</a>'
    else:
        prev_link = '<a class="disabled">&lsaquo; 上一课</a>'

    if chapter_idx < len(CHAPTERS) - 1:
        next_file = CHAPTERS[chapter_idx + 1][0]
        next_link = f'<a href="{next_file}.html">下一课 &rsaquo;</a>'
    else:
        next_link = '<a class="disabled">下一课 &rsaquo;</a>'

    nav = f"""<nav class="yy-nav">
  <div class="yy-nav-left">{prev_link}</div>
  <a href="index.html" class="yy-nav-title">{title}</a>
  <div class="yy-nav-right">{next_link}</div>
</nav>"""

    # Bottom nav with more detail
    if chapter_idx > 0:
        prev_name = CHAPTERS[chapter_idx - 1][1]
        prev_file = CHAPTERS[chapter_idx - 1][0]
        bottom_prev = f'<a href="{prev_file}.html">&lsaquo; {prev_name}</a>'
    else:
        bottom_prev = '<a class="disabled">&lsaquo;</a>'

    if chapter_idx < len(CHAPTERS) - 1:
        next_name = CHAPTERS[chapter_idx + 1][1]
        next_file = CHAPTERS[chapter_idx + 1][0]
        bottom_next = f'<a href="{next_file}.html">{next_name} &rsaquo;</a>'
    else:
        bottom_next = '<a href="index.html">返回课程首页</a>'

    bottom_nav = f"""<div class="yy-bottom-nav">
  {bottom_prev}
  {bottom_next}
</div>"""

    return nav, bottom_nav


def inject_chapter(chapter_idx):
    slug, title = CHAPTERS[chapter_idx]
    filepath = BUILD_DIR / f"{slug}.html"

    if not filepath.exists():
        print(f"  SKIP: {filepath} not found")
        return

    content = filepath.read_text("utf-8")

    # Remove any previous injection
    content = re.sub(r'<style id="youyou-brand">.*?</style>', '', content, flags=re.DOTALL)
    content = re.sub(r'<nav class="yy-nav">.*?</nav>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div class="yy-bottom-nav">.*?</div>', '', content, flags=re.DOTALL)

    top_nav, bottom_nav = build_nav_html(chapter_idx)

    # Inject CSS before </head>
    content = content.replace('</head>', BRAND_CSS + '\n</head>')

    # Inject top nav after <body...>
    content = re.sub(
        r'(<body[^>]*>)',
        rf'\1\n{top_nav}',
        content,
        count=1
    )

    # Inject bottom nav before </main>
    content = content.replace('</main>', bottom_nav + '\n</main>')

    # Update page title
    content = re.sub(
        r'<title>[^<]*</title>',
        f'<title>{title} - AI 记忆系统入门课程</title>',
        content,
        count=1
    )

    filepath.write_text(content, "utf-8")
    print(f"  OK: {slug}.html")


if __name__ == "__main__":
    print("Injecting YouYou AI brand into chapter pages...")
    for i in range(len(CHAPTERS)):
        inject_chapter(i)
    print("Done!")
