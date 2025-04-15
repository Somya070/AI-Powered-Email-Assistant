import requests

def send_to_slack(message, slack_bot_token, channel_id):
    url = "https://slack.com/api/chat.postMessage"
    headers = {
        "Authorization": f"Bearer {slack_bot_token}",
        "Content-Type": "application/json"
    }
    data = {
        "channel":SLACK_CHANNEL,
        "text": message
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 200 or not response.json().get("ok"):
        print("Failed to send message to Slack:", response.text)
    else:
        print("Message sent to Slack successfully!")
