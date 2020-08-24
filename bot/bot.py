# -*- coding: utf-8 -*- 
# 누나 ID: 1238642275
# 나의 ID: 1179537484
from crawler import Crawler
import telegram
import json
import time

# bot 세팅
TOKEN = 'Token 입력하시고'
bot = telegram.Bot(token=TOKEN)

# 크롤러 세팅
crawler = Crawler("chromedriver 주소 입력하시고")
count = 0 

# 알림봇 일하기 시작!
while True:
    # 시간 및 횟수 측정!
    count += 1
    now = time.strftime('%H%M%S')
    print("*"*15,"{}시 {}분에 {}차 시작~".format(now[:2], now[2:4], count), "*"*15)

    # 과거 데이터 불러오기
    with open('info_crawled.json','r') as outfile:
        past_data = json.load(outfile)

    new_data = crawler.crawl_data()
    
    new_info = list(set(new_data.keys() - set(past_data.keys())))
    print("새로운 정보: {}건".format(len(new_info)))

    if new_info == []:
        pass
    elif new_info != []:
        for new in sorted(new_info):
            region = new_data[new]['근무지역']
            title = new_data[new]['제목']
            info = new_data[new]['세부사항']
            URL = new_data[new]['URL']

            bot.send_message(chat_id="id입력하시고", text="새로운 공고가 나왔어요!!!\n\n* 제목: {}\n* 지역: <{}>\n*세부사항: {} \n\n\n 관심있으면 여길 클릭하숑!\n{}".format(title, region, info, URL))

    new_data.update(past_data)

    with open('info_crawled.json', 'w') as outfile:
        json.dump(new_data, outfile, indent=4)

    print("끝!")
    time.sleep(600)