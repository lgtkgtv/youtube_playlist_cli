## ytcli/cli.py

import json
import csv

from .config import load_config
from .env import init_youtube_client
from .playlist_utils import fetch_playlists, render_markdown_table


def main():
    args = load_config()

    if not hasattr(args, "email") or not args.email:
        print("❌ Missing required --email argument. Please provide it via CLI or config.yaml.")
        return

    yt = init_youtube_client(email=args.email)
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

