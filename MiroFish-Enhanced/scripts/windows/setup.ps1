# MiroFish Enhanced - Windows Setup Script
# Run this in PowerShell as Administrator
# Usage: .\scripts\windows\setup.ps1

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  MiroFish Enhanced - Windows Setup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check Node.js
Write-Host "Checking Node.js..." -ForegroundColor Yellow
try {
    $nodeVersion = node -v 2>&1
    Write-Host "  Node.js found: $nodeVersion" -ForegroundColor Green
} catch {
    Write-Host "  ERROR: Node.js not found!" -ForegroundColor Red
    Write-Host "  Please install Node.js 18+ from: https://nodejs.org" -ForegroundColor Red
    exit 1
}

# Check Python
Write-Host "Checking Python..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "  Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "  ERROR: Python not found!" -ForegroundColor Red
    Write-Host "  Please install Python 3.11+ from: https://python.org" -ForegroundColor Red
    exit 1
}

# Check uv
Write-Host "Checking uv package manager..." -ForegroundColor Yellow
try {
    $uvVersion = uv --version 2>&1
    Write-Host "  uv found: $uvVersion" -ForegroundColor Green
} catch {
    Write-Host "  uv not found. Installing uv..." -ForegroundColor Yellow
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    Write-Host "  uv installed successfully!" -ForegroundColor Green
}

# Setup .env file
Write-Host ""
Write-Host "Setting up environment file..." -ForegroundColor Yellow
if (-not (Test-Path ".env")) {
    Copy-Item ".env.example" ".env"
    Write-Host "  .env file created from .env.example" -ForegroundColor Green
    Write-Host "  IMPORTANT: Edit .env with your API keys before starting!" -ForegroundColor Red
} else {
    Write-Host "  .env file already exists, skipping" -ForegroundColor Green
}

# Install Node dependencies
Write-Host ""
Write-Host "Installing Node.js dependencies..." -ForegroundColor Yellow
npm install
if ($LASTEXITCODE -ne 0) {
    Write-Host "  ERROR: npm install failed!" -ForegroundColor Red
    exit 1
}
Write-Host "  Node.js dependencies installed!" -ForegroundColor Green

# Install frontend dependencies
Write-Host ""
Write-Host "Installing frontend dependencies..." -ForegroundColor Yellow
Set-Location frontend
npm install
if ($LASTEXITCODE -ne 0) {
    Write-Host "  ERROR: frontend npm install failed!" -ForegroundColor Red
    Set-Location ..
    exit 1
}
Set-Location ..
Write-Host "  Frontend dependencies installed!" -ForegroundColor Green

# Install Python backend dependencies
Write-Host ""
Write-Host "Installing Python backend dependencies..." -ForegroundColor Yellow
Set-Location backend
uv venv
uv pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) {
    Write-Host "  ERROR: Python dependencies install failed!" -ForegroundColor Red
    Set-Location ..
    exit 1
}
Set-Location ..
Write-Host "  Python backend dependencies installed!" -ForegroundColor Green

# Done
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Setup Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "  1. Edit .env file with your API keys" -ForegroundColor White
Write-Host "     - LLM_API_KEY (get from groq.com for free)" -ForegroundColor White
Write-Host "     - ZEP_API_KEY (get from app.getzep.com for free)" -ForegroundColor White
Write-Host ""
Write-Host "  2. Start the application:" -ForegroundColor White
Write-Host "     npm run dev" -ForegroundColor Cyan
Write-Host ""
Write-Host "  3. Open in browser:" -ForegroundColor White
Write-Host "     http://localhost:3000" -ForegroundColor Cyan
Write-Host ""
