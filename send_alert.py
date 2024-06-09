import smtplib
from email.message import EmailMessage

def send_email_alert(subject, message):
    # Replace with your email settings
    sender_email = "senders_mail.com"
    receiver_email = "receivers_mail.com"
    password = "uysc hqsg zhmf tnf"

    try:
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login(sender_email, password)
        msg = f"Subject: {subject}\n\n{message}"
        server.sendmail(sender_email, receiver_email, msg)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}")
          # Replace with your fall detection logic
    subject = "Fall Detected"
    message = "A fall has been detected. Please check the system."
    send_alert_email(subject, message)
