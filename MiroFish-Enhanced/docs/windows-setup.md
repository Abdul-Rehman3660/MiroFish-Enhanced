# Windows Setup Guide

This guide walks you through setting up MiroFish Enhanced on Windows step by step.

---

## Prerequisites

### Step 1 — Install Node.js

1. Go to [nodejs.org](https://nodejs.org)
2. Download the **LTS version** (18 or higher)
3. Run the installer, accept all defaults
4. Verify: open Command Prompt and run `node -v`

### Step 2 — Install Python

1. Go to [python.org/downloads](https://python.org/downloads)
2. Download Python **3.11** or **3.12** (not 3.13 — not yet compatible)
3. Run the installer
4. **IMPORTANT**: Check the box "Add Python to PATH" during installation
5. Verify: open Command Prompt and run `python --version`

### Step 3 — Install Git

1. Go to [git-scm.com](https://git-scm.com)
2. Download and install Git for Windows
3. Accept all defaults during installation

---

## Installation

### Option A — Automatic (Recommended)

Open **PowerShell as Administrator** and run:

```powershell
git clone https://github.com/YOUR_USERNAME/MiroFish-Enhanced.git
cd MiroFish-Enhanced
.\scripts\windows\setup.ps1
```

If you see a security error, first run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try the setup script again.

### Option B — Manual

Open Command Prompt or PowerShell:

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/MiroFish-Enhanced.git
cd MiroFish-Enhanced

# Install uv (Python package manager)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Copy environment file
copy .env.example .env

# Install Node dependencies
npm install

# Install frontend dependencies
cd frontend
npm install
cd ..

# Install Python dependencies
cd backend
uv venv
uv pip install -r requirements.txt
cd ..
```

---

## Configure API Keys

Edit the `.env` file (use Notepad or VS Code):

```
notepad .env
```

Fill in your API keys. For the cheapest option, use Groq (free tier):

1. Go to [console.groq.com](https://console.groq.com)
2. Sign up for a free account
3. Create an API key
4. Paste it as `LLM_API_KEY`
5. Set `LLM_BASE_URL=https://api.groq.com/openai/v1`
6. Set `LLM_MODEL_NAME=llama-3.3-70b-versatile`

For Zep (agent memory):

1. Go to [app.getzep.com](https://app.getzep.com)
2. Sign up for a free account
3. Create an API key
4. Paste it as `ZEP_API_KEY`

---

## Start MiroFish

```bash
npm run dev
```

Open your browser at **http://localhost:3000**

---

## Common Windows Problems

### "npm is not recognized"

Node.js was not added to PATH. Reinstall Node.js and make sure to check "Add to PATH" during setup.

### "python is not recognized"

Python was not added to PATH. Reinstall Python and check "Add Python to PATH".

### "uv is not recognized" after installation

Close your terminal and open a new one. The PATH update requires a new session.

### Port 3000 or 5001 already in use

Find and stop the process using that port:

```powershell
netstat -ano | findstr :3000
taskkill /PID <PID_NUMBER> /F
```

### Backend fails to start

Make sure you are in the project root (not inside the backend folder) when running `npm run dev`.

---

## Still having trouble?

Open an issue on GitHub with your error message and we will help.
