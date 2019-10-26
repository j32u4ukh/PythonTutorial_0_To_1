# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:47:26 2019

@author: j32u4ukh

教學大綱：
1. 建立 DataFrame
2. 根據行數，取出資料
3. 根據欄位，取出資料
4. 迴圈印出日期
5. 資料寫出(rotors.xlsx 和 rotors_status.xlsx)
6. 資料讀入
"""
from datetime import datetime
from datetime import timedelta
from random import shuffle
import pandas as pd

df = pd.DataFrame({'column 1':[i for i in range(10)],
                   'column 2':[i for i in range(10, 20)],
                   'column 3':[i for i in range(20, 30)]})

print(df.head())

def getTaiwanElement():
     # ㄅ ASCII: 12549
     # ㄩ ASCII: 12585
     _taiwan_element = [chr(i) for i in range(12549, 12585 + 1)]
     
     # ˊ ASCII: 714
     # ˇ ASCII: 711
     # ˋ ASCII: 715
     # ˙ ASCII: 729          
     punctuation = ["ˊ", "ˇ", "ˋ", "˙"]
     for i in punctuation:
          _taiwan_element.append(i)
          
     return _taiwan_element


def getJapanElement():
     # あ ASCII: 12354
     # ん ASCII: 12435
     _japan_element = [chr(i) for i in range(12354, 12435 + 1)]
     
     return _japan_element
     

def getEnglishElement():
     # a ASCII: 97
     # z ASCII: 122
     _english_element = [chr(i) for i in range(97, 122 + 1)]
     
     return _english_element


taiwan_element = getTaiwanElement()
japan_element = getJapanElement()
english_element = getEnglishElement()
element = taiwan_element + japan_element + english_element

df = pd.DataFrame(columns=[i for i in range(len(element))])


today = datetime.today()
print(today)

current_date = datetime(2019, 11, 1)
end_date = datetime(2019, 12, 1)

while current_date < end_date:
     element_copy = element.copy()
     shuffle(element_copy)
     df.loc[current_date] = element_copy
     current_date += timedelta(days=1)

print(df.head())
print(df.tail())

df.to_csv("rotors.csv")

read_df = pd.read_csv("rotors.csv")
print(read_df.head())
print(read_df.tail())