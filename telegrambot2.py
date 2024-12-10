import requests
import urllib.request
import json

with open("telegram_keys.txt", "r") as telegram_file:
    telegram_key = telegram_file.read()
url=f"https://api.telegram.org/bot{telegram_key}/getUpdates"

def check_messages(): 

    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    
    recent_message = json.loads(response.read())

    # chat_id = recent_message['result'][-1]['message']['chat']['id']
    message_contents = recent_message['result'][-1]['message']['text']
    # returned_data = [chat_id, message_contents]
    print(message_contents)

check_messages()