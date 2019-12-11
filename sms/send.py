# Starting at $0.0075 to send or receive a message.
# airtel $0.0950 per
# mtn $0.0725 per

from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

# Your Account SID from twilio.com/console
account_sid = os.getenv("account_sid")
# Your Auth Token from twilio.com/console
auth_token  = os.getenv("auth_token")

client = Client(account_sid, auth_token)

message = client.messages.create(
    to = "+256758551394", 
    from_ = os.getenv("phone_number"),
    body = "Success - Test!")

# print(message.sid)
print(message)