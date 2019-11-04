# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 22:27:34 2019

@author: j32u4ukh
"""

from enigma import Enigma, Rotor

"""
operator1:print, len, 
variable1:int, str, variable, type()
variable2:+-*/%, +=, -=, ==, ..., variable_name
operator1_5:True, False, and, or, not
operator1_8:if elif else
variable3:二進制、十進制、二進制應用
array1:append(), sort(), copy()；索引值；id()
operator2:ord('a') & chr(97):ASCII 數值與符號的轉換, int(), float()
operator3:for, while, str.format()
operator4:break, continue
array2:[i for i in range]
operator5:try, except, Error
dict1:建立、新增、取值
def1:function, return, _variable_name
def2:assert, 預設值, *args
operator6:import, from, pip
pandas:將 rotors.xlsx 和 rotors_status.xlsx 建立並儲存成檔案
class1:(Object-oriented,OO)
class2:inherit, super(), Reflector
class3:if __name__ == "__main__":, Rotor

     
if, else
==
"""
from datetime import datetime

import pandas as pd


# rotors.csv
rotors_df = pd.read_csv("../rotors.csv", header=0, index_col=0)
choose_rotor_df = pd.read_csv("../choose_rotor.csv", header=0, index_col=0)
#I   = ['H', 'e', 'l', 'o', 'W', 'r', 'd', 's']
#II  = ['H', 'o', 'W', 'r', 'd', 'e', 'l', 's']
#III = ['H', 'd', 's', 'e', 'l', 'o', 'W', 'r']
#IV  = ['r', 'd', 's', 'e', 'H', 'o', 'W', 'l']
#V   = IV.copy()
#V.sort()

#for i in choose_rotor.index:
#     print(pd.to_datetime(i, format="%Y-%m-%d"))

#I   = rotors.loc['I'].values
#II  = rotors.loc['II'].values
#III = rotors.loc['III'].values
#IV  = rotors.loc['IV'].values
#V   = rotors.loc['V'].values

today = datetime.today()
# current_date = datetime(2019, 11, 4)
current_date = datetime(today.year, today.month, today.day)
date_index = current_date.strftime("%Y-%m-%d")
rotors_index = choose_rotor_df.loc[date_index].values
rotors = [rotors_df.loc['I'].values for r in rotors_index]

items =  ['H', 'e', 'l', 'o', 'W', 'r', 'd', 's']
items1 = ['H', 'o', 'W', 'r', 'd', 'e', 'l', 's']
items2 = ['H', 'd', 's', 'e', 'l', 'o', 'W', 'r']
items3 = ['r', 'd', 's', 'e', 'H', 'o', 'W', 'l']
items4 = items.copy()
items4.sort()

items = list(rotors[0].copy())
items.sort()
items1 = list(rotors[0])
items2 = list(rotors[1])
items3 = list(rotors[2])
word = "helloworld"

enigma = Enigma(items)
rotor1 = Rotor(items1)
rotor2 = Rotor(items2)
rotor3 = Rotor(items3)
#rotor4 = Rotor(items4)
enigma.add(rotor1)
enigma.add(rotor2)
enigma.add(rotor3)
#enigma.add(rotor4)

# set rotor after add rotors into enigma
# rotors_status.xlsx
enigma.setRotors(9, 5, 2)
enigma.compile_()


encode = enigma.swap(word)        
print("encode:", encode)

enigma.setRotors(9, 5, 2)
decode = enigma.swap(encode)   
print("decode:", decode)
