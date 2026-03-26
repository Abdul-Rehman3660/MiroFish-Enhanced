<div align="center">

<img src="./static/image/MiroFish_logo_compressed.jpeg" alt="MiroFish Logo" width="75%"/>

# 🐟 MiroFish Enhanced

### A Universal Swarm Intelligence Engine — Predicting Anything

*SimCity meets AI Forecasting — Build digital worlds, simulate society, predict the future*

[![GitHub Stars](https://img.shields.io/github/stars/666ghj/MiroFish?style=flat-square&color=DAA520)](https://github.com/666ghj/MiroFish/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/666ghj/MiroFish?style=flat-square)](https://github.com/666ghj/MiroFish/network)
[![License](https://img.shields.io/badge/License-AGPL%20v3-blue?style=flat-square)](./LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11%2B-green?style=flat-square&logo=python)](https://python.org)
[![Node](https://img.shields.io/badge/Node.js-18%2B-green?style=flat-square&logo=node.js)](https://nodejs.org)
[![Discord](https://img.shields.io/badge/Discord-Join-5865F2?style=flat-square&logo=discord)](http://discord.gg/ePf5aPaHnA)

[English](./README-EN.md) | [Chinese / 中文](./README.md)

> **This is an enhanced fork** adding full English documentation, Windows support,
> free LLM alternatives, a cost estimator, and contributor guides.
> Original project: [666ghj/MiroFish](https://github.com/666ghj/MiroFish)

</div>

---

## What is MiroFish?

MiroFish is a **next-generation AI prediction engine** that does NOT predict the future by crunching numbers. Instead, it **builds a miniature version of society** and runs it forward at accelerated speed.

You feed it a news article, financial report, policy document, or even a novel. MiroFish spawns **thousands of AI agents** — each with a unique personality, memory, and social connections. These agents debate, argue, form coalitions, and change their minds. Their collective behavior produces a **prediction report** about what might happen next.

> Think of it as **SimCity for prediction** — but instead of buildings, you are simulating human society.

### How is this different from ChatGPT?

| Regular AI (ChatGPT etc.) | MiroFish |
|---|---|
| One model, one answer | Thousands of agents, emergent behavior |
| Static response | Living, evolving simulation |
| Single perspective | Entire society of perspectives |
| Cannot simulate social dynamics | Built specifically for social dynamics |
| No "what if" injection | God's-eye view — inject variables mid-simulation |

---

## Real-World Results

- **Trading**: A developer connected MiroFish to a Polymarket trading bot, simulated 2,847 digital humans before every trade, and reported $4,266 profit over 338 trades
- **Public Opinion**: Simulated how sentiment evolved around a university controversy with time-sequenced opinion trajectories
- **Creative**: Fed 80 chapters of an ancient Chinese novel and predicted the lost ending based on character behavior
- **Finance**: Simulated how retail investors, institutional players, and analysts react differently to market signals

---

## How It Works — 5 Steps

```
Step 1  Upload Seed Material
        News article, report, policy draft, or novel

Step 2  Knowledge Graph Built  (GraphRAG)
        Extracts entities, relationships, key players

Step 3  Thousands of AI Agents Generated
        Each gets: unique personality + long-term memory + social network

Step 4  Dual-Platform Simulation Runs
        Twitter-like + Reddit-like environments
        Agents post, argue, follow, debate, shift opinions

Step 5  Prediction Report Generated
        ReportAgent analyzes emergent patterns
        Chat with any agent or inject new variables
```

---

## Enhancements in This Fork

| Feature | Original | This Fork |
|---|---|---|
| English README | Basic | Comprehensive |
| Windows setup | Not supported | Full guide + script |
| Free LLM options | Not documented | 4 free/cheap providers |
| Cost estimator | None | Python script included |
| Troubleshooting guide | None | Common issues documented |
| Contributing guide | None | Full CONTRIBUTING.md |
| Issue templates | None | Bug + Feature templates |
| English code comments | Partial | All key files translated |

---

## Installation

### Prerequisites

| Tool | Version | Check |
|------|---------|-------|
| Node.js | 18+ | `node -v` |
| Python | 3.11 to 3.12 | `python --version` |
| uv | Latest | `uv --version` |

Install uv (Python package manager):

```bash
# macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Quick Start (macOS and Linux)

```bash
git clone https://github.com/YOUR_USERNAME/MiroFish-Enhanced.git
cd MiroFish-Enhanced
cp .env.example .env
# Edit .env with your API keys
npm run setup:all
npm run dev
```

Open **http://localhost:3000**

### Windows Setup

```powershell
git clone https://github.com/YOUR_USERNAME/MiroFish-Enhanced.git
cd MiroFish-Enhanced
.\scripts\windows\setup.ps1
npm run dev
```

See [docs/windows-setup.md](./docs/windows-setup.md) for step-by-step guide.

### Docker

```bash
cp .env.example .env
# Edit .env with your keys
docker compose up -d
```

---

## API Keys

MiroFish needs 2 API keys:

### 1. LLM API Key

Use ANY of these OpenAI-compatible providers:

| Provider | Cost | Sign Up |
|---|---|---|
| Alibaba Qwen (Recommended) | Cheapest | [bailian.console.aliyun.com](https://bailian.console.aliyun.com/) |
| DeepSeek | Very cheap | [platform.deepseek.com](https://platform.deepseek.com/) |
| Groq | Free tier | [console.groq.com](https://console.groq.com/) |
| Google Gemini Flash | Free tier | [aistudio.google.com](https://aistudio.google.com/) |
| OpenAI | Moderate | [platform.openai.com](https://platform.openai.com/) |

### 2. Zep Cloud Key (Agent Memory)

Sign up free at [app.getzep.com](https://app.getzep.com/) — free tier is enough for testing.

---

## Configuration

Edit your `.env` file:

```env
# LLM — choose one provider and uncomment it

# Alibaba Qwen (Cheapest — Recommended)
LLM_API_KEY=your_api_key_here
LLM_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
LLM_MODEL_NAME=qwen-plus

# DeepSeek (Uncomment to use)
# LLM_API_KEY=your_api_key_here
# LLM_BASE_URL=https://api.deepseek.com/v1
# LLM_MODEL_NAME=deepseek-chat

# Groq — Free tier (Uncomment to use)
# LLM_API_KEY=your_api_key_here
# LLM_BASE_URL=https://api.groq.com/openai/v1
# LLM_MODEL_NAME=llama-3.3-70b-versatile

# Google Gemini Flash — Free tier (Uncomment to use)
# LLM_API_KEY=your_api_key_here
# LLM_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/
# LLM_MODEL_NAME=gemini-2.0-flash

# Zep Memory (Required)
ZEP_API_KEY=your_zep_api_key_here

# Simulation settings (Optional)
OASIS_DEFAULT_MAX_ROUNDS=10
REPORT_AGENT_MAX_TOOL_CALLS=5
```

---

## Cost Estimation

Run before starting a simulation:

```bash
python scripts/cost_estimator.py --rounds 20 --agents 100 --provider qwen
```

Rough cost guide:

| Size | Rounds | Agents | Qwen | DeepSeek | Groq |
|---|---|---|---|---|---|
| Test | 10 | 50 | ~$0.05 | ~$0.03 | Free |
| Medium | 20 | 100 | ~$0.30 | ~$0.15 | ~$0.05 |
| Large | 40 | 200 | ~$1.50 | ~$0.80 | ~$0.30 |

Start with fewer than 40 rounds on your first run.

---

## Documentation

- [Quick Start Guide](./docs/quickstart.md)
- [Windows Setup Guide](./docs/windows-setup.md)
- [API Keys Guide](./docs/api-keys.md)
- [Cost Guide](./docs/cost-guide.md)
- [Free LLM Options](./docs/free-llm-options.md)
- [Troubleshooting](./docs/troubleshooting.md)
- [Contributing Guide](./CONTRIBUTING.md)

---

## Limitations

- Not a crystal ball — produces plausible scenarios, not guaranteed predictions
- Version 0.1 — early stage, expect rough edges
- Expensive at scale — large simulations use many API tokens
- AI agents show more herd behavior than real humans
- Better for qualitative prediction than exact numbers

---

## Contributing

All contributions welcome. See [CONTRIBUTING.md](./CONTRIBUTING.md).

Easy ways to start: report bugs, improve docs, add translations, fix issues.

---

## Credits

- Original MiroFish by [Guo Hangjiang](https://github.com/666ghj) — [666ghj/MiroFish](https://github.com/666ghj/MiroFish)
- Simulation engine: [OASIS by CAMEL-AI](https://github.com/camel-ai/oasis)
- Backed by: [Shanda Group](https://www.shanda.com/)
- License: AGPL v3

MiroFish team is hiring — send your CV to **mirofish@shanda.com**
