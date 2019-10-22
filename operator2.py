# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:44:11 2019

@author: j32u4ukh

教學大綱：
1. ord()
2. chr()
3. int()
4. float()

這裡要介紹 ASCII 碼與文字符號之間的轉換，ASCII 碼簡單來說就是為了讓電腦理解，因此
用一串數字去表示許多文字或符號，至於精確地說明就請自行上網找來看吧。

利用 ord() 將文字符號轉換成 ASCII 碼；chr()則可將 ASCII 碼轉換回文字符號。兩者是可以
互相轉換的關係。
"""
print(ord('a'))  # 97
print(chr(97))   # a

print(ord('z'))          # 122
print(chr(97 + 26 - 1))  # z

"""
說個題外話，在前面的教學曾經教過利用"/"進行除法，以及利用"%"取得餘數，這裡要介紹如何
取得商數。

實際執行 5 / 2 你會得到 2.5 而非 2；若是 7 / 2 會得到 3.5 而非 3。

但都可以觀察到，商數就是答案的整數部分，若能只取得整數部分，那就達到目的了，
此時就是要使用 int()。
"""
ans = 5 / 2
print(ans)       # 2.5
print(int(ans))  # 2

ans = 7 / 2
print(ans)       # 3.5
print(int(ans))  # 3

"""
int() 可以忽略小數點，返回整數的部分。另一方面， float() 則可將正數變成浮點數。

實際上， int() 和 float() 也可以將字串形式的數值，分別變成整數和浮點數呢。
"""
num1 = 9
print(num1)         # 9
print(float(num1))  # 9.0

num2 = "11"
print(int(num2))    # 11
print(float(num2))  # 11.0

num3 = "9.8"
# print(int(num3)) 是不行的喔
print(float(num3))  # 11.0

"""
哪些形式的內容可以變成你所需要的值，其實不急著在現在全部都了解，
遇到那些需求時再去了解就可以了。
"""