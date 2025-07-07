# ytcli/playlist_clone.py

from googleapiclient.errors import HttpError
from .playlist_utils import fetch_playlists


def fetch_playlist_videos(youtube, playlist_id):
    videos = []
    request = youtube.playlistItems().list(
        part="snippet,contentDetails",
        playlistId=playlist_id,
        maxResults=50
    )
    while request:
        response = request.execute()
        for item in response.get("items", []):
            videos.append({
                "videoId": item["contentDetails"]["videoId"],
                "title": item["snippet"]["title"]
            })
        request = youtube.playlistItems().list_next(request, response)
    return videos


def remove_duplicates(videos):
    seen = set()
    result = []
    for video in videos:
        if video["videoId"] not in seen:
            seen.add(video["videoId"])
            result.append(video)
    return result


def resolve_playlist_id_by_title(youtube, title):

    DummyArgs = type("Args", (), {
        "filter": None,
        "sort_by_count": False,
        "group_by_privacy": False,
        "no_truncate": False,
        "extended": False,
    })
    playlists = fetch_playlists(youtube, args=DummyArgs())
    for p in playlists:
        if p["title"].strip().lower() == title.strip().lower():
            return p["url"].split("list=")[-1]
    print(f"❌ Playlist with title '{title}' not found.")
    return None


def create_new_playlist(youtube, title, privacy_status="private"):
    response = youtube.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {"title": title, "description": f"Cloned by ytcli"},
            "status": {"privacyStatus": privacy_status}
        }
    ).execute()
    return response["id"]


def add_videos_to_playlist(youtube, playlist_id, videos):
    for video in videos:
        try:
            youtube.playlistItems().insert(
                part="snippet",
                body={
                    "snippet": {
                        "playlistId": playlist_id,
                        "resourceId": {
                            "kind": "youtube#video",
                            "videoId": video["videoId"]
                        }
                    }
                }
            ).execute()
            print(f"✅ Added: {video['title']}")
        except HttpError as e:
            print(f"❌ Failed to add {video['title']}: {e}")

def clone_playlist(youtube, source_title, new_title, remove_original=False):
    print(f"🔍 Resolving playlist titled '{source_title}'...")
    playlist_id = resolve_playlist_id_by_title(youtube, source_title)
    if not playlist_id:
        return

    print("📥 Fetching videos...")
    videos = fetch_playlist_videos(youtube, playlist_id)
    print(f"📦 Fetched {len(videos)} videos.")

    unique_videos = remove_duplicates(videos)
    print(f"🧹 {len(unique_videos)} unique videos after removing duplicates.")

    print(f"📁 Creating new playlist: {new_title}")
    new_playlist_id = create_new_playlist(youtube, new_title)

    print(f"➕ Adding videos to '{new_title}'...")
    add_videos_to_playlist(youtube, new_playlist_id, unique_videos)

    print(f"\n✅ Playlist cloned successfully as '{new_title}' (ID: {new_playlist_id})")

    if remove_original:
        confirm = input(f"⚠️ Are you sure you want to delete the original playlist '{source_title}'? [y/N]: ").strip().lower()
        if confirm == "y":
            print(f"🗑️ Deleting original playlist ID: {playlist_id}")
            youtube.playlists().delete(id=playlist_id).execute()
            print("✅ Original playlist deleted.")
        else:
            print("❌ Deletion cancelled.")

