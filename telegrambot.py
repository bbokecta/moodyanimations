import threading
import time
import requests
import traceback
from threading import Thread

with open("telegram_keys.txt", "r") as telegram_file:
    telegram_key = telegram_file.read()

class ReturnableThread(Thread):
    # This class is a subclass of Thread that allows the thread to return a value.
    def __init__(self, target):
        Thread.__init__(self)
        self.target = target
        self.result = None
    
    def run(self) -> None:
        self.result = self.target()

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
    # if len(all_results) == 2:
    #     if all_results[0] == all_results[1]:
    #         return all_results[-1]
    #     else:
    #        return all_results
    return results


def message_check():
   recent_message = requests.post(
                url=f"https://api.telegram.org/bot{telegram_key}/getUpdates",
            ).json()
   chat_id = recent_message['result'][-1]['message']['chat']['id']
   message_contents = recent_message['result'][-1]['message']['text']
   returned_data = [chat_id, message_contents]
   return returned_data


thread = ReturnableThread(target=lambda: every(1, message_check))
thread.start()

while thread.result is None:
   time.sleep(0.1)

print(thread.result[1])



