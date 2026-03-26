# Cost Guide

Understanding and controlling your MiroFish simulation costs.

---

## What costs money?

Every simulation makes many API calls to your LLM provider. The cost depends on:

- Number of simulation **rounds** (biggest factor)
- Number of **agents** generated
- Length of your **seed document**
- Which **LLM provider** you use

---

## Cost Estimator Tool

Always check before running:

```bash
# Interactive mode
python scripts/cost_estimator.py

# Direct parameters
python scripts/cost_estimator.py --rounds 20 --agents 100 --provider deepseek
```

---

## Rough Cost Reference

### Using Groq (Free tier)
All small and medium simulations are free within daily limits.

| Size | Rounds | Free? |
|---|---|---|
| Test | 10 | Yes |
| Medium | 20 | Usually yes |
| Large | 40+ | May hit daily limit |

### Using DeepSeek or Qwen (Paid)

| Size | Rounds | Approx Cost |
|---|---|---|
| Test | 10 | $0.02 – $0.05 |
| Medium | 20 | $0.10 – $0.30 |
| Large | 40 | $0.50 – $1.50 |
| Very Large | 80 | $2.00 – $6.00 |

---

## 5 Ways to Reduce Costs

### 1. Use Groq or Gemini free tiers for all testing

Both have generous free tiers. Only switch to a paid provider when you need more capacity.

### 2. Start with fewer rounds

Set in your `.env`:
```env
OASIS_DEFAULT_MAX_ROUNDS=10
```

You can always run additional rounds if needed.

### 3. Use shorter seed documents

A 1-page news article costs much less to process than a 50-page report.

### 4. Reduce Report Agent calls

```env
REPORT_AGENT_MAX_TOOL_CALLS=3
REPORT_AGENT_MAX_REFLECTION_ROUNDS=1
```

### 5. Run the estimator first

Always estimate before a large simulation — a 80-round simulation can cost $5–$10 on paid providers.

---

## Monitoring Your Usage

Check your usage dashboard on your LLM provider:
- Groq: [console.groq.com/usage](https://console.groq.com/usage)
- DeepSeek: [platform.deepseek.com](https://platform.deepseek.com)
- Qwen: Alibaba Bailian console
- OpenAI: [platform.openai.com/usage](https://platform.openai.com/usage)

Set up billing alerts where available to avoid surprises.
