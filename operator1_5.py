# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 23:12:28 2019

@author: j32u4ukh

教學大綱：
1. True, False
2. and, or, not
"""

"""
True 和 False 是邏輯型的資料，正確或不正確，成立或不成立，相等或不相等，以此類推。
"""
print(2 > 1)  # True
print(2 < 1)  # False

"""
True 和 False 之間互相組合，可以產生許多變化。組合則是透過 and, or, not 等來達到。

and: 都是 True 才會是 True。
"""
print(True and True)    # True
print(True and False)   # False
print(False and False)  # False

"""
or: 其中一個 True 就會是 True。
"""
print(True or True)    # True
print(True or False)   # True
print(False or False)  # False

"""
not:True → False, False → True。
"""
print(not True)    # False
print(not False)   # True
