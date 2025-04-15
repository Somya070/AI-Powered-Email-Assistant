import requests
import os
from dotenv import load_dotenv

load_dotenv()

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def send_to_slack(message):
    payload = {"text": message}
    response = requests.post(SLACK_WEBHOOK_URL, json=payload)

    if response.status_code != 200:
        print("❌ Slack Error:", response.status_code, response.text)
        return False
    print("✅ Sent to Slack")
    return True

# 🔁 Test Message
send_to_slack("🚀 Test message from Somya's AI Email Assistant!")
