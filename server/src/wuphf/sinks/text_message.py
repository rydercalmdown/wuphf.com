import os
from twilio.rest import Client


def build_message(message, sender):
    """Builds a message from the message and sender"""
    return f"WUPHF from {sender}: {message}"


def send_sms(sender, message, phone_number):
    """Makes a phone call to the particular number via twilio"""
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)
    response = client.messages.create(
        body=build_message(message, sender),
        from_=os.environ.get('TWILIO_PHONE_NUMBER'),
        to=phone_number
    )
