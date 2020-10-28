import requests
import time
import os

def telegram_bot_sendtext(bot_message):
    
    bot_token = os.environ.get('BOT_TOKEN')
    bot_chatID = os.environ.get('BOT_CHAT_ID')
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)

    return response.json()

def main():
  while True:
    telegram_bot_sendtext("I'm sending a message every 3 seconds")
    time.sleep(3)

if __name__ == '__main__':
  main()

