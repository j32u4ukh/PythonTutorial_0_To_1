# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 22:44:14 2019

@author: j32u4ukh

教學大綱：
1. dict 建立
2. dict 取值
3. dict 新增

除了陣列之外，還有一種基本的資料儲存方式，叫做'字典'。透過 {key1:value1, 
key2:value2} 的形式來組成。

就像字典透過單字去查找單字的解釋一樣， Python 的字典透過 key 去取得它所代表的 value 。

字典的建立是透過大括弧將內容包起來，先輸入 key 然後冒號後面接著它所代表的 value ，這
是一組資料，要建立第二組時，一樣透過逗號將它們分開。
"""
d1 = {'a':1, 'b':2, 'c':3}
d2 = {1:'a', 2:'b', 3:'c'}
d3 = {'a':[1, 2, 3], 
      'b':{"w":"up", "s":"down", "a":"left", "d":"right"}
      }
"""
從上面的示範中可以知道， key 可以是字串或數字，而 value 基本上各種資料都可以放進去，
甚至是在字典當中，放入另一個字典。

當我們想取出字典中的值(value)時，有兩種方法，第一種是像陣列，在字典變數名稱後面加上
中括弧，括弧當中放入要取出的值的 key 。因為是 key ，所以也就不是從 0 開始計算了。

另一種則是透過 get 去取得，這種方式較為安全。因為當我們透過中括弧去取出一個不在字典
當中的值時就會產生錯誤，但若是透過 get 去取得則只是返回 None ，不影響程式繼續執行。
"""
print(d1['a'])
print(d2[1])
try:
     print(d3['c'])
except KeyError:
     print("""c 並不在 d3 的 key 當中。
c は d3 の key の中にありません。
c is not in the keys of d3.""")
     
print(d1.get('b'))
print(d2.get(4))
d3_b = d3.get('b')
print(d3_b)
print(d3.get('c'))

"""
當我們想要往字典當中新增 key-value 的時候，可以透過中括弧把 key 包住，讓它等於你所
希望賦予的值。

這點和陣列也是十分不同，陣列這樣做的話可是會報錯的。
"""
print(d1)
d1['d'] = 4
print(d1)
