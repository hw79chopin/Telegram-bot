# -*- coding: utf-8 -*- 
import pandas as pd
from random import *

class Extractor:
    def __init__(self, url):
        self.df = pd.read_excel(url)

    
    def todays_quote(self):
        idx = randint(1, self.df.shape[0]+1)
        return idx, self.df.loc[idx]['신문이름. 책 제목. 화자'], self.df.loc[idx]['글귀']

    def update_starts(self, id):
        stars = self.df.loc['']