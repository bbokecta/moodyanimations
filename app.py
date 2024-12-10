from flask import Flask, render_template, request
from chatbot import get_response
from telegrambot2 import get_messages, arabica_reply 

app = Flask(__name__, static_url_path='/static') 

message_update = get_messages()
new_question = message_update[0]

@app.route('/')
def index():
    chat_id = message_update[1]
    answer = get_response(new_question)
    arabica_reply(chat_id, answer)
    return render_template('index.html', question=new_question, bot_answer=answer, number=4)

@app.route('/', methods=['POST'])
def index_post():
    message_update = get_messages()
    new_question = message_update[0]
    chat_id = message_update[1]

    answer = get_response(new_question)
    arabica_reply(chat_id, answer)
    return render_template('index.html', question=new_question, bot_answer=answer, number=4)