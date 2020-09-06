# -*- coding: utf-8 -*- 
import json
import time
import telegram
import numpy as np
import pandas as pd

class TeleBot:
    def __init__(self):
        self.name = "I am a good robot"

    def send_message(self, past_data, new_data):
        TOKEN = '1257448855:AAGU5nTrmFI--06ZRUTBfn9Wqq_oZ4_BLD8'
        bot = telegram.Bot(token=TOKEN)
        new_info = list(set(new_data.keys() - set(past_data.keys())))
        print("새로운 정보: {}건".format(len(new_info)))

        if new_info == []:
            pass

        elif new_info != []:
            for new in sorted(new_info):
                region = new_data[new]['region']
                title = new_data[new]['title']
                info = new_data[new]['details']
                URL = new_data[new]['URL']

                # 누나 ID: 1238642275
                # 나의 ID: 1179537484
                bot.send_message(chat_id=1179537484, text="새로운 공고가 나왔어요!!!\n\n* 제목: {}\n* 지역: {}\n* 세부사항: {} \n\n\n 관심있으면 여길 클릭하숑!\n{}".format(title, region, info, URL))
                # bot.send_message(chat_id=1238642275, text="새로운 공고가 나왔어요!!!\n\n* 제목: {}\n* 지역: <{}>\n* 세부사항: {} \n\n\n 관심있으면 여길 클릭하숑!\n{}".format(title, region, info, URL))

    def update_and_save_data(self, past_data, new_data, dir):
        new_data.update(past_data)
        with open(dir, 'w') as outfile:
            json.dump(new_data, outfile, indent=4)