# -*- coding: utf-8 -*- 
import time
import numpy as np
import pandas as pd
import urllib.request
from tqdm.notebook import tqdm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class Crawler:
    def __init__(self, webdriver_dir):
        self.webdriver_dir = webdriver_dir


    def crawl_data(self):
        driver = webdriver.Chrome(r"{}".format(self.webdriver_dir))

        driver.get('http://recruit.dailypharm.com/Search.php?mode=offer&order=reg&optionAreaVal%5B%5D=97&optionAreaVal%5B%5D=100&optionAreaVal%5B%5D=104&optionAreaVal%5B%5D=106&optionAreaVal%5B%5D=107&optionAreaVal%5B%5D=109&optionAreaVal%5B%5D=110&optionAreaVal%5B%5D=111&optionJobVal%5B%5D=17&optionJobVal%5B%5D=12&optionJobVal%5B%5D=13&keyword=')

        # 등록일순으로 정렬하기
        driver.find_element_by_xpath('//*[@id="container"]/div[2]/div/div[3]/p[6]/a').click()

        # 정보 모으기
        dict_info = {}
        for page in range(1,2):
            driver.find_element_by_xpath('//*[@id="container"]/div[2]/div/div[3]/div/div/ul/li['+ str(page % 10) + ']/a').click()
                                        
            for num in tqdm(range(20)):
                dict_temp = {}

                # 세부정보로 들어가기
                driver.find_element_by_xpath('//*[@id="container"]/div[2]/div/div[3]/ul/li[' + str(num+1) + ']').click()

                # 필요한 정보 모아주고
                title = driver.find_elements_by_css_selector('#container > div.recruitViewWrap > div.recruitView_wrap > div.firstView.OfferViewWarp > div.offer_title_wrap > h2')[0].text
                career = driver.find_elements_by_css_selector('#container > div.recruitViewWrap > div.recruitView_wrap > div.firstView.OfferViewWarp > div.TopDetailBox > div > div:nth-child(1) > div > table > tbody > tr:nth-child(1) > td.boxbody.td_blue')[0].text
                school = driver.find_elements_by_css_selector('#container > div.recruitViewWrap > div.recruitView_wrap > div.firstView.OfferViewWarp > div.TopDetailBox > div > div:nth-child(1) > div > table > tbody > tr:nth-child(2) > td.boxbody.td_blue')[0].text
                emply_status = driver.find_elements_by_css_selector('#container > div.recruitViewWrap > div.recruitView_wrap > div.firstView.OfferViewWarp > div.TopDetailBox > div > div:nth-child(2) > div > table > tbody > tr:nth-child(1) > td.boxbody.td_blue')[0].text
                salary = driver.find_elements_by_css_selector('#container > div.recruitViewWrap > div.recruitView_wrap > div.firstView.OfferViewWarp > div.TopDetailBox > div > div:nth-child(2) > div > table > tbody > tr:nth-child(2) > td.boxbody')[0].text
                region = driver.find_elements_by_css_selector('#container > div.recruitViewWrap > div.recruitView_wrap > div.firstView.OfferViewWarp > div.TopDetailBox > div > div:nth-child(2) > div > table > tbody > tr:nth-child(3) > td.boxbody')[0].text
                gender = driver.find_elements_by_css_selector('#container > div.recruitViewWrap > div.recruitView_wrap > div.secondView > div.secondViewbody > div.recruit_wrap > div.ViewBodyContents > table > tbody > tr > td.offerTable_table2 > div > table > tbody > tr:nth-child(2) > td.tableRow_body')[0].text
                age = driver.find_elements_by_css_selector('#container > div.recruitViewWrap > div.recruitView_wrap > div.secondView > div.secondViewbody > div.recruit_wrap > div.ViewBodyContents > table > tbody > tr > td.offerTable_table2 > div > table > tbody > tr:nth-child(3) > td.tableRow_body')[0].text
                url = driver.current_url
                id_ = url.split('.php?ID=')[1]
                driver.get(url.replace('OfferView', 'offerContens'))
                content = driver.find_element_by_tag_name("body").text.strip()
                    
                # 저장하기
                dict_temp['제목'] = title
                dict_temp['경력'] = career
                dict_temp['학력'] = school
                dict_temp['고용형태'] = emply_status
                dict_temp['급여조건'] = salary
                dict_temp['근무지역'] = region
                dict_temp['성별'] = gender
                dict_temp['나이'] = age
                dict_temp['URL'] = url
                dict_temp['세부사항'] = content
                dict_info[id_] = dict_temp
                driver.back()
                driver.back()
                
                # 스크롤 이동
                element = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div/div[3]/ul/li[' + str(num+1) + ']')
                driver.execute_script("arguments[0].scrollIntoView();", element)

        driver.quit()
        data = dict_info.copy()

        return data