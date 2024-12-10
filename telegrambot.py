import threading
import time
import requests
import traceback
from threading import Thread

with open("telegram_keys.txt", "r") as telegram_file:
    telegram_key = telegram_file.read()

def message_check():
   recent_message = requests.post(
                url=f"https://api.telegram.org/bot{telegram_key}/getUpdates",
            ).json()
   chat_id = recent_message['result'][-1]['message']['chat']['id']
   message_contents = recent_message['result'][-1]['message']['text']
   returned_data = [chat_id, message_contents]
   return returned_data

returned_data = message_check()
print(returned_data)

reply_text = 'hello friend'

def ivy_reply(reply_text):
    requests.post(
    url=f'https://api.telegram.org/bot{telegram_key}/sendMessage',
    data={'chat_id': chat_id, 'text': reply_text}
    ).json()