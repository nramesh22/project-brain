Here is a **production-quality `README.md`** for your VS Code extension.

You can copy this directly into `README.md` in the root of your extension.

---

# **Project Brain AI — VS Code Extension**

Project Brain AI is a self-hosted, Cursor-class AI coding assistant for Visual Studio Code.
It allows developers to send selected code and instructions to a private AI backend that analyzes, modifies, and applies changes to the project.

This extension is designed for teams that want **full control over their code, data, and AI models** without relying on third-party SaaS tools.

---

## **Features**

* Send selected code to your private AI server
* Ask the AI to refactor, fix, or enhance project code
* Works directly inside VS Code
* No cloud dependency — runs against your own API
* Supports multi-file and project-aware workflows via backend orchestration

---

## **How It Works**

1. You select code in the editor
2. Run the **Project Brain: Ask AI** command
3. Enter what you want the AI to do
4. The extension sends:

   * Your prompt
   * Selected code
   * File path
     to your backend API
5. Your AI server performs analysis and applies changes
6. VS Code shows confirmation

---

## **Backend Requirement**

This extension requires a running Project Brain server.

Default endpoint used by the extension:

```
POST http://172.18.1.157:8800/edit
```

Expected JSON payload:

```json
{
  "query": "Refactor this function",
  "selected_code": "function foo() { ... }",
  "file": "/path/to/file.ts"
}
```

The backend is responsible for:

* Understanding the request
* Modifying project files
* Applying code changes

---

## **Installation**

### Option 1 — Install from VSIX

```bash
code --install-extension project-brain-1.0.0.vsix
```

Or:

* Open VS Code
* Extensions → `…` → Install from VSIX

---

## **Usage**

1. Open any file
2. Select code
3. Press `Ctrl + Shift + P`
4. Run:

   ```
   Project Brain: Ask AI
   ```
5. Enter what you want the AI to do

Example prompts:

* “Refactor this to async/await”
* “Add error handling”
* “Optimize this loop”
* “Convert this to TypeScript”

---

## **Security Model**

* No code is sent to third-party services
* All data stays within your network
* You control the AI model, embeddings, and storage
* Ideal for enterprise and IP-sensitive environments

---

## **Development Setup**

```bash
npm install
npm run compile
vsce package
```

This produces:

```
project-brain-1.0.0.vsix
```

---

## **Tech Stack**

* VS Code Extension API
* TypeScript
* Native Node.js `fetch()`
* Custom AI orchestration backend

--
