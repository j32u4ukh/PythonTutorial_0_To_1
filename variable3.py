# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:40:42 2019

@author: j32u4ukh

教學大綱：
1. 十進制
2. 二進制
3. 二進制應用
"""

"""
一般我們所在使用的數字就是"十進制"，應該很好理解，數字為 0~9，超過 9 就會進位變成 10。

而"二進制"是電腦的進位方式，數字為 0~1，超過 1 就會進位變成 10，通常會 8 位或 16 位一起寫。

例：左邊十進制，右邊二進制
0  → 00000000
1  → 00000001
2  → 00000010
3  → 00000011
4  → 00000100
...
10 → 00001010
11 → 00001011

透過Python 內建方法可輕鬆的進行十進制和二進制兩者的轉換。
"""
decimal = 11
binary = "1011"
# 十進制 → 二進制
print(bin(decimal))

# 二進制 → 十進制
print(int(binary, 2))

"""
接著是本篇的重點，二進制應用。在這個專案的利用上是判斷奇偶。

判斷奇偶可也可用之前教的"%"，但利用二進制的性質，可以更有效率的進行。

11 → 00001011
1  → 00000001
"""
odd = 11
even = 12

# %
if odd % 2 == 0:
     print("偶數")
else:
     print("奇數")
     
if even % 2 == 0:
     print("偶數")
else:
     print("奇數")
     
# 二進制應用
if odd and 1 == 0:
     print("偶數")
else:
     print("奇數")
     
if even and 1 == 0:
     print("偶數")
else:
     print("奇數")