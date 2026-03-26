# API Keys Guide

MiroFish needs 2 API keys to run. Both have free tiers.

---

## Key 1 — LLM API Key

This powers the AI reasoning of all agents. Choose any provider:

### Groq (Free tier — Recommended for beginners)

1. Go to [console.groq.com](https://console.groq.com)
2. Click "Sign Up" — use Google or email
3. In left sidebar, click "API Keys"
4. Click "Create API Key"
5. Give it a name like "mirofish"
6. Copy the key immediately (it only shows once)

In your `.env`:
```
LLM_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxx
LLM_BASE_URL=https://api.groq.com/openai/v1
LLM_MODEL_NAME=llama-3.3-70b-versatile
```

### Alibaba Qwen (Cheapest paid — Best compatibility)

1. Go to [bailian.console.aliyun.com](https://bailian.console.aliyun.com)
2. Sign up (requires phone number)
3. Navigate to API Key section
4. Create and copy your key

In your `.env`:
```
LLM_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
LLM_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
LLM_MODEL_NAME=qwen-plus
```

### DeepSeek (Very cheap, high quality)

1. Go to [platform.deepseek.com](https://platform.deepseek.com)
2. Sign up
3. Go to API section
4. Create API key

In your `.env`:
```
LLM_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
LLM_BASE_URL=https://api.deepseek.com/v1
LLM_MODEL_NAME=deepseek-chat
```

---

## Key 2 — Zep Cloud Key (Agent Memory)

Zep stores long-term memory for each agent across simulation rounds.

1. Go to [app.getzep.com](https://app.getzep.com)
2. Click "Sign Up"
3. Verify your email
4. Go to Settings in the top right
5. Click "API Keys"
6. Click "New API Key"
7. Copy the key

In your `.env`:
```
ZEP_API_KEY=z_xxxxxxxxxxxxxxxxxxxx
```

**Free tier**: Enough for experimentation and small simulations.

---

## Common Mistakes

- Do not share your API keys publicly
- Do not commit `.env` to GitHub (it is already in `.gitignore`)
- If a key stops working, generate a new one from the provider dashboard
- Make sure there are no spaces around the `=` sign in `.env`

---

## Cost Monitoring

Always run the cost estimator before large simulations:

```bash
python scripts/cost_estimator.py --rounds 20 --agents 100 --provider groq
```
