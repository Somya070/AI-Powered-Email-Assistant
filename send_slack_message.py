import requests
import os
from dotenv import load_dotenv

load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
CHANNEL_ID = os.getenv("SLACK_CHANNEL_ID")

def send_slack_message(text):
    headers = {
        "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "channel": CHANNEL_ID,
        "text": text
    }

    response = requests.post("https://slack.com/api/chat.postMessage", headers=headers, json=data)
    print("Status:", response.status_code)
    print("Response:", response.json())
