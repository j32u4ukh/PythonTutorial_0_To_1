"""
Step0_05000000:operator1:print, len
Step0_10000000:variable1:int, str, variable, type()
Step0_15000000:variable2:+-*/%, +=, -=, ==, ..., variable_name
Step0_20000000:operator1_5:True, False, and, or, not
Step0_22500000:operator1_8:if elif else
Step0_25000000:variable3:二進制、十進制、二進制應用
Step0_30000000:array1:append(), sort(), copy()；索引值；id()
Step0_35000000:operator2:ord('a') & chr(97):ASCII 數值與符號的轉換, int(), float()
Step0_40000000:operator3:for, while, str.format()
Step0_45000000:operator4:break, continue
Step0_50000000:array2:[i for i in range]
Step0_55000000:operator5:try, except, Error
Step0_60000000:dict1:建立、新增、取值
Step0_65000000:def1:function, return, _variable_name
Step0_70000000:def2:assert, 預設值, *args
Step0_75000000:operator6:import, from, pip # 多個 import 可用 () 框起來
Step0_80000000:pandas:csv:rotors, rotors_status, choose_rotor # .strftime("%Y-%m-%d")
Step0_85000000:class1:(Object-oriented,OO), Pipeline
Step0_90000000:class2:inherit, super(), Reflector
Step0_95000000:class3:if __name__ == "__main__":, Rotor
Step1_00000000:enigma.py, Step1_00000000.py
"""
from datetime import datetime
from random import shuffle

import pandas as pd

from Step1_00000000.enigma import Enigma, Rotor


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
    rotors = [element.copy() for _ in range(4)]

    for r in rotors:
        shuffle(r)
        print(r[:10])

    items = list(rotors[0])
    items1 = list(rotors[1])
    items2 = list(rotors[2])
    items3 = list(rotors[3])

    return items, items1, items2, items3


items, items1, items2, items3 = implementWithPandas()
# items, items1, items2, items3 = implementWithoutPandas()

word = "HelloWorld"

enigma = Enigma(items)
rotor1 = Rotor(items1)
rotor2 = Rotor(items2)
rotor3 = Rotor(items3)
# rotor4 = Rotor(items4)
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
