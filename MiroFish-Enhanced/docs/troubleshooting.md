# Troubleshooting Guide

Common problems and their solutions.

---

## Installation Issues

### "uv: command not found"

uv was not installed or PATH was not updated.

**Fix**:
```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.bashrc   # or source ~/.zshrc on Mac

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
# Then close and reopen terminal
```

### "npm run setup:all fails"

**Fix**: Run each step separately to find the error:
```bash
npm install
cd frontend && npm install && cd ..
cd backend && uv venv && uv pip install -r requirements.txt && cd ..
```

### Python version error (3.13 not supported)

MiroFish requires Python 3.11 or 3.12 — not 3.13.

**Fix**: Install Python 3.11 from [python.org](https://python.org/downloads/release/python-3118/)

---

## Startup Issues

### Backend fails to start — "LLM_API_KEY not configured"

Your .env file is missing or API keys are not set.

**Fix**:
```bash
cp .env.example .env
# Edit .env and add your API keys
```

### "ZEP_API_KEY not configured"

**Fix**: Sign up at [app.getzep.com](https://app.getzep.com) and get a free API key.

### Port already in use

**Fix**:
```bash
# macOS / Linux
lsof -ti:3000 | xargs kill -9
lsof -ti:5001 | xargs kill -9

# Windows
netstat -ano | findstr :3000
taskkill /PID <PID> /F
```

---

## Simulation Issues

### Simulation runs but produces no output

Usually an API key or model name issue.

**Fix**: Check your .env file — make sure LLM_MODEL_NAME matches a model your provider actually offers.

### Very high API costs

**Fix**: Reduce simulation rounds in .env:
```env
OASIS_DEFAULT_MAX_ROUNDS=10
```

### Simulation times out

**Fix**: Reduce agents and rounds. Start with 10 rounds maximum.

### "JSON format invalid" error

Some LLM providers return responses in unexpected formats.

**Fix**: Try switching to a different LLM provider. Qwen-Plus and DeepSeek work most reliably.

---

## Frontend Issues

### Blank page at localhost:3000

**Fix**: Make sure backend is also running (`npm run dev` starts both).

### Cannot upload files

Maximum file size is 50MB. Reduce your file size or split it into smaller documents.

---

## Getting More Help

If your issue is not listed here:

1. Check existing [GitHub Issues](../../issues)
2. Open a new issue with your error message and environment details
3. Join [Discord](http://discord.gg/ePf5aPaHnA) for community help
