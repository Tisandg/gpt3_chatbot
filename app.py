from flask import Flask, request, session
from twilio.twim.messaging_response import MessagingResponse
from bot import ask_append_interaction_to_chat_log

app = Flask(__name__)
#If for some reasons the conversation with the robots gets weird, change secret key
app.config['SECRET_KEY'] = '89djhf9lhkd93'

@app.route('gptchat', methods='POST')
def jabe():
  incoming_msg = request.values['Body']
  chat_log = session.get('chat_log')
  answer = ask(incoming_msg, chat_log)