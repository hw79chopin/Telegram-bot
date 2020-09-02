# -*- coding: utf-8 -*- 
# 누나 ID: 1238642275
# 나의 ID: 1179537484
from extractor import Extractor
import telegram
import json
import time

class Messenger:
    def __init__(self):
        self.name = "나는야 착한 로봇"
        TOKEN = 'token'
        self.bot = telegram.Bot(token = TOKEN)

    def send_quote(self):
        model = Extractor("quotes.xlsx")
        idx, source, quote = model.todays_quote()

        self.bot.send_message(chat_id=1179537484, text="오늘의 리마인더\n\n* index: {}\n\n* {}\n\n from: [{}]".format(idx, quote, source))
