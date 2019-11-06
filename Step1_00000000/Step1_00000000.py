# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 22:27:34 2019

@author: j32u4ukh

operator1:print, len, 
variable1:int, str, variable, type()
variable2:+-*/%, +=, -=, ==, ..., variable_name
operator1_5:True, False, and, or, not
operator1_8:if elif else
variable3:二進制、十進制、二進制應用
array1:append(), sort(), copy()；索引值；id()
*operator2:ord('a') & chr(97):ASCII 數值與符號的轉換, int(), float()
*operator3:for, while, str.format()
*operator4:break, continue
*array2:[i for i in range]
*operator5:try, except, Error
*dict1:建立、新增、取值
*def1:function, return, _variable_name
*def2:assert, 預設值, *args
*operator6:import, from, pip # 多個 import 可用 () 框起來
*pandas:csv:rotors, rotors_status, choose_rotor # .strftime("%Y-%m-%d")
*class1:(Object-oriented,OO), Pipeline
*class2:inherit, super(), Reflector
*class3:if __name__ == "__main__":, Rotor
*1_00000000:enigma.py, Step1_00000000.py
"""
from datetime import datetime
from random import shuffle

import pandas as pd

from enigma import Enigma, Rotor


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
     _english_element = [chr(i) for i in range(65, 90 + 1)]
     _english_element += [chr(i) for i in range(97, 122 + 1)]
     
     return _english_element


def implementWithPandas():
     # rotors.csv
     rotors_df = pd.read_csv("../rotors.csv", header=0, index_col=0)
     choose_rotor_df = pd.read_csv("../choose_rotor.csv", header=0, index_col=0)
     
     current_date = datetime(2019, 11, 4)
     date_index = current_date.strftime("%Y-%m-%d")
     rotors_index = choose_rotor_df.loc[date_index].values
     rotors = [rotors_df.loc[r].values for r in rotors_index]
     
     for r in rotors:
          print(r[:10])
     
     items = list(rotors[0].copy())
     items.sort()
     items1 = list(rotors[0])
     items2 = list(rotors[1])
     items3 = list(rotors[2])
     
     return items, items1, items2, items3
     

def implementWithoutPandas():
     element = getTaiwanElement() + getJapanElement() + getEnglishElement()
     rotors = [element.copy() for i in range(4)]
     
     for r in rotors:
          shuffle(r)
          print(r[:10])
     
     items = list(rotors[0])
     items1 = list(rotors[1])
     items2 = list(rotors[2])
     items3 = list(rotors[3])
     
     return items, items1, items2, items3


items, items1, items2, items3 = implementWithPandas()
#items, items1, items2, items3 = implementWithoutPandas()

word = "HelloWorld"

enigma = Enigma(items)
rotor1 = Rotor(items1)
rotor2 = Rotor(items2)
rotor3 = Rotor(items3)
#rotor4 = Rotor(items4)
enigma.add(rotor1)
enigma.add(rotor2)
enigma.add(rotor3)

enigma.setRotors(7, 8, 4)
enigma.compile_()

encode = enigma.swap(word)        
print("encode:", encode)

enigma.setRotors(7, 8, 4)
decode = enigma.swap(encode)   
print("decode:", decode)  


