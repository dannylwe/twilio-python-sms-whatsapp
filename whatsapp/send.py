# $0.0576 / UGX 211.99 per

from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

account_sid = os.getenv("account_sid")
auth_token  = os.getenv("auth_token")
client = Client(account_sid, auth_token)

from_number = "whatsapp:" + os.getenv("sandbox")

message = client.messages.create(
    from_ = from_number,
    body = 'Success - Test!',
    to = 'whatsapp:+256772961467')

print(message)