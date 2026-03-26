# Quick Start Guide

Get MiroFish Enhanced running in 10 minutes.

---

## Step 1 — Get API Keys (5 minutes)

You need 2 keys. Both have free tiers.

### LLM Key (choose one)

**Groq — Fastest free option:**
1. Go to [console.groq.com](https://console.groq.com)
2. Sign up with Google or email
3. Go to API Keys section
4. Click "Create API Key"
5. Copy the key

**Google Gemini — Also free:**
1. Go to [aistudio.google.com](https://aistudio.google.com)
2. Sign in with Google
3. Click "Get API Key"
4. Copy the key

### Zep Key (agent memory)
1. Go to [app.getzep.com](https://app.getzep.com)
2. Sign up free
3. Go to Settings → API Keys
4. Copy the key

---

## Step 2 — Install (3 minutes)

```bash
git clone https://github.com/YOUR_USERNAME/MiroFish-Enhanced.git
cd MiroFish-Enhanced
cp .env.example .env
npm run setup:all
```

---

## Step 3 — Configure (1 minute)

Open `.env` file and fill in your keys.

If using Groq:
```env
LLM_API_KEY=your_groq_key_here
LLM_BASE_URL=https://api.groq.com/openai/v1
LLM_MODEL_NAME=llama-3.3-70b-versatile
ZEP_API_KEY=your_zep_key_here
```

If using Gemini Flash:
```env
LLM_API_KEY=your_gemini_key_here
LLM_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/
LLM_MODEL_NAME=gemini-2.0-flash
ZEP_API_KEY=your_zep_key_here
```

---

## Step 4 — Start

```bash
npm run dev
```

Open **http://localhost:3000**

---

## Step 5 — Your First Simulation

1. Click **New Project**
2. Upload a news article (copy-paste text or upload PDF)
3. Type your prediction question — for example:
   - "How will public opinion shift about this?"
   - "How will markets react to this announcement?"
4. Set rounds to **10** for your first test
5. Click **Start Simulation**
6. Wait 5–10 minutes
7. Read your prediction report!

---

## Tips for First-Time Users

- Start with **10 rounds maximum** — you can always run more later
- Use **short documents** (1–3 pages) for your first simulation
- The first simulation always takes longest — subsequent ones are faster
- If simulation fails, check your API keys in `.env`

---

## Something Not Working?

See [Troubleshooting Guide](./troubleshooting.md)
