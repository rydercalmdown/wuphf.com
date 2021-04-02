import os
from twilio.rest import Client


def build_message(message, sender):
    """Builds a twiml message from the message and sender"""
    speak = f"Hello, you have a new Woof from {sender}. {message}"
    return f"<Response><Say>{speak}</Say></Response>"


def call(sender, message, phone_number):
    """Makes a phone call to the particular number via twilio"""
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)
    message = build_message(message, sender)
    call = client.calls.create(
        twiml=message,
        to=phone_number,
        from_=os.environ.get('TWILIO_PHONE_NUMBER')
    )
