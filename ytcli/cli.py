import argparse
from .auth import get_authenticated_youtube
from .playlist_utils import fetch_and_export_playlists
from .subscriptions import fetch_and_export_subscriptions
from .export import list_known_users

def main():
    parser = argparse.ArgumentParser(description="YouTube CLI - Multi-account Playlist Manager")
    parser.add_argument("--account", type=str, help="Unique account identifier (e.g., email)", required=True)
    parser.add_argument("--download-all", action="store_true", help="Download playlists + subscriptions for account")
    parser.add_argument("--list-users", action="store_true", help="List all authenticated accounts")
    args = parser.parse_args()

    if args.list_users:
        list_known_users()
        return

    yt = get_authenticated_youtube(args.account)

    if args.download_all:
        fetch_and_export_playlists(yt, args.account)
        fetch_and_export_subscriptions(yt, args.account)
        print(f"✅ All data saved to data/{args.account.replace('@', '_at_').replace('.', '_dot_')}/")

if __name__ == "__main__":
    main()
