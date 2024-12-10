from flask import Flask, render_template, request
from flask_apscheduler import APScheduler
from chatbot import get_response
from telegrambot2 import get_messages, arabica_reply
from flask_socketio import SocketIO 

app = Flask(__name__, static_url_path='/static') 
message_list = []

@app.route('/')
def index():
    result = get_messages()
    new_question = result[0]
    chat_id = result[1]

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
    print(answer)
    return render_template('index.html', question=new_question, bot_answer=answer, number=4)

def update_text():
    result = get_messages()
    message_list.append(result)
    new_question = result[0]
    chat_id = result[1]

    answer = get_response(new_question)

    if len(message_list) > 1:
        if message_list[-1][2] != message_list[-2][2]:
            arabica_reply(chat_id, answer)
     
    socketio.emit('new_data', {'data' : answer})

if (__name__ == "__main__"):
    scheduler = APScheduler()
    socketio = SocketIO(app)

    scheduler.add_job(func=update_text, trigger='interval', id='job', seconds=5)
    scheduler.start()
    app.run(port = 5000)