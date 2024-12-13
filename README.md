### Usage

This application allows users to communicate with a telegram bot named Arabica, the moody teenager. Every 5 seconds Arabica responds to the most recently sent message and the response is displayed on my Flask site, as the narration to an animated Three.js scene.

### Installation

To run this program locally, you'll need to install the libraries from my requirements.txt file. 

You will also need to create your own Telegram bot to interface with, which you can do [here](https://core.telegram.org/api#bot-api). 

Once you get the API token for your Telegram bot from @BotFather, add the token to your directory as a .txt file. In line #5 of the telegrambot.py code, you'll need to paste your token filename in place of 'arabica_key.txt'.

Happy botting!