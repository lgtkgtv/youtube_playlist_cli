# ytcli/env.py
import os
import sys
import logging
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# YouTube Data API v3 scope
SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]

# Default client secrets file name
CLIENT_SECRET_FILE = "client_secret.json"


def init_youtube_client(email=None):
    """
    Initializes an authenticated YouTube API client using OAuth 2.0.
    If email is provided, token is saved as token_<email>.json.
    """
    if not os.path.exists(CLIENT_SECRET_FILE):
        print(f"Missing {CLIENT_SECRET_FILE}. Follow instructions in README.md to download it.")
        sys.exit(1)

    if not email:
        print("No email provided. Use --email flag or config.yaml.")
        sys.exit(1)

    token_file = f"token_{email.replace('@', '_at_')}.json"

    creds = None
    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(token_file, "w") as token:
            token.write(creds.to_json())

    from googleapiclient.discovery import build
    youtube = build("youtube", "v3", credentials=creds)
    return youtube

