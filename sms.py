from flask import Flask, request
app = Flask(__name__)
from twilio.twiml.messaging_response import MessagingResponse

@app.route('/sms', methods=['POST'])
def sms():
    print(request.form)
    resp = MessagingResponse()
    resp.message("Hello boy!")
    return str(resp)
    
@app.route('/')
def index():
    return "Hello all"

if __name__ == '__main__':
    app.run(debug=True)
