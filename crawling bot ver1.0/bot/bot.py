# -*- coding: utf-8 -*- 
import json
import time
from crawler import Crawler, TeleBot
from messenger import Messenger
from datetime import date

# 크롤러 세팅
crawler = Crawler()
telebot = TeleBot()

# 알림봇 일하기 시작!
count = 0
while True:
    count += 1
    # 시간 및 횟수 측정!
    if count == 1:
        previous_day = 1
    today, now = date.today(), time.strftime('%H%M%S')
    print("*"*15,"{} {}시 {}분에 시작~".format(today, now[:2], now[2:4]), "*"*15)

    # 누나를 위한 텔레그램 봇 
    past_data = crawler.load_past_data('info_crawled.json')
    new_data = crawler.crawl_data("chromedriver")

    telebot.send_message(past_data, new_data)
    telebot.update_and_save_data(past_data, new_data, 'info_crawled.json')

    # 나를 위한 봇
    if today != previous_day:
        model = Messenger()
        model.send_quote()
    
    print("끝!")
    previous_day = today
    time.sleep(600)