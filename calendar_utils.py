from __future__ import print_function
import datetime
import os.path
import pytz
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request


# If modifying these SCOPES, delete the token.json file.
SCOPES = ['https://www.googleapis.com/auth/calendar.events']


def create_calendar_event(start_time_str, title, description, location, duration_minutes=30):
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    # ⏰ Format start and end time
    start_time = datetime.datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
    end_time = start_time + datetime.timedelta(minutes=duration_minutes)

    event = {
        'summary': title,
        'description': description,
        'location': location,
        'start': {
            'dateTime': start_time.isoformat(),
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': end_time.isoformat(),
            'timeZone': 'Asia/Kolkata',
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('📅 Calendar event created:', event.get('htmlLink'))
