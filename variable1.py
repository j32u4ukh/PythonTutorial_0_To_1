# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:39:37 2019

@author: j32u4ukh

教學大綱：
1. int
2. float
3. str
4. variable
5. type()
"""

"""
變數還有其他類型，但現在先教各位會需要使用的就可以了。

首先是整數 int，如：1, 2, 3, 9527, ...
"""
print(1)
print(2)
print(3)
print(9527)

"""
字串 str，之前的教學也提過，這裡就快速帶過。
"""

"""
浮點數 float，也就是帶有小數點的數字
"""
print(2.71828)
print(3.14159)
print(9.0)

"""
前面提的整數或字串，可以利用"變數"代替，方便我們重複使用。

這個過程叫做"賦值"，將"右邊"的值給予"左邊"的變數，之後還會提到，請記得"賦值"的意思。
"""
t0 = 1
t1 = "字串"
t2 = 2.71828
j0 = 2
j1 = "さしすせそ"
j2 = 3.14159

print(t0)  # 1
print(t1)  # 字串
print(t2)  # 2.71828
print(j0)  # 2
print(j1)  # さしすせそ
print(j2)  # 3.14159

"""
當我們將整數、浮點數或字串存到變數裡面之後，我怎麼知道它是整數、浮點數還是字串呢？

可利用 type()，查看變數是屬於哪種類型喔。

<class 'int'>表示它屬於整數；<class 'str'>表示它屬於字串；<class 'float'>表示它屬於浮點數。
"""
print(type(1))      # <class 'int'>
print(type(j0))     # <class 'int'>

print(type("字串")) # <class 'str'>
print(type(j1))     # <class 'str'>

print(type(2.7182)) # <class 'float'>
print(type(j2))     # <class 'float'>
