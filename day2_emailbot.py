import smtplib
import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config
def send_email(receiver, subject, body):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(config.SENDER_EMAIL, config.APP_PASSWORD)
        
        msg = MIMEMultipart()
        msg["From"] = config.SENDER_EMAIL
        msg["To"] = receiver
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))
        
        server.sendmail(config.SENDER_EMAIL, receiver, msg.as_string())
        server.quit()
        print("✅ Email sent successfully!")

    except Exception as e:
        print(f"❌ Something went wrong: {e}")

reminders = [
    {"time": "08:00", "subject": "Good Morning!", "body": "Start your day. Open your Python project."},
    {"time": "14:00", "subject": "Afternoon Check-in", "body": "Have you coded today? Even 30 mins counts."},
    {"time": "22:00", "subject": "Wind Down", "body": "Great work today. Rest well, build tomorrow."},
]

def schedule_reminders():
    for reminder in reminders:
        schedule.every().day.at(reminder["time"]).do(
            send_email,
            receiver=config.RECEIVER_EMAIL,
            subject=reminder["subject"],
            body=reminder["body"]
        )
        print(f"📅 Scheduled: {reminder['subject']} at {reminder['time']}")

if __name__ == "__main__":
    print("🤖 WhileIRest bot is running...\n")
    schedule_reminders()
    
    while True:
        schedule.run_pending()
        time.sleep(60)