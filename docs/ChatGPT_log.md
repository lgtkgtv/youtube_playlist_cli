## ChatGPT_log.md

# YouTube Playlist CLI

> A Python CLI tool to fetch, format, and export YouTube playlist metadata securely using OAuth.

## Features
- Markdown / JSON / CSV export
- Group by privacy
- Filter by keyword
- OAuth 2.0 Authorization

## Installation

```bash
git clone https://github.com/lgtkgtv/youtube_playlist_cli.git
cd youtube_playlist_cli
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Usage 

```bash 
./run.sh --markdown --group-by-privacy --export-md output.md
```

Or with a config file:
```bash 
./run.sh --config config.yaml
```

## OAuth Setup

Get your `client_secret.json` from `Google Cloud Console`.
Save it in the root directory.
First run will prompt for authorization.

## Source 

A minimal Python CLI tool to list your YouTube playlists using the YouTube Data API.

youtube_playlist_cli/
    ├── README.md                   # User Guide 
    ├── requirements.txt
    ├── config.yaml                 # Optional user config
    ├── run.sh                      # CLI wrapper (calls cli.py)
    ├── .gitignore                  # Handling of secrets... 
    ├── .env                        # YOUTUBE_API_KEY="..." -- Not needed when using oauth2 
    ├── client_secret.json          # Google App Secret - Never commit to github  
    ├── token_<email>.json          # Token cache                 
    └── ytcli
        ├── __init__.py
        ├── env.py                  # Load API key from .env
        ├── config.py               # Utility to parse configurations
        ├── cli.py                  # CLI + YAML config loader
        └── playlist_utils.py


⚠️ **Do not commit `client_secret.json` to version control!**
This file contains OAuth client credentials. Add it to `.gitignore` and protect it with `chmod 600`.

Store it in `~/.config/ytcli/client_secret.json` or use environment variables for added security.

## CLI Flags

| Flag                   | Required | Default         | Description                                                                 |
|------------------------|----------|-----------------|-----------------------------------------------------------------------------|
| `--extended`           | ❌       | `False`         | Include video count column for each playlist                               |
| `--no-truncate`        | ❌       | `False`         | Show full titles and URLs without shortening                                |
| `--group-by-privacy`   | ❌       | `False`         | Group playlists by privacy (public, private, unlisted)                      |
| `--sort-by-count`      | ❌       | `False`         | Sort playlists in descending order by number of videos                      |
|------------------------|----------|-----------------|-----------------------------------------------------------------------------|
| `--filter <term>`      | ❌       | `None`          | Only include playlists with `<term>` in title                              |
|------------------------|----------|-----------------|-----------------------------------------------------------------------------|
| `--markdown`           | ❌       | `False`         | Output playlist data as a Markdown-formatted table                         |
| `--export-md <file>`   | ❌       | `None`          | Write Markdown output to the specified file                                 |
| `--export-json <file>` | ❌       | `None`          | Export playlist data as JSON to the given file                              |
| `--export-csv <file>`  | ❌       | `None`          | Export playlist data as CSV to the given file                               |
|------------------------|----------|-----------------|-----------------------------------------------------------------------------|
| `--config <file>`      | ❌       | `config.yaml`   | Load CLI options from a YAML config file (overridden by CLI flags)          |
| `--email <addr>`       | ✅ (if no token exists) | `None` | Google account email for token storage in `~/.ytcli/<email>/token.json` |
|------------------------|----------|-----------------|-----------------------------------------------------------------------------|

> ℹ️ Notes:
> - If `--email` is not provided and no token exists, authentication will prompt for it.
> - CLI flags override values loaded from the YAML config file.

## Example YAML Config (`config.yaml`)
```yaml
email: "lgtkgtv@gmail.com"   # Optional: if using token directory per email
extended: true
group_by_privacy: true
sort_by_count: false
no_truncate: false
filter: "Python"
markdown: true
export_md: "output.md"
export_json: "output.json"
export_csv: "output.csv"
```
✅ Good Practices:
Booleans (true, false) must be lowercase YAML literals.
Strings should be quoted only when necessary (e.g., paths or terms containing special characters).
If --email is part of your flow (for per-user token storage), include email:.



---
# Using API_KEY Vs OAuth 2.0

### ✅ You're using OAuth 2.0 (via `client_secret.json`)

Your app uses:

```python
from google_auth_oauthlib.flow import InstalledAppFlow
```

and creates a service with:

```python
build("youtube", "v3", credentials=creds)
```

This setup uses **OAuth 2.0 credentials**, not an API key. It allows access to:

* **private playlists**
* user-specific metadata
* read/write operations (depending on scopes)

> This is more powerful and secure than an API key, but it requires interactive authentication and user consent.

---

### ❌ When would an API key be needed?

An API key is used only for **public, unauthenticated access** like:

* listing public playlists
* searching public videos
* accessing public channel data

Example:

```python
youtube = build("youtube", "v3", developerKey=API_KEY)
```

That approach:

* **cannot access** private playlists or modify user data
* is **subject to quota abuse** and shouldn't be used in user-authenticated apps

---
git config --global user.name "lgtkgtv"
git config --global user.email "lgtkgtv@gmail.com"


### 🧾 Summary

| Feature                   | `API_KEY`         | `OAuth (client_secret.json)` |
| ------------------------- | ----------------- | ---------------------------- |
| Access private playlists  | ❌                 | ✅                            |
| Access user account data  | ❌                 | ✅                            |
| Auth via Google login     | ❌                 | ✅                            |
| Safer for multi-user apps | ❌ (no user scope) | ✅                            |
| Quota usage per user      | ❌ (shared)        | ✅ (per user)                 |

---

### ✅ Your current app: No API key needed

Since your CLI tool logs in the user and fetches **user-specific playlists**, you're doing it right with **OAuth only**.

Let me know if you want a fallback mode to use API key *just for public data* — that can be added conditionally.


-------------------------------------------------------------------------------------------------

## pyproject.toml` + Poetry
 

### ✅ Short Answer:

Yes, switching to `pyproject.toml` and Poetry **early** has strong long-term benefits — even if you're not adding tests yet. 
But if you're keeping it very minimal, it’s not *strictly* necessary *right now*.


### ⚖️ Should You Use `pyproject.toml` + Poetry Now?

| Criteria                                                 | Verdict                                                |
| -------------------------------------------------------- | ------------------------------------------------------ |
| You want clean dependency management and reproducibility | ✅ **Poetry is great** for this                         |
| You plan to publish this as a package                    | ✅ Poetry makes publishing to PyPI very easy            |
| You have multiple CLI tools, notebooks, or environments  | ✅ Use Poetry to manage everything consistently         |
| You are building a one-off script or throwaway tool      | ❌ Not required — a `requirements.txt` + `venv` is fine |
| You want to containerize (Docker) or deploy later        | ✅ Poetry works well with CI/CD, Docker, GitHub Actions |

---

### ✅ Benefits of Switching to `pyproject.toml` + Poetry

1. **Modern Standard**: `pyproject.toml` is [PEP 518](https://peps.python.org/pep-0518/)-compliant and will eventually replace `setup.py` and `requirements.txt`.
2. **Dependency Isolation**: Poetry installs dependencies in a project-specific environment (no more `pip freeze > requirements.txt`).
3. **Version Pinning**: Poetry pins exact versions in `poetry.lock`, making builds reproducible.
4. **Script Hooks**: You can define CLI entry points easily in `pyproject.toml`.
5. **Publishing**: Poetry makes it very easy to build and publish Python packages.
6. **No more `setup.py`, `MANIFEST.in`, or `requirements.txt` hassle**.

---

### ❌ When Not to Use Poetry

If:
* Your project is only a couple scripts
* You have no dependencies beyond `google-api-python-client`
* You are **not sharing**, **not packaging**, or **not maintaining** the code long-term

Then `poetry` may be overkill *right now*.

---

### 🔧 Recommendation

Since you’ve already:

* Structured your CLI cleanly
* Want YAML config, GitHub integration, OAuth
* Asked about testing and CI in future

You're clearly **not making a throwaway tool**. 
So **yes**, I’d recommend switching to Poetry and `pyproject.toml` now — it’s clean, modern, and makes future growth (tests, releases, CI) easier.

Would you like me to scaffold a `pyproject.toml` + `poetry` setup for this CLI now?


