# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:46:56 2019

@author: j32u4ukh

教學大綱：
1. function
2. return
3. _variable_name

前面我們曾利用迴圈去添加元素到陣列當中，將重複的內容寫到了迴圈當中。

當我們要做一些重複的事情，除了利用迴圈，還會使用 '函式(def)' 來將這些內容重複呼叫。

其實前面所使用的 print() 、 len() 、 append() 、、、都是函式(def)的例子。
"""
def printAToZ():
     a_to_z = []
     for i in range(97, 97 + 26):
          _char = chr(i)
          a_to_z.append(_char)
          
     print(a_to_z)


printAToZ()
printAToZ()
"""
上方例子 printAToZ() 的括弧中沒有東西，也沒有使用到外部的變數，因此每次執行的結果都是相同的。

括弧中可以放一些變數，又可稱為參數，讓我們可以執行'大部分相同，只有些許部分不同'的內容。
"""


def elementIndex(_array, _element):
     try:
          _index = _array.index(_element)
     except ValueError:
          _array.append(_element)
          # sort array
          _array.sort()
     
          _index = _array.index(_element)
     
     print("element:{} @index:{}, array = {}".format(
               _element,
               _index,
               _array
           ))
     

array = [1, 3, 5, 7, 9]
elementIndex(array, 5)
elementIndex(array, 6)

array = [0, 2, 4, 6, 8]
elementIndex(array, 5)
elementIndex(array, 6)
"""
可以看到，一樣的函式根據不同的參數，可以執行'大部分相同，只有些許部分不同'的內容。

函式除了單純執行程式碼，還可以回傳數值。比如幫我計算完 BMI 後，透過最後一行的
return 將結果回傳出來。
"""


def computeBmi(_height, _weight):
     try:
          # cm → m
          _height /= 100
          _bmi = _weight / (_height * _height)
     except ZeroDivisionError:
          _height = 1.6
          _bmi = _weight / (_height * _height)
          
     return _bmi


bmi = computeBmi(188, 70)
print("My bmi is ", bmi)
"""
從前面幾個函式的使用，應該可以發現一些命名規則，例如函式名稱的開頭單字是小寫，後面的
單字都只有開頭是大寫，其他都是小寫。

而且，函式名稱大多會使用動詞，可以讓其他人一眼就知道這個函式的作用為何，但這只是習慣而已，
並不保證全部函式都會這麼命名。

而參數或函式當中的變數，都會以底線'_'作為開頭。這是為了方便區分函式內外的變數，避免混淆
的做法。

以下示範函式內使用到函式外的變數的例子，一般即便不使用 global 來宣告 value 為全域變數
也可使用，但函式結束後對全域變數的操作便無效了。

應該是因為我目前是使用 Spyder 的編譯器，變得必須使用 global 。使用 global 的效果便是
在函式內的操作在函式結束後依然有效。
"""
value = 7

def sumValue(_new_value):
     global value
     value += _new_value
     
     print("value:", value)
     

sumValue(3)
sumValue(3)
