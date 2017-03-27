from twilio.rest import TwilioRestClient

account_sid = "AC7e12c6628acbe723c054aeb7130f7ac6" # Your Account SID from www.twilio.com/console
auth_token  = "8c67a16ce0377c3e10d67dcd73e52817"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Pranav",
    to="+91 8001342093",    # Replace with your phone number
    from_="+19544177784") # Replace with your Twilio number

print(message.sid)
