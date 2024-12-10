import json
import urllib.request

with open("arabica_key.txt", "r") as key_file:
    arabica_key = key_file.read()

def get_messages():
    url = f"https://api.telegram.org/bot{arabica_key}/getUpdates"

    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)

    message_data = json.loads(response.read())

    text = message_data['result'][0]['message']['text']
    chat_id = message_data['result'][0]['message']['chat']['id']

    return [text, chat_id]

results = get_messages()
print(results)