from twilio.rest import Client

# your account sid and auth token from twilio.com/console
account_sid='ACe07f4947a37a4c5fb69b40fe13dcad38'
auth_token='280f4bb22f54bffe6004d25359d5f4be'
client = Client(account_sid, auth_token)

message = client.messages.create(
    media_url="https://i.ytimg.com/vi/U_JbTHp6uzI/maxresdefault.jpg",
    body="Is this an MMS?",
    from_="+12053464687",
    to="+15512326100"
)

print(message.sid)