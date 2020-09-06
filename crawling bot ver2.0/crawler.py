# -*- coding: utf-8 -*- 
import time
import numpy as np
import pandas as pd
import urllib.request
import requests
import json
from bs4 import BeautifulSoup

class Crawler:
    def __init__(self):
        self.name = "I am a good robot"

    def load_past_data(self, url):
        with open(url,'r') as f:
            data = json.load(f)
        return data

    def crawl_data(self):
        url = 'http://recruit.dailypharm.com/Search.php?mode=offer&order=reg&optionAreaVal%5B%5D=97&optionAreaVal%5B%5D=100&optionAreaVal%5B%5D=104&optionAreaVal%5B%5D=106&optionAreaVal%5B%5D=107&optionAreaVal%5B%5D=109&optionAreaVal%5B%5D=110&optionAreaVal%5B%5D=111&optionJobVal%5B%5D=17&optionJobVal%5B%5D=12&optionJobVal%5B%5D=13&keyword='
        res = requests.get(url)

        soup = BeautifulSoup(res.text, 'html.parser')
        contents = soup.select("li.search_tabCont_wrap a")

        dict_info = {}
        for content in contents:
            dict_temp = {}
            href = content['href']
            content_url = 'http://recruit.dailypharm.com' + href
            id_ = content_url.split('.php?ID=')[1]
            
            # crawl title and region
            res_2 = requests.get(content_url)
            soup_2 = BeautifulSoup(res_2.content.decode('euc-kr','replace'), 'html.parser')
            title = soup_2.select("div.offer_title_wrap h2")[0].text
            region = soup_2.select("div.boxList td.boxbody")[4].text.strip()
            
            # crawl details
            res_3 = requests.get(content_url.replace('OfferView', 'offerContens'))
            soup_3 = BeautifulSoup(res_3.content.decode('euc-kr','replace'), 'html.parser')
            details = ''
            for i in soup_3.select("body p"):
                details = details + '\n' + i.text.strip()
            
            # save crawled informations
            dict_temp['title'] = title
            dict_temp['region'] = region
            dict_temp['details'] = details
            dict_temp['URL'] = content_url
            dict_info[id_] = dict_temp
        return dict_info