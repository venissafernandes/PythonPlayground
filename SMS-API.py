from twilio.rest import Client

account_sid='ACe07f4947a37a4c5fb69b40fe13dcad38'
auth_token='280f4bb22f54bffe6004d25359d5f4be'
client=Client(account_sid,auth_token)

message = client.messages.create(
    from_='+12053464687',
    to='+15512326100',
    body='Thanks for purchasing the shorts!!'
)

print(message.sid)