# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:44:57 2019

@author: j32u4ukh

教學大綱：
1. for, range
2. while
3. str.format()

這篇主要是要教迴圈的使用，分別為 for 和 while 兩種。這兩種迴圈都是在中止條件前，
重複執行迴圈內的程式碼，但形式略有不同罷了。

for 的中止條件較為明確，而 while 的中止條件可以更為多樣，但若忘記加上中止條件，程式將
不停地執行，進而造成電腦負擔，又被稱為無窮迴圈，請一定要避免這種情況發生喔。

因此我建議，有明確的次數時使用 for 迴圈，若沒有明確次數，而是某些條件符合才執行時
使用 while 迴圈。以下搭配之前教的內容，示範迴圈的使用。
"""
array1 = [1, 2, 3, 4, 5]
for i in array1:
     print(i)
     
"""
上面的 i 將依序到 array1 裡面取值，原本需要 5 行才能把全部印出來，現在 2 行就完成了。

而 while 則需要透過中括號與索引值來取值的方式進行。
"""
i = 0
while i < len(array1):
     print(array1[i])
     
     i += 1
     
"""
while 後面接的是終止條件，也就是索引值小於長度值之前，重複印出陣列中第 i 個值。

緊接在印出的程式碼後面， i += 1 讓索引值每次加一，下次執行時印出的便會是下一個值，
隨著索引值每次加一，最終將與長度值相等，並結束這個迴圈。

如果不知道為什麼"索引值小於長度值之前"才要印出的話，可以複習前面在教陣列的內容喔，
以下示範其他應用的 for 和 while 迴圈。
"""
print("for loop")
array2 = ['あ', 'い', 'う', 'え', 'お']
for i in array2:
     print(i)
 
print("while loop")
i = 0
while i < len(array2):
     print(array2[i])
     
     i += 1
     
"""
如果 for 迴圈也想根據索引值去取出陣列中的值，想必會需要有個東西，依序取出時會是
[0, 1, 2, 3, 4]，那就是 range(5)。

range(5) 表示從 0 開始，到 5 為止(不包含)，每次加一，相當於 range(0, 5) 或
range(0, 5, 1)。只有一個值時，預設第一個值為 0 ，且第三個值為 1；
兩個值時，預設第三個值為 1。

如果想從 1 開始，到 5 為止(不包含)，每次加二，則寫成 range(1, 5, 2)。
"""
for i in range(5):
     print(array2[i])
     
for i in range(0, 5, 1):
     print(array2[i])
     
for i in range(1, 5, 2):
     print(array2[i])

"""
迴圈搭配字串格式化等，便可印出連續變化的字串等，不需要一個一個打。

字串格式化可利用 {} 與 format() ，依序將數值放入即可。

若只是要印出，更可透過逗號 "," 將內容依序排列即可。
"""
num = 0
for i in range(1, 6):
     print("i = ", i)
     num += i
     print("loop {}: num = {}".format(i, num))
     
"""
字串可透過 * 號，乘上次數，形成多個字串連接的單一字串。搭配迴圈可印出一些有趣的圖案。
"""
for i in range(1, 6):
     print("*" * i)
     
"""
陣列也經常使用迴圈去新增或讀取。
"""
array3 = []
for i in range(5):
     array3.append(i)
     
for i in range(5):
     print(array3[i])
     
print(array3)