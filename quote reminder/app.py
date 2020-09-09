# -*- coding: utf-8 -*- 
# 누나 ID: 1238642275
# 나의 ID: 1179537484
from extractor import Extractor
import telegram
import json
import time

# bot 세팅
TOKEN = 'Token'
bot = telegram.Bot(token=TOKEN)
updates = bot.getUpdates()

# 데이터 세팅
for i in range(5):
    model = Extractor("다시 볼 글귀들 모음.xlsx")
    idx, quote, source = model.todays_quote()
    bot.send_message(chat_id=id, text="오늘의 리마인더\n\n* index: {}\n\n* {}\n\n from: {}".format(idx, quote, source))