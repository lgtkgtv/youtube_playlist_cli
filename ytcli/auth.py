import os
import sys
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]
CLIENT_SECRET_FILE = os.getenv("YTCLI_CLIENT_SECRET", "client_secret.json")

def normalize_account_id(account):
    return account.replace("@", "_at_").replace(".", "_dot_")

def get_authenticated_youtube(account):
    os.makedirs("tokens", exist_ok=True)
    norm = normalize_account_id(account)
    token_file = os.path.join("tokens", f"{norm}.json")
    creds = None
    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CLIENT_SECRET_FILE):
                print("Missing client_secret.json")
                sys.exit(1)
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(token_file, "w") as token:
            token.write(creds.to_json())
    return build("youtube", "v3", credentials=creds)
