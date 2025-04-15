from slack_sdk import WebClient
from config import SLACK_BOT_TOKEN, SLACK_CHANNEL

client = WebClient(token=SLACK_BOT_TOKEN)

def send_slack_message(text):
    try:
        response = client.chat_postMessage(channel=SLACK_CHANNEL, text=text)
        print("✅ Sent to Slack:", response["ts"])
    except Exception as e:
        print("Slack Error:", e)
