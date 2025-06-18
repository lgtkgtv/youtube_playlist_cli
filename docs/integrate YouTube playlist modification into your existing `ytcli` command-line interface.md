#  To integrate YouTube playlist modification into your existing `ytcli` command-line interface (CLI), follow these steps:

---

## ✅ 1. **Add a New CLI Command (`add-video`)**

Update your `ytcli/cli.py` to include a subcommand like `add-video`.

```python
# ytcli/cli.py

import argparse
from ytcli.env import init_youtube_client
from ytcli.playlist_utils import add_video_to_playlist

def main():
    parser = argparse.ArgumentParser(description="YouTube Playlist CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add-video command
    add_video_parser = subparsers.add_parser("add-video", help="Add a video to a playlist")
    add_video_parser.add_argument("--playlist-id", required=True, help="Target playlist ID")
    add_video_parser.add_argument("--video-id", required=True, help="YouTube video ID to add")

    args = parser.parse_args()

    if args.command == "add-video":
        service = init_youtube_client()
        add_video_to_playlist(service, args.playlist_id, args.video_id)
```

---

## ✅ 2. **Add the `add_video_to_playlist` Function**

Create or update `ytcli/playlist_utils.py` with this helper:

```python
# ytcli/playlist_utils.py

def add_video_to_playlist(service, playlist_id, video_id):
    request = service.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": playlist_id,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": video_id
                }
            }
        }
    )
    response = request.execute()
    print(f"✅ Added video {video_id} to playlist {playlist_id}")
```

---

## ✅ 3. **OAuth Client Loader**

Your `ytcli/env.py` should already contain something like:

```python
# ytcli/env.py

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import os

SCOPES = ["https://www.googleapis.com/auth/youtube"]

def init_youtube_client():
    creds = None
    token_path = "token.json"

    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
        creds = flow.run_local_server(port=0)
        with open(token_path, "w") as token:
            token.write(creds.to_json())

    return build("youtube", "v3", credentials=creds)
```

---

## ✅ 4. **Run the CLI**

```bash
uv run ytcli add-video --playlist-id=PLxxxxxx --video-id=dQw4w9WgXcQ
```

---

## 🧪 Next Suggestions

You can follow the same pattern to add commands for:

* `create-playlist`
* `remove-video`
* `list-playlists`
* `rename-playlist`

Let me know if you want these implemented too.


