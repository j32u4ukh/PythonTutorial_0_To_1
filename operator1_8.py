# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 22:46:08 2019

@author: j32u4ukh

教學大綱：
1. if else
2. elif
"""

"""
這裡要介紹條件判斷的用法，白話來說就是執行：判斷是否正確，正確的話做什麼，不正確的話做什麼。

if 後面接了條件句，條件句的結果是 True 或 False 這兩種邏輯型的資料。
"""
if True:  # if 條件
     print("I'm smart.")  # 正確的話做什麼
else:  # 否則
     print("It is impossible.")
     
"""
如果像前面的範例，在條件的部分直接寫 True，這麼做的意義不大，我們可以用來檢查一個字串長度是否超過 5。
"""
string = "Hello World"
if len(string) > 5:
     print("Length is longer than 5.")
else:
     print("Length is shorter than 5.")
     
string = "Hello"
if len(string) > 5:
     print("Length is longer than 5.")
else:
     print("Length is shorter than 5.")
     
"""
從這兩個範例，可以看到條件判斷都相同，輸入不同的字串就有了不同的結果。

if else 將情況做了二分法，只有是或不是，在實際使用上也會出現三種(或以上)情況的時候，
若只有 if else 就必須寫兩層  if else，實在不太方便，因此可以使用 elif，在第一個 if
判斷完之後繼續判斷，全部條件都不符合後才執行 else 裡面的內容。

下面兩種寫法等價，但使用 elif 可讓程式碼較簡潔。
"""
number = 3

if number == 1:
     print("number is 1.")
else:
     if number == 2:
          print("number is 2.")
     else:
          if number == 3:
               print("number is 3.")
          else:
               if number == 4:
                    print("number is 4.")
               else:
                    print("number is 5.")

 
if number == 1:
     print("number is 1.")
elif number == 2:
     print("number is 2.")
elif number == 3:
     print("number is 3.")
elif number == 4:
     print("number is 4.")
else:
     print("number is 5.")
