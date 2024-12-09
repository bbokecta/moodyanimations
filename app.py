from flask import Flask, render_template, request
from chatbot import get_response
from telegrambot import message_check, ivy_reply 

app = Flask(__name__, static_url_path='/static') 

new_question = ""

@app.route('/')
def index():
    # new_question = message_check()[1]
    answer = get_response(new_question)
    ivy_reply(answer)
    return render_template('index.html', question=new_question, bot_answer=answer, number=4)

@app.route('/', methods=['POST'])
def index_post():
    # user_question = request.form['req_question']
    user_question = message_check()
    answer = get_response(user_question)
    bot_answer = answer.split('-')[0]
    num_answer = answer.split('-')[1]
    return render_template('index.html', question=user_question, bot_answer=bot_answer, number=num_answer)