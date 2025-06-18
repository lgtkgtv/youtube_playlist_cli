# script to generate OAuth2 **access** and **refresh** tokens

Here is a **complete and ready-to-run Python script** to generate OAuth2 **access** and **refresh** tokens for the **YouTube Data API** using your `client_secret.json`:

---

### ✅ Step-by-step Instructions

#### 1. 📁 Make sure you have this file:

* `client_secret.json` downloaded from Google Cloud Console (see previous steps).

#### 2. 🐍 Create `generate_tokens.py` with the following code:

```python
# generate_tokens.py

from google_auth_oauthlib.flow import InstalledAppFlow
import json

# Define the scopes your app needs
SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
    
    # Launches a local server and opens a browser for user to authenticate
    creds = flow.run_local_server(port=0)

    # Save the credentials to token.json
    with open("token.json", "w") as token_file:
        token_file.write(creds.to_json())
    
    print("\n✅ Token saved to 'token.json'")
    print("Access Token:", creds.token)
    print("Refresh Token:", creds.refresh_token)

if __name__ == "__main__":
    main()
```

---

#### 3. 📦 Install required packages (use `uv` or `pip`):

If you're using `uv`:

```bash
uv pip install google-auth google-auth-oauthlib
```

Or with `pip`:

```bash
pip install google-auth google-auth-oauthlib
```

---

#### 4. ▶️ Run the script:

```bash
python generate_tokens.py
```

It will:

* Open your browser to authenticate with Google.
* Ask for permission to access YouTube on your behalf.
* Save the resulting tokens into `token.json`.

---

### 🔐 What's in `token.json`?

It contains:

* `access_token` (expires after \~1 hour)
* `refresh_token` (used to get new access tokens)
* `client_id`, `client_secret`, scopes, expiry, etc.

You can now use this file in your CLI app for authenticated YouTube API access.

---

To **modify YouTube playlists programmatically**, you'll need to use the **YouTube Data API v3** with **OAuth2 authentication**. Here’s what you need to do:

---

## ✅ 1. Enable Required Scopes

To **modify playlists** (create, delete, reorder, update), you need **write access**, not just read-only.

Update your Python script to use this scope:

```python
SCOPES = ["https://www.googleapis.com/auth/youtube"]
```

This grants **full read/write access** to YouTube account content (playlists, videos, etc.).

---

## ✅ 2. Regenerate `token.json`

1. Delete any old `token.json` generated with read-only scope.
2. Update the `SCOPES` in your `generate_tokens.py` script.
3. Re-run the script:

```bash
python generate_tokens.py
```

This will prompt Google login again and ask for the new permissions.

---

## ✅ 3. Use the API to Modify Playlists

After authentication, use the `googleapiclient.discovery.build` to call YouTube API endpoints.

### Example: Add a video to a playlist

```python
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import json

# Load saved token
creds = Credentials.from_authorized_user_file("token.json", ["https://www.googleapis.com/auth/youtube"])

# Build the API client
youtube = build("youtube", "v3", credentials=creds)

# Add a video to a playlist
request = youtube.playlistItems().insert(
    part="snippet",
    body={
        "snippet": {
            "playlistId": "YOUR_PLAYLIST_ID",
            "resourceId": {
                "kind": "youtube#video",
                "videoId": "VIDEO_ID_TO_ADD"
            }
        }
    }
)
response = request.execute()
print("✅ Video added:", response["id"])
```

---

## 🧰 What You Can Do

You can use the following API methods:

| Operation                | Method                             |
| ------------------------ | ---------------------------------- |
| Create playlist          | `youtube.playlists().insert()`     |
| List your playlists      | `youtube.playlists().list()`       |
| Add video to playlist    | `youtube.playlistItems().insert()` |
| Remove video from list   | `youtube.playlistItems().delete()` |
| Reorder playlist items   | `youtube.playlistItems().update()` |
| Update playlist metadata | `youtube.playlists().update()`     |

---

## 🚨 Notes

* Playlist ID: Format like `PLxxxxxxxxxxxxxxxxx`
* Video ID: Standard 11-char YouTube video ID (e.g., `dQw4w9WgXcQ`)
* You must own the playlist to modify it.
* Write operations need full `youtube` scope.

---

Would you like a ready-made CLI function to:

* List playlists
* Add/remove videos
* Create/delete playlists?

Let me know how you'd like to proceed.




