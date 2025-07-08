# ytcli - Multi-Account YouTube Playlist Manager

## ✅ Features

- Authenticate and manage **multiple YouTube accounts**
- Download:
  - All playlists (with videos)
  - All subscriptions
- Store each user's data under `data/<account>/`
- Reusable tokens in `tokens/<account>.json`
- CLI and Makefile automation

## 🚀 Setup

```bash
make sync
export YTCLI_CLIENT_SECRET=secrets/client_secret.json
make download-all ACCOUNT=you@gmail.com
```

## 🧰 Makefile Commands

- `make sync`: install dependencies
- `make download-all ACCOUNT=...`: download all user data
- `make list-users`: show authenticated users
- `make clean`: remove .venv, tokens, and data

## 📂 Project Structure

```
ytcli/
├── cli.py, auth.py, export.py, playlist_utils.py, subscriptions.py
run.sh
Makefile
secrets/client_secret.json
```

Tokens stored in `tokens/`, data in `data/<account>/`
