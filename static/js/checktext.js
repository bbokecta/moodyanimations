var tele_key = process.env.TELEGRAM_KEY;
const apiUrl = `https://api.telegram.org/bot${tele_key}/getUpdates`;

var latest_message = "";

function check_messages() {
   fetch(apiUrl)
   .then(response => {
      return response.json();
   })
   .then(response_data => {
      let messages = response_data['result']
      let latest_message = messages[messages.length - 1]['message']['text'];
      console.log(latest_message);
      return latest_message;
   })
}

const interval = 1000;

setInterval(check_messages, interval)
// check_messages();