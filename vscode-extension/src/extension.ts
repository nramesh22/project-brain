import * as vscode from "vscode";
import fetch from "node-fetch";

export function activate(context: vscode.ExtensionContext) {

  const disposable = vscode.commands.registerCommand(
    "projectBrain.ask",
    async () => {
      const editor = vscode.window.activeTextEditor;
      if (!editor) return;

      const selection = editor.document.getText(editor.selection);

      const prompt = await vscode.window.showInputBox({
        prompt: "What should the AI change in this project?"
      });

      if (!prompt) return;

      const body = {
        query: prompt,
        selected_code: selection,
        file: editor.document.fileName
      };

      const res = await fetch("http://localhost:8000/edit", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body)
      });

      const json = await res.json();
      vscode.window.showInformationMessage("Project Brain applied changes");
    }
  );

  context.subscriptions.push(disposable);
}
