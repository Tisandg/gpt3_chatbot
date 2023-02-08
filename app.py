from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from bot import ask, append_interaction_to_chat_log

app = Flask(__name__)
#If for some reasons the conversation with the robots gets weird, change secret key
#Secret_key is ‘any-random-string’
app.config['SECRET_KEY'] = '89djhf9lhkd93'

@app.route('/gptchat', methods=['POST'])
def jabe():
  incoming_msg = request.values['Body']
  chat_log = session.get('chat_log')
  answer = ask(incoming_msg, chat_log)
  session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer, chat_log)
  msg = MessagingResponse()
  msg.message(answer)
  return str(msg)

if __name__ == '__main__':
  app.run(debug=True)