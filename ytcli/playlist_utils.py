import os
from .export import ensure_user_dir, save_json

def fetch_and_export_playlists(youtube, account):
    playlists = []
    request = youtube.playlists().list(part="snippet,contentDetails", mine=True, maxResults=50)
    while request:
        response = request.execute()
        playlists.extend(response.get("items", []))
        request = youtube.playlists().list_next(request, response)

    folder = ensure_user_dir(account)
    save_json(playlists, f"{folder}/playlists.json")
    os.makedirs(f"{folder}/playlists", exist_ok=True)

    for pl in playlists:
        title = pl["snippet"]["title"].replace("/", "_").replace(" ", "_")
        pl_id = pl["id"]
        videos = []
        req = youtube.playlistItems().list(part="snippet,contentDetails", playlistId=pl_id, maxResults=50)
        while req:
            res = req.execute()
            videos.extend(res.get("items", []))
            req = youtube.playlistItems().list_next(req, res)
        save_json(videos, f"{folder}/playlists/{title}.json")
