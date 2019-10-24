# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:47:12 2019

@author: j32u4ukh

教學大綱：
1. 預設值
2. assert
3. *args

之前提到函式可以透過參數執行'大部分相同，只有些許部分不同'的內容，這次要對參數做
進一步的介紹。

函式的參數可以事先給予值，如果這個數值適用我們當下的情形時，可以省略不給予值。

若想修改值，就和原本教的一樣，給予想要的數值即可。
"""
def computeMultiply(_value, _multiply=2):     
     return _value * _multiply


value = 3
value = computeMultiply(value)  # 6 = 3 * 2
print(value)
value = computeMultiply(value)  # 12 = 6 * 2
print(value)
value = computeMultiply(value, 5)  # 60
print(value)
"""
我們除了可以根據參數去執行函式之外，還可以對這些參數設定一些要求與限制。

例如做正整數除法時，利用 assert 限制分母一定要大於 0，當不符合限制時，
會產生 AssertionError，並回饋給使用者逗號後面的資訊。
"""


def divide(_numerator, _denominator):
     assert _denominator > 0, "分母一定要大於 0"
     
     return _numerator / _denominator


print(divide(5, -2))
print(divide(5, 2))
"""
最後，如果我們在規劃函式的時候不確定會有幾個參數，在參數的地方利用 *args 表示
不定數量參數是個好方法，函式內部使用時，則不需要米字號。


"""
def getSum(*args):
     _sum = 0
     for i in args:
          _sum += i
          
     return _sum


print(getSum(1, 2, 3, 4, 5))
print(getSum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))