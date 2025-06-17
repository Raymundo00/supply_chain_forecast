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
