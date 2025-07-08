from .export import ensure_user_dir, save_json

def fetch_and_export_subscriptions(youtube, account):
    subscriptions = []
    request = youtube.subscriptions().list(part="snippet", mine=True, maxResults=50)
    while request:
        response = request.execute()
        subscriptions.extend(response.get("items", []))
        request = youtube.subscriptions().list_next(request, response)
    folder = ensure_user_dir(account)
    save_json(subscriptions, f"{folder}/subscriptions.json")
