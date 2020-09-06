# -*- coding: utf-8 -*- 
import json
import time
from crawler import Crawler
from teleBot import TeleBot
from datetime import date

# Modules Setting
crawler = Crawler()
teleBot = TeleBot()

# Start!
while True:
    # 시간 및 횟수 측정!
    today, now = date.today(), time.strftime('%H%M%S')
    print("*"*15,"{} {}시 {}분에 시작~".format(today, now[:2], now[2:4]), "*"*15)

    # Crawl and Send telegram message
    past_data = crawler.load_past_data('/Users/junghyunwoo/Downloads/crawled_data.json')
    new_data = crawler.crawl_data()
    teleBot.send_message(past_data, new_data)

    # Save new_info
    teleBot.update_and_save_data(past_data, new_data, '/Users/junghyunwoo/Downloads/crawled_data.json')

    print("Finished")
    time.sleep(600)

