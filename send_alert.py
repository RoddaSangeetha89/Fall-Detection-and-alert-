from twilio.rest import Client

# Your Twilio account SID and auth token
account_sid = 'twilo_account_sid'
auth_token = 'twilo_token'

def send_sms_alert(message):
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_='twilo_number',
        to='receiver_number'
    )

    print(f"SMS sent successfully. SID: {message.sid}")

# Example usage:
message = "Fall detected! Please check immediately."
send_sms_alert(message)


