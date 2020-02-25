from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("Welcome everyone to my presentation!!")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
	
	
	




