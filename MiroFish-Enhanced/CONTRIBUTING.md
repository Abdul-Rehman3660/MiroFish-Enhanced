# Contributing to MiroFish Enhanced

Thank you for your interest in contributing! Every contribution — big or small — is valued.

## Ways to Contribute

### For Non-Developers
- **Report bugs** — open a GitHub Issue with details
- **Improve documentation** — fix typos, add examples, clarify instructions
- **Add translations** — translate docs to your language
- **Share your experience** — tell us what worked and what did not

### For Developers
- **Fix bugs** — pick an issue labeled `good first issue`
- **Add features** — discuss first in Issues before building
- **Improve tests** — add or fix test coverage
- **Optimize performance** — reduce API token usage

---

## Getting Started

### 1. Fork the repo

Go to [github.com/YOUR_USERNAME/MiroFish-Enhanced](https://github.com) and click Fork.

### 2. Clone your fork

```bash
git clone https://github.com/YOUR_USERNAME/MiroFish-Enhanced.git
cd MiroFish-Enhanced
```

### 3. Create a branch

```bash
git checkout -b fix/bug-description
# or
git checkout -b feature/new-feature-name
```

### 4. Make your changes

Follow the code style you see in existing files.

### 5. Test your changes

```bash
# Start the dev server
npm run dev

# Test your changes at http://localhost:3000
```

### 6. Commit and push

```bash
git add .
git commit -m "fix: describe what you fixed"
git push origin fix/bug-description
```

### 7. Open a Pull Request

Go to your fork on GitHub and click "Compare & pull request".

---

## Commit Message Format

Use clear commit messages:

```
type: short description

Examples:
fix: correct environment variable loading on Windows
feat: add Groq provider configuration example
docs: translate README to Urdu
refactor: simplify cost estimator logic
```

Types: `fix`, `feat`, `docs`, `refactor`, `test`, `chore`

---

## What We Need Most Right Now

These are the highest-priority contributions:

1. **Windows testing** — test the setup script on real Windows machines
2. **Documentation improvements** — expand troubleshooting section
3. **Free LLM testing** — test with Groq and Gemini Flash and report results
4. **Bug reports** — find and report installation issues
5. **Translations** — Urdu, Hindi, Arabic, Spanish README translations

---

## Code of Conduct

Be respectful. We are building something cool together. Treat others how you want to be treated.

---

## Questions?

Open a GitHub Issue or join the Discord: [discord.gg/ePf5aPaHnA](http://discord.gg/ePf5aPaHnA)
