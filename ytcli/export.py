import os
import json
import glob

def normalize_account_id(account):
    return account.replace("@", "_at_").replace(".", "_dot_")

def ensure_user_dir(account):
    folder = f"data/{normalize_account_id(account)}"
    os.makedirs(folder, exist_ok=True)
    return folder

def save_json(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def list_known_users():
    tokens = glob.glob("tokens/*.json")
    users = [os.path.basename(t).replace(".json", "").replace("_at_", "@").replace("_dot_", ".") for t in tokens]
    if not users:
        print("No authenticated users found.")
        return
    print("📧 Known authenticated users:")
    for u in users:
        print(" -", u)
