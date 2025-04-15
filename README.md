# AI-Powered-Email-Assistant

An AI-enhanced assistant that connects with your Gmail inbox, summarizes emails using a language model, forwards messages to Slack, and helps schedule meetings directly into Google Calendar — all from a sleek Streamlit dashboard.

Made with ❤ by [Somya Anand](https://github.com/Somya070)

---

## 🌟 Features

✅ Summarizes recent emails using AI  
✅ Shows summaries and Slack forwarding status in a user-friendly UI  
✅ Lets you create Google Calendar events for specific emails  
✅ Beautiful UI with Streamlit, cleanly displays your latest 10 emails  
✅ Stores emails locally in SQLite

---

## 🛠 Tech Stack

- Python
- Streamlit
- SQLite
- Google APIs (Gmail + Calendar)
- OpenAI/Gemini API (for summaries)
- Slack Webhooks / Bot Token
- dotenv (.env) for secret management

---

## ⚙ Setup Instructions

### 1. *Clone the Repo*

git clone https://github.com/your-username/Email-Assistant.git
cd Email-Assistant

### 2. Create Virtual Environment (Optional but Recommended)

python -m venv venv

### 3. Install Dependencies

-streamlit
-openai
-google-auth
-google-auth-oauthlib
-google-api-python-client
-requests
-python-dotenv
-dateparser

### 4. Environment Setup
Create a .env file in the root folder:

* SLACK_WEBHOOK_URL=your_webhook_or_bot_url
* SLACK_BOT_TOKEN=your_slack_bot_token
* CHANNEL_ID=your_channel_id
* OPENAI_API_KEY=your_openai_key_or_gemini

### 5. Google API Setup
Required for Gmail & Calendar integration

🔹 Step 1: Create a project on Google Cloud Console
Enable:
    - Gmail API
    - Calendar API

🔹 Step 2: Download credentials.json
Place it in the root folder (not shared on GitHub).

🔹 Step 3: Authorize your app
First time you run Gmail/Calendar functions, a browser window will open for login. It will create token.json.

### 6. Run the App

- streamlit run app.py
- App will launch at http://localhost:8501


📬 Contact
For questions, reach out to me on Instagram(@_.somya_77) or raise an issue on GitHub.
