# ytcli/env.py
import os
import sys
import json
import logging
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# YouTube Data API v3 scope
# SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]
SCOPES = ["https://www.googleapis.com/auth/youtube"]


# Default path from env or fallback
def get_valid_client_secret():
    path = os.getenv("YTCLI_CLIENT_SECRET", "client_secret.json")

    while True:
        if os.path.exists(path):
            try:
                with open(path, "r") as f:
                    json.load(f)
                return path
            except Exception as e:
                print(f"❌ File found but is not valid JSON: {e}")
        else:
            print(f"❌ File not found at: {path}")

        # Prompt user to enter a new path
        path = input("🔐 Enter path to a valid client_secret.json: ").strip()
        if not path:
            print("Aborted: no path provided.")
            sys.exit(1)

def init_youtube_client(email=None):
    """
    Initializes an authenticated YouTube API client using OAuth 2.0.
    If email is provided, token is saved as token_<email>.json.
    """
    client_secret_path = get_valid_client_secret()

    if not email:
        print("❌ No email provided. Use --email flag or config.yaml.")
        sys.exit(1)

    token_file = f"token_{email.replace('@', '_at_')}.json"

    creds = None
    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(client_secret_path, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(token_file, "w") as token:
            token.write(creds.to_json())

    from googleapiclient.discovery import build
    youtube = build("youtube", "v3", credentials=creds)
    return youtube
