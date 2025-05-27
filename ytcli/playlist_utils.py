## ytcli/playlist_utils.py

def fetch_playlists(youtube, args):
    request = youtube.playlists().list(part="snippet,contentDetails", mine=True, maxResults=50)
    response = request.execute()

    playlists = []
    for item in response.get("items", []):
        title = item["snippet"]["title"]
        url = f"https://www.youtube.com/playlist?list={item['id']}"
        count = item["contentDetails"].get("itemCount", 0)
        privacy = item["status"].get("privacyStatus", "unknown") if "status" in item else "unknown"
        playlists.append({"title": title, "url": url, "count": count, "privacy": privacy})

    if args.filter:
        playlists = [p for p in playlists if args.filter.lower() in p["title"].lower()]
    if args.sort_by_count:
        playlists.sort(key=lambda x: x["count"], reverse=True)
    else:
        playlists.sort(key=lambda x: x["title"].lower())

    return playlists


def truncate(text, max_len):
    return text if len(text) <= max_len else text[:max_len - 3] + "..."


def render_markdown_table(playlists, args):
    from collections import defaultdict

    grouped = defaultdict(list)
    for p in playlists:
        key = p["privacy"] if args.group_by_privacy else "All"
        grouped[key].append(p)

    output = []
    for group, items in grouped.items():
        output.append(f"\n### Privacy: {group}\n")
        headers = ["Title", "Video Count", "URL"] if args.extended else ["Title", "URL"]
        rows = []

        for p in items:
            title = p["title"]
            url = p["url"]
            if not args.no_truncate:
                title = truncate(title, 40)
                url = truncate(url, 45)
            row = [title, str(p["count"]), url] if args.extended else [title, url]
            rows.append(row)

        col_widths = [max(len(row[i]) for row in [headers] + rows) for i in range(len(headers))]
        fmt_row = lambda r: "| " + " | ".join(r[i].ljust(col_widths[i]) for i in range(len(r))) + " |"
        sep = "|" + "|".join("-" * (w + 2) for w in col_widths) + "|"

        output.append(fmt_row(headers))
        output.append(sep)
        output.extend([fmt_row(row) for row in rows])

    return "\n".join(output)
