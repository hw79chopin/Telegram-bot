# -*- coding: utf-8 -*- 
from crawler import Crawler
import telegram
import time

# bot 세팅
TOKEN = 'telegram_token'
bot = telegram.Bot(token=TOKEN)

# 크롤러 세팅
crawler = Crawler("chrome-driver-directory")
count = 0 

# 알림봇 일하기 시작!
while True:
    # 시간 및 횟수 측정!
    count += 1
    now = time.strftime('%H%M%S')
    print("*"*15,"{}시 {}분에 {}차 시작~".format(now[:2], now[2:4], count), "*"*15)
    
    result = crawler.crawl_data()
    if count == 1:
        previous_result = result
    
    new_info = list(set(result.keys() - set(previous_result.keys())))
    print("새로운 정보: {}건".format(len(new_info)))
    if new_info == []:
        pass
    elif new_info != []:
        for new in new_info:
            region = result[new]['근무지역']
            title = result[new]['제목']
            URL = result[new]['URL']
            bot.send_message(chat_id=telegram_id1, text="새로운 공고가 나왔어요!!!\n* 지역: {}\n* 제목: <{}>\n관심있으면 여길 클릭하숑!\n{}".format(region, title, URL))
            bot.send_message(chat_id=telegram_id2, text="새로운 공고가 나왔어요!!!\n* 지역: {}\n* 제목: <{}>\n관심있으면 여길 클릭하숑!\n{}".format(region, title, URL))

    previous_result = result
    print("끝!")
    time.sleep(1200)
