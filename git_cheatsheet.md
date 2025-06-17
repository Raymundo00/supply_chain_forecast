# Git Cheatsheet – Supply Chain Forecast Project

This file contains the most common Git commands used during the setup and development of this project. Use it as a quick reference guide.

---

## 🔧 Initialization & Configuration

| Command | Description |
|--------|-------------|
| `git init` | Initialize Git in the project folder. |
| `git config --global user.name "Your Name"` | Set your Git username globally. |
| `git config --global user.email "your@email.com"` | Set your Git email globally. |

---

## 📁 Working with Files

| Command | Description |
|--------|-------------|
| `git status` | Check the status of your files. |
| `git add filename` | Add a specific file to staging (ready to commit). |
| `git add .` | Add all new/modified files to staging. |
| `git commit -m "your message"` | Save a snapshot of your staged files. |

---

## 🔍 History

| Command | Description |
|--------|-------------|
| `git log --oneline` | Show commit history (one line per commit). |

---

## ☁️ Connecting to GitHub

| Command | Description |
|--------|-------------|
| `git remote add origin https://github.com/YOUR-USER/project.git` | Link local repo to GitHub. |
| `git remote -v` | Check remote connection. |
| `git push -u origin main` | Push local commits to GitHub (first time). |
| `git push` | Push new commits to GitHub. |
| `git branch -M main` | Rename branch to main (if needed). |
| `git remote remove origin` | Remove the current remote if it's incorrect. |

---

## 📝 File Creation from Terminal

| Command | Description |
|--------|-------------|
| `echo "# Project Title" > README.md` | Create a file and add content. |
| `ls` | List files in the current directory. |

---

## ✅ Tip

Make regular commits with clear messages to track your progress and changes properly.


---

## 🖥️ Opening VS Code from Git Bash

| Command | Description |
|---------|-------------|
| `code .` | Opens the current folder in Visual Studio Code. Make sure `code` is installed in PATH. |

> To enable the `code` command:
> - Open VS Code  
> - Press `Ctrl + Shift + P`  
> - Search for: `Shell Command: Install 'code' command in PATH`  
> - Press Enter, then restart Git Bash


## 📝 Extra Notes

### 📁 Why `.gitignore` is not ignored

Even though the file is called `.gitignore`, **it is not ignored by Git**.

Git uses it to know what other files or folders to ignore, such as:

- `.env` → environment/credential files
- `data/` → raw data files (like CSVs or Excel)
- `__pycache__/` → temporary Python files

You should **track `.gitignore` with Git** like any other config file:

```bash
git add .gitignore
git commit -m "Add or update .gitignore"
git push
