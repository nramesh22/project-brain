
# ProjectBrain

ProjectBrain is a self-hosted **Cursor-class AI coding assistant**.  
It understands your **entire codebase** and applies **multi-file, git-safe changes** using LLMs.

---

## Features

- Project-wide semantic search
- Symbol-level dependency graph
- Multi-file AI refactoring
- Git-diff based safe edits
- Test-aware validation loop
- VS Code integration
- File and folder creation

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-org/projectbrain
cd projectbrain
````

### 2. Copy Environment

```bash
cp .env.example .env
```

### 3. Start Services

```bash
docker-compose up --build
```

---

## Import Your Project

Copy your project into `projectbrain/repos/`:

```
projectbrain/repos/my-api
```

Then index it:

```bash
curl -X POST http://localhost:8000/index \
  -H "Content-Type: application/json" \
  -d '{"path":"/repos/my-api"}'
```

---

## Use VS Code Extension

1. Open VS Code
2. Install the ProjectBrain extension (from `vscode-extension` folder)
3. Open your project in VS Code
4. Select code or place cursor
5. Press `Ctrl+Shift+P` → `Project Brain: Ask AI`
6. Type your request:

```
Add JWT authentication to login API
```

AI will:

* Analyze project graph
* Update multiple files
* Create new files/folders if needed
* Apply changes via git diffs

---

## Stay in Control

Use standard git commands to review:

```bash
git status
git diff
git checkout .
git revert <commit>
```

---

## License

MIT License