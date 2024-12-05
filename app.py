from flask import Flask, render_template, request
from chatbot import get_response 

app = Flask(__name__, static_url_path='/static') 

new_question = "Hi!"

@app.route('/')
def index():
    answer = get_response(new_question)
    return render_template('index.html', question=new_question, bot_answer=answer, number=4)

@app.route('/', methods=['POST'])
def index_post():
    # user_address1 = request.form['req_add1']
    user_question = request.form['req_question']
    answer = get_response(user_question)
    bot_answer = answer.split('-')[0]
    num_answer = answer.split('-')[1]
    return render_template('index.html', question=user_question, bot_answer=bot_answer, number=num_answer)