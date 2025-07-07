# ytcli

---

CLI tool to manage YouTube playlists.

---

## ✅ Setup Instructions Using `uv`

```bash
uv init                      # Initialize uv-based virtual environment (.venv/)
uv sync                      # Install all dependencies
source .venv/bin/activate    # (optional) Activate the virtual environment

# Run the tool using uv
uv run ./run.sh --email="you@example.com"

# Optional: override the path to your client_secret.json
export YTCLI_CLIENT_SECRET=secrets/client_secret.json
```

---

## 🔐 OAuth Setup: How to Create `client_secret.json`

1. Visit [Google Cloud Console](https://console.cloud.google.com/).
2. Create or select a project.
3. Go to **APIs & Services > Library** and enable **YouTube Data API v3**.
4. Go to **APIs & Services > Credentials**:

   * Click **+ Create Credentials > OAuth client ID**
   * Choose **Desktop App**
   * Name it (e.g., `ytcli Desktop App`)
5. Configure the OAuth consent screen if prompted.
6. Click **Download JSON** after creating credentials.
7. Save and rename it to `client_secret.json`. Place it in your project root **or** set its location using:

   ```bash
   export YTCLI_CLIENT_SECRET=path/to/client_secret.json
   ```
8. ⚠️ **Do NOT check this file into git** — it contains sensitive credentials.

---

## 🎯 Project Structure

```
├── README.md                      # Usage & setup instructions
├── run.sh                         # Entry-point script
├── requirements.txt               # Dependencies
├── pyproject.toml                 # Project metadata
├── config.yaml                    # CLI default settings
├── ytcli/                         # Source code package
│   ├── cli.py                     # CLI entry point logic
│   ├── config.py                  # Config parsing
│   ├── env.py                     # OAuth setup
│   ├── playlist_utils.py          # Business logic (YouTube API)
```

---

## 🚀 Features

* Authenticate via OAuth 2.0 (`client_secret.json`)
* List user playlists (via YouTube Data API v3)
* Filter, sort, and group playlists
* Export to CSV, JSON, Markdown

---

## 🧪 Example Usage

```bash
# Default usage:
uv run ./run.sh --email="you@gmail.com"

# With Markdown table and export
uv run ./run.sh --email="you@gmail.com" --markdown --export-md=playlists.md

# Filtered and sorted
uv run ./run.sh --email="you@gmail.com" --filter=music --sort-by-count
```

---

## 🛠️ Troubleshooting

* If the CLI runs but shows no output:

  * Ensure your YouTube account has playlists
  * Try adding `--markdown` or `--export-json`
  * Confirm you’ve authenticated successfully (browser popup)

---

## ✅ .gitignore Reminder

Ensure your `.gitignore` includes:

```gitignore
client_secret.json
token_*.json
secrets/
.venv/
*.csv
*.json
*.md
```

## ✅ Milestone 1: GitHub Check-In Guide

### 📦 What's Ready

* OAuth-enabled YouTube playlist CLI tool
* Clean `README.md` with setup and usage docs
* `uv`-based virtual environment workflow
* Secure `client_secret.json` handling
* Export to Markdown, JSON, CSV
* Smart CLI flags and config via YAML

## 🚧 Milestone 2 Roadmap (Planned Features)

*
