# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 21:49:38 2019

@author: j32u4ukh

教學大綱：
1. break
2. continue

之前在教迴圈的時候提到，for 和 while 會重複執行迴圈內的程式碼，
直到達成中止條件，這次要教的 break 和 continue 能讓我們在使用迴圈時更加的彈性。

中止條件是在一開始就設定好，倘若在迴圈執行的過程中，達到了其他的中止條件，希望直接
停止迴圈時，便可使用 break ，中途停止迴圈。

例如：迴圈的中止條件為變數 i 大於等於 0 小於 10，但如果變數 i 可以被 7 整除
且大於 0，那就停止迴圈。像這種複合條件，就會需要使用之前教的 and, or 來連接。
"""
for i in range(10):
     print("for i:", i)
     
     if i % 7 == 0 and i != 0:
          break
print("=" * 10)

i = 0
while i < 10:
     print("while i:", i)
     if i % 7 == 0 and i != 0:
          break
     
     i += 1

"""
另一方面，倘若在迴圈執行的過程中，某個條件下不執行，但其他仍照樣執行，則需使用
 continue。

例如：印出大於等於 0 小於 10 的奇數。這個例子不使用 continue 也可以做到，我將兩個
版本都寫出來，讓各位比較一下，先不使用 continue ，之後再使用 continue 。
"""
# no continue
for i in range(10):
     # 注意差異
     if i & 1 != 0:
          print("for i:", i)
          
print("="*10)
i = 0
while i < 10:
     # 注意差異
     if i & 1 != 0:
          print("while i:", i)
     i += 1
     
# with continue
for i in range(10):
     # 注意差異
     if i & 1 == 0:
          continue
     print("for i:", i)
          
print("="*10)
# 注意差異
i = -1
while i < 10:
     i += 1
     
     # 注意差異
     if i & 1 == 0:
          continue
     print("while i:", i)
     