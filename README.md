# AI 记忆系统入门课程

> 专为前端开发者设计，从零理解 AI 记忆系统的工作原理。

## 课程目标

学完这门课后，你能看懂你们项目的 `memory_system_overview.md`，理解后端同事在做什么，并能参与记忆系统的技术讨论。

## 课程大纲

| 课 | 主题 | 你会学到 |
|---|---|---|
| 01 | LLM 是什么 | Token、Prompt、Context Window 这些基本概念 |
| 02 | 和 LLM 对话 | 用 Python 调 OpenAI/Claude API，亲手发一条消息 |
| 03 | 让 AI 提取结构化信息 | Prompt Engineering、JSON 输出、从聊天记录提取人物信息 |
| 04 | 记忆的存储 | 数据库存储 vs 向量检索，Embedding 是什么 |
| 05 | 记忆的更新 | 新旧信息冲突怎么办、增量更新、Mem0 的方案 |
| 06 | 记忆的应用 | RAG 是什么、怎么把记忆注入 Prompt |
| 07 | 实战：联系人记忆 | 用 Mem0 搭一个简化版的联系人记忆系统 |
| 08 | 流式输出 | SSE 协议、打字机效果、前端怎么接 |
| 09 | 后台任务 | 异步队列、任务链、为什么需要它 |
| 10 | 回到你们的系统 | 逐块解读 memory_system_overview.md |

## 环境准备

```bash
# 1. 创建虚拟环境
cd /Users/bytedance/StudioProjects/ai-memory-course
python3.12 -m venv .venv
source .venv/bin/activate

# 2. 安装依赖
pip install jupyter openai anthropic mem0ai chromadb

# 3. 启动 Jupyter
jupyter notebook

# 或者直接在 VSCode 中打开 .ipynb 文件（需安装 Jupyter 扩展）
```

## 需要的 API Key

课程中会调用 LLM API，你需要准备至少一个：
- OpenAI API Key（推荐，课程示例默认用这个）：https://platform.openai.com/api-keys
- 或 Anthropic API Key：https://console.anthropic.com/

在课程目录创建 `.env` 文件：
```
OPENAI_API_KEY=sk-xxx
```

## 学习建议

- 每节课预计 30-60 分钟
- 建议按顺序学，每节课都依赖前面的知识
- 代码 cell 一定要自己跑一遍，改改参数看看效果
- 遇到不懂的随时问我
