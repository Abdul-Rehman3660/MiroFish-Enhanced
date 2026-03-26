# Free and Cheap LLM Options for MiroFish

MiroFish works with any OpenAI-compatible API. Here are the best free and cheap options.

---

## Option 1 — Groq (Best Free Tier)

Groq offers a generous free tier with very fast inference.

**Sign up**: [console.groq.com](https://console.groq.com)

**.env configuration**:
```env
LLM_API_KEY=your_groq_api_key
LLM_BASE_URL=https://api.groq.com/openai/v1
LLM_MODEL_NAME=llama-3.3-70b-versatile
```

**Free tier limits**: Daily token limits — enough for several simulations per day.

**Best for**: Testing and small to medium simulations.

---

## Option 2 — Google Gemini Flash

Google offers a free tier through AI Studio.

**Sign up**: [aistudio.google.com](https://aistudio.google.com)

**.env configuration**:
```env
LLM_API_KEY=your_gemini_api_key
LLM_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/
LLM_MODEL_NAME=gemini-2.0-flash
```

**Free tier limits**: Generous — 1500 requests per day.

**Best for**: Regular use without paying.

---

## Option 3 — DeepSeek (Cheapest Paid)

If you want to pay a little, DeepSeek is the cheapest high-quality option.

**Sign up**: [platform.deepseek.com](https://platform.deepseek.com)

**.env configuration**:
```env
LLM_API_KEY=your_deepseek_api_key
LLM_BASE_URL=https://api.deepseek.com/v1
LLM_MODEL_NAME=deepseek-chat
```

**Cost**: About $0.27 per 1M tokens — roughly $0.03 for a small simulation.

**Best for**: Regular simulations at minimal cost.

---

## Option 4 — Alibaba Qwen (Recommended by MiroFish team)

The original MiroFish was built with Qwen — it works best.

**Sign up**: [bailian.console.aliyun.com](https://bailian.console.aliyun.com)

**.env configuration**:
```env
LLM_API_KEY=your_qwen_api_key
LLM_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
LLM_MODEL_NAME=qwen-plus
```

**Cost**: About $0.40 per 1M tokens.

**Best for**: Production use and best compatibility.

---

## Cost Comparison

Run the cost estimator before your simulation:

```bash
python scripts/cost_estimator.py --rounds 10 --agents 50 --provider groq
```

| Provider | 10 rounds / 50 agents | 20 rounds / 100 agents |
|---|---|---|
| Groq | Free (within limits) | Free (within limits) |
| Gemini Flash | Free (within limits) | Free (within limits) |
| DeepSeek | ~$0.02 | ~$0.12 |
| Qwen-Plus | ~$0.03 | ~$0.18 |
| OpenAI GPT-4o-mini | ~$0.04 | ~$0.28 |

---

## Tips to Reduce Cost

1. **Start small** — use 10 rounds and 50 agents for your first simulation
2. **Use Groq or Gemini free tiers** for all testing
3. **Only use paid providers** when you need larger simulations
4. **Set OASIS_DEFAULT_MAX_ROUNDS=10** in your .env to cap rounds
5. **Run the cost estimator** before every large simulation
