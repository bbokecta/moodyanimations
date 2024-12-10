import requests

with open("telegram_keys.txt", "r") as telegram_file:
    telegram_key = telegram_file.read()

recent_message = requests.post(
    url=f"https://api.telegram.org/bot{telegram_key}/getUpdates",
    ).json()

# chat_id = recent_message['result'][-1]['message']['chat']['id']
message_contents = recent_message['result'][-1]['message']['text']
# returned_data = [chat_id, message_contents]
print(message_contents)