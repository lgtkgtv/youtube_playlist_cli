## ytcli/cli.py

import argparse
import sys
import json
import csv

from .env import init_youtube_client
from .playlist_utils import fetch_playlists, render_markdown_table
from .playlist_clone import clone_playlist


def main():
    parser = argparse.ArgumentParser(description="YouTube Playlist CLI")

    # Authentication
    parser.add_argument("--email", required=True, help="Google account email to authenticate")

    # Clone logic
    parser.add_argument("--clone-playlist", type=str, help="Playlist title to clone")
    parser.add_argument("--new-title", type=str, help="New title for cloned playlist")

    # Display and export
    parser.add_argument("--extended", action="store_true")
    parser.add_argument("--markdown", action="store_true")
    parser.add_argument("--no-truncate", action="store_true")
    parser.add_argument("--group-by-privacy", action="store_true")
    parser.add_argument("--sort-by-count", action="store_true")
    parser.add_argument("--filter", type=str, default=None)
    parser.add_argument("--export-md", type=str, default=None)
    parser.add_argument("--export-json", type=str, default=None)
    parser.add_argument("--export-csv", type=str, default=None)
    parser.add_argument("--remove-original", action="store_true", help="Delete the original playlist after cloning")

    args = parser.parse_args()

    yt = init_youtube_client(email=args.email)

    if args.clone_playlist:
        if not args.new_title:
            print("❌ --new-title is required when using --clone-playlist")
            sys.exit(1)
        # clone_playlist(youtube=yt, source_title=args.clone_playlist, new_title=args.new_title)
        clone_playlist(
            youtube=yt,
            source_title=args.clone_playlist,
            new_title=args.new_title,
            remove_original=args.remove_original,
        )
        
        return

    playlists = fetch_playlists(yt, args)

    if args.markdown:
        output = render_markdown_table(playlists, args)
        print(output)
        if args.export_md:
            with open(args.export_md, "w", encoding="utf-8") as f:
                f.write(output)
    else:
        for p in playlists:
            print(f"{p['title']} ({p['count']}): {p['url']}")

    if args.export_json:
        with open(args.export_json, "w", encoding="utf-8") as f:
            json.dump(playlists, f, indent=2)

    if args.export_csv:
        with open(args.export_csv, "w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["title", "url", "count", "privacy"])
            writer.writeheader()
            writer.writerows(playlists)


if __name__ == '__main__':
    main()

