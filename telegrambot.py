import threading
import time
import requests
import traceback

with open("telegram_keys.txt", "r") as telegram_file:
    telegram_key = telegram_file.read()

# def message_check(timer_runs):
#     while timer_runs.is_set():
#         recent_message = requests.post(
#                 url=f"https://api.telegram.org/bot{telegram_key}/getUpdates",
#             ).json()
#         time.sleep(5)

#     return recent_message
incoming_message = ""

def every(delay, task):
  next_time = time.time() + delay
  while True:
    time.sleep(max(0, next_time - time.time()))
    try:
    #   task()
      results = task()
    except Exception:
      traceback.print_exc() 
    # skip tasks if we are behind schedule:
    next_time += (time.time() - next_time) // delay * delay + delay
    print(results)


def message_check():
   recent_message = requests.post(
                url=f"https://api.telegram.org/bot{telegram_key}/getUpdates",
            ).json()
   chat_id = recent_message['result'][-1]['message']['chat']['id']
   message_contents = recent_message['result'][-1]['message']['text']
   return chat_id, message_contents


# thread = threading.Thread(target=lambda: every(2, message_check))
thread = threading.Thread(target=lambda: every(2, message_check))
thread.start()

def task_done():
   print("task done")



# def timer(timer_runs):
#    while timer_runs.is_set():
#       thread = threading.Thread(target=lambda: every(2, message_check))
#       thread.start()

# timer_runs = threading.Event()
# timer_runs.set()
# time.sleep(15)
# timer_runs.clear()
# print("Finished")





# reply_text = 'hello friend'

# ivy_reply = requests.post(
#         url=f'https://api.telegram.org/bot{telegram_key}/sendMessage',
#         data={'chat_id': chat_id, 'text': reply_text}
#     ).json()