# -*- coding: utf-8 -*- 

import telegram

TOKEN = 'Secret'
bot = telegram.Bot(token=TOKEN)

updates = bot.getUpdates()

for i in updates:
    print(i.message.chat.id)

bot.send_message(chat_id="Secret", text="잘 가니?")
# import time

# while True:
#    your_script_hereㅣ
#    time.sleep(300)
