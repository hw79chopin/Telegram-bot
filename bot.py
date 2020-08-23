# -*- coding: utf-8 -*- 

import telegram

TOKEN = '1257448855:AAGU5nTrmFI--06ZRUTBfn9Wqq_oZ4_BLD8'
bot = telegram.Bot(token=TOKEN)

updates = bot.getUpdates()

for i in updates:
    print(i.message.chat.id)

bot.send_message(chat_id=1179537484, text="잘 가니?")
# import time

# while True:
#    your_script_hereㅣ
#    time.sleep(300)