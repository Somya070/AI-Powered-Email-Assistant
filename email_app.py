import streamlit as st
from calendar_utils import create_calendar_event
import sqlite3
import datetime

# Streamlit config
st.set_page_config(page_title="AI Email Assistant", layout="wide")
st.title("📧 AI-Powered Email Assistant")

# Connect to database
conn = sqlite3.connect("emails.db")
cursor = conn.cursor()

# Fetch emails with slack status
cursor.execute("SELECT id, subject, body, summary, slack_status FROM emails ORDER BY id DESC LIMIT 10")
emails = cursor.fetchall()

# Show emails with numbers
st.subheader("📬 Latest Emails")
if emails:
    for idx, email in enumerate(emails, 1):  # Numbering emails starting from 1
        email_id, subject, body, summary, slack_status = email

        with st.expander(f"📩 Email {idx}: {subject} (ID: {email_id})"):
            # Email Number
            st.markdown(f"### **Email {idx}**")  # Display email number
            st.markdown(f"**Subject:** {subject}")
            st.markdown(f"**Body:**\n{body}")

            # ✅ Show summary
            if summary and summary.strip().lower() != "summary not available":
                st.success(f"**Summary:** {summary}")
            else:
                st.warning("Summary not available for this email.")

            # 📤 Show Slack status
            if slack_status == "sent":
                st.success("📤 Forwarded to Slack")
            else:
                st.info("📤 Not forwarded to Slack")

            # 📅 Calendar form
            st.subheader(f"📅 Create a Calendar Event for this Email")

            with st.form(f"calendar_form_{email_id}"):
                title = st.text_input("Event Title", value=f"Meeting regarding {subject}")
                description = st.text_area("Event Description", value=f"Discuss email: {subject}")
                date = st.date_input("Event Date")
                time = st.time_input("Event Time")
                location = st.text_input("Location", value="Google Meet")

                submitted = st.form_submit_button("Create Event")

                if submitted:
                    try:
                        start_dt = datetime.datetime.combine(date, time)
                        formatted = start_dt.strftime("%Y-%m-%d %H:%M")

                        # Create calendar event and get event link
                        event_link = create_calendar_event(
                            summary=title,
                            description=description,
                            start_time_str=formatted
                        )

                        # Success message
                        st.success("📅 Event created successfully!")
                        if event_link:
                            st.markdown(f"[🔗 View Event in Google Calendar]({event_link})", unsafe_allow_html=True)
                    except Exception as e:
                        st.error(f"❌ Failed to create event: {e}")
else:
    st.warning("No emails found in the database.")

conn.close()

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit | [GitHub](https://github.com/Somya070/AI-Powered-Email-Assistant)")
