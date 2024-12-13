import json
import urllib.request
import requests

with open("arabica_key.txt", "r") as key_file:
    arabica_key = key_file.read()

def get_messages():
    url = f"https://api.telegram.org/bot{arabica_key}/getUpdates"

    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)

    message_data = json.loads(response.read())

    text = message_data['result'][-1]['message']['text']
    chat_id = message_data['result'][-1]['message']['chat']['id']
    message_id = message_data['result'][-1]['message']['date']
    # print(text)
    return [text, chat_id, message_id]

def arabica_reply(chat_id, reply_text):
    requests.post(
    url=f'https://api.telegram.org/bot{arabica_key}/sendMessage',
    data={'chat_id': chat_id, 'text': reply_text}
    ).json()