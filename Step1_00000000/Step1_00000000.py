# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 22:27:34 2019

@author: j32u4ukh
"""

from enigma import Enigma, Rotor

"""
operator1:print, len, 
variable1：int, str, variable, type()
variable2：+-*/%, +=, -=, ==, ..., variable_name
operator1_5:True, False, and, or, not
variable3：二進制、十進制、二進制應用
array1：append(), sort(), copy()；id()
operator2:ord('a') & chr(97)：ASCII 數值與符號的轉換, int(), float()
operator3:for, while loop, break, str.format(), continue
array2:[i for i in range]
operator4:try, except, Error
def1：function, return, _variable_name
def2：assert, 預設值, *args
panda：將 rotors.xlsx 和 rotors_status.xlsx 建立並儲存成檔案
class1：(Object-oriented,OO)
class2：inherit, super()
class3：if __name__ == "__main__":

     
if, else
==
"""

# rotors.xlsx
I   = ['H', 'e', 'l', 'o', 'W', 'r', 'd', 's']
II  = ['H', 'o', 'W', 'r', 'd', 'e', 'l', 's']
III = ['H', 'd', 's', 'e', 'l', 'o', 'W', 'r']
IV  = ['r', 'd', 's', 'e', 'H', 'o', 'W', 'l']
V   = IV.copy()
V.sort()

items =  ['H', 'e', 'l', 'o', 'W', 'r', 'd', 's']
items1 = ['H', 'o', 'W', 'r', 'd', 'e', 'l', 's']
items2 = ['H', 'd', 's', 'e', 'l', 'o', 'W', 'r']
items3 = ['r', 'd', 's', 'e', 'H', 'o', 'W', 'l']
items4 = items.copy()
items4.sort()
word = "HelloWorld"

enigma = Enigma(items)
rotor1 = Rotor(items1)
rotor2 = Rotor(items2)
rotor3 = Rotor(items3)
rotor4 = Rotor(items4)
enigma.add(rotor1)
enigma.add(rotor2)
enigma.add(rotor3)
enigma.add(rotor4)

# set rotor after add rotors into enigma
# rotors_status.xlsx
enigma.setRotors(9, 5, 2, 7)
enigma.compile_()


encode = enigma.swap(word)        
print("encode:", encode)

enigma.setRotors(9, 5, 2, 7)
decode = enigma.swap(encode)   
print("decode:", decode)
