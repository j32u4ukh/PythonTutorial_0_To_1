# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:43:20 2019

@author: j32u4ukh

教學大綱：
1. array
2. append()
3. sort()
4. copy()
5. 索引值
6. id()
"""
"""
這裡要介紹的是"陣列 array"，包含建立、添加、排序與複製。

"陣列 array"是由一連串順序性的元素組成，元素可以都相同(都是整數)，
也可以不相同，整數和字串交雜，甚至放另一個陣列進去也可以。

陣列的元素由中括弧所包住，逗號分隔每一個元素，以下示範建立。
"""
array1 = [1, 2, 3]
array2 = [1, "one", 2, "二", 3, [1, 2, 3]]
print(array1)
print(array2)

"""
建立了"陣列 array"之後，還可以透過 append() 添加新的元素進去。
"""
array1.append(4)
print(array1)

"""
有了 append() 添加元素，一開始建立"陣列 array"的時候也可以是空的，事後再將元素加進去。
"""
array3 = []
array3.append(3)
array3.append(1)
array3.append(2)
print(array3)

"""
array1 和 array3 的元素都是 1, 2, 3 只是順序不一樣，若我們想讓它由小排到大，
可以利用 sort()，請看以下示範。
"""
array3.sort()
print(array1)
print(array3)

"""
可以看到在 array3.sort() 之後，array3 的順序也變成由小排到大。如果我只想排序之後
做一些操作，並不想該改到原本的陣列的話，就要透過 copy()。
"""
array4 = [3, 1, 2]
array5 = array4.copy()
array5.sort()
print(array4)
print(array5)

"""
如果你覺得一樣是給陣列 [3, 1, 2] 的值，為何不直接 array5 = array4 就好了呢？

這裡順便介紹一下，如何讀取、修改陣列中的特定值。可利用 陣列[索引值] 讀取或修改，
索引值從 0 開始計算，長度為 3 的陣列，索引值依序為 0, 1, 2。
"""
# 讀取
print(array4[0])
print(array4[1])
print(array4[2])

# 修改
array4[0] = 4
array4[1] = 5
array4[2] = 6
print(array4)

"""
現在可以正式開始示範，為何不直接 array5 = array4 就好了呢？
讓我們在 array5 = array4 之後，修改 array5 裡面的值，看看分別對
array4 和 array5 有何影響？
"""
array5 = array4
array5[1] = 7
print(array4)
print(array5)

"""
改了 array5 裡面的值， array4 的值也跟著一起改變了。這是因為 array5 = array4
的本質上，是讓 array5 去連結到和 array4 所對應的"記憶體位置"，也就是他們是同一個陣列。

我們可以利用 id() 去查詢變數的"記憶體位置"，更清楚的了解"array5 = array4 後的
array4 和 array5 是同一個陣列"這件事。

而前面使用的 copy() 則是在不同的"記憶體位置"複製一份相同數值的陣列。
"""
print(id(array4))
print(id(array5))

array6 = array4.copy()
print(id(array6))

array6[1] = 5
print(array4)
print(array6)
