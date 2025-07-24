# ytcli - Multi-Account YouTube Playlist Manager

## YT API ref
```
https://developers.google.com/youtube/v3/quickstart/python
    https://developers.google.com/youtube/v3/docs/channels
    https://developers.google.com/youtube/v3/docs/playlists
    https://developers.google.com/youtube/v3/docs/playlistItems
    https://developers.google.com/youtube/v3/docs/videos
    https://developers.google.com/youtube/v3/docs/subscriptions
    https://developers.google.com/youtube/v3/docs/search
    https://developers.google.com/youtube/v3/docs/comments
    https://developers.google.com/youtube/v3/docs/activities

YouTube Data API PyDoc documentation      
    https://developers.google.com/resources/api-libraries/documentation/youtube/v3/python/latest/

YouTube Data API reference documentation 
    https://developers.google.com/youtube/v3/docs

GitRepo
    https://github.com/youtube/api-samples
```

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
