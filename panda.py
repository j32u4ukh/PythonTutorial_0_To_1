# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:47:26 2019

@author: j32u4ukh

教學大綱：
1. 建立 DataFrame
2. 根據行數，取出資料
3. 根據欄位，取出資料
4. 迴圈印出日期
5. 資料寫出(rotors.xlsx 和 rotors_status.xlsx)
6. 資料讀入
7. as
8. datetime

9. loc
10. strftime

這次的課程大量地使用到了之前教的 from 和 import ，課程的目標除了讓各位初步認識
pandas 這個套件，還要為最終目標的 Enigma 做些準備。

首先將所需的套件都先引入。雖然需要時再引入也可以，但這樣對於管理與閱讀較為不便，
因此我通常會在最上方就將將所需的套件全部引入。
"""
from datetime import datetime
from datetime import timedelta
from random import shuffle
from random import randint
import pandas as pd

"""
pandas 相當於 Python 裡面的 Excel ，是個很好用的套件。 pandas 後面的 as pd 表示
以下我要用 pd 代表 pandas 的意思，名稱可以自己取，但 pd 已是大家習慣的命名，建議照樣
使用 pd ，這樣互相看到就知道是在指 pandas 。

pandas 要建立表格時會利用 DataFrame ，括弧內利用字典，建立一欄一欄的數據。

注意，每一欄數據的數量要相同才行喔。
"""
df = pd.DataFrame({'column 1':[i for i in range(10)],
                   'column 2':[i for i in range(10, 20)],
                   'column 3':[i for i in range(20, 30)]})

"""
可以利用 print 把整個表格印出來，但當欄位或是行數很多的時候，無法一一看完，可以印出
頭尾幾筆資料，來觀察內容與資料格式。

利用 head 印出最前面幾筆，利用 tail 印出最後面幾筆。括弧內沒給數字時，預設會印出 5 筆
數據，也可以根據需求指定行數。
"""
print(df)
print(df.head())
print(df.head(3))
print(df.tail())
print(df.tail(3))
"""
以下正式開始替 Enigma 做準備，首先，因為這個專案是以三種語言為特色，因此將三種語言的
元素作為範例。

getTaiwanElement()、getJapanElement()、getEnglishElement() 分別將三種語言的元素
加入陣列並回傳。

由於相同語言的 ASCII 基本上都是連續的，因此可以利用 for 迴圈取得他們的 ASCII 
再利用 chr 轉換成字串，這樣就不用一一輸入了。
"""


def getTaiwanElement():
     # ㄅ ASCII: 12549
     # ㄩ ASCII: 12585
     _taiwan_element = [chr(i) for i in range(12549, 12585 + 1)]
     
     # ˊ ASCII: 714
     # ˇ ASCII: 711
     # ˋ ASCII: 715
     # ˙ ASCII: 729          
     punctuation = ["ˊ", "ˇ", "ˋ", "˙"]
     for i in punctuation:
          _taiwan_element.append(i)
          
     return _taiwan_element


def getJapanElement():
     # あ ASCII: 12354
     # ん ASCII: 12435
     _japan_element = [chr(i) for i in range(12354, 12435 + 1)]
     
     return _japan_element
     

def getEnglishElement():
     # a ASCII: 97
     # z ASCII: 122
     _english_element = [chr(i) for i in range(65, 90 + 1)]
     _english_element += [chr(i) for i in range(97, 122 + 1)]
     
     return _english_element


"""
taiwan_element、japan_element、english_element 分別儲存了各自語言的元素，透過 + 將
三個陣列結合，形成 element 。
"""
taiwan_element = getTaiwanElement()
japan_element = getJapanElement()
english_element = getEnglishElement()
element = taiwan_element + japan_element + english_element
"""
shuffleElements 中的 temp 透過 element.copy() 取得，因此 element 本身的順序並沒有
被打亂。每次回傳的都是由原本的 element 的順序去進行打亂。
"""


def shuffleElements(_element):
     temp = _element.copy()
     shuffle(temp)
     return temp


I = shuffleElements(element)
II = shuffleElements(element)
III = shuffleElements(element)
IV = shuffleElements(element)
V = shuffleElements(element)

"""
I, II, III, IV, V 是羅馬數字的一到五，分別代表五個旋轉盤，擁有著"元素相同，但順序
不同"的五個陣列，用於之後存取。

後面將會把這五個陣列記錄下來，未來使用相同旋轉盤與相同狀態去進行加密解密時，才會有
一致的結果。

重新建立一個表格，用來存放接下來的數據。由於現在還沒有數據，因此利用 columns 告訴
pandas 我要建立多少欄位的表格。

若是建立的同時就給予數據， pandas 會自己判斷有多少欄位。
"""
rotor_df = pd.DataFrame(columns=[i for i in range(len(element))])
rotor_df.loc["I"] = I
rotor_df.loc["II"] = II
rotor_df.loc["III"] = III
rotor_df.loc["IV"] = IV
rotor_df.loc["V"] = V

print(rotor_df.head())
print(rotor_df.tail())

"""
這個表格在最後一個課程當中會需要用到，所以這裡利用 to_csv 把它寫成 csv 檔，保存
在電腦中。括弧內寫的是儲存的檔案(相對)路徑。
"""
rotor_df.to_csv("rotors.csv")

"""
之後如果要再使用這個表格，可以利用 read_csv 根據檔案路徑把資料讀進來。

header=0 與 index_col=0 分別代表了橫向第一行是 header (前面說的 columns) 以及
縱向第一行是 index(I, II, III, IV, V)
"""
read_df = pd.read_csv("rotors.csv", header=0, index_col=0)
print(read_df.head())
print(read_df.tail())

"""
除了三種語言的元素，還需要所謂的狀態值，提供 Enigma 的旋轉盤當作參數使用。

旋轉盤的狀態將隨著日期，每天做變動，因此下面這個表格將利用日期作為每一行的名稱。

datetime 是 Python 在處理日期時間方面的套件之一，利用 datetime.today() 可以取得
現在的日期與時間。
"""
today = datetime.today()
print(today)

"""
若直接在 datetime 後面輸入年月日，便可產生指定日期的 datetime 。

我準備透過迴圈建立 2019 年 11 月一整個月的日期，因此先分別建立 11 月 1 日與 
12 月 1 日的 datetime 。
 
datetime 可以加減與筆大小的性質，讓我可以這麼做。
"""
current_date = datetime(2019, 11, 1)
end_date = datetime(2019, 12, 1)

"""
預設為 5 組旋轉盤的狀態，同樣這裡先告訴 pandas 我要建立 NUM 個欄位，如果有需要可以
將 NUM 的數值做修改。
"""
NUM = 5
status_df = pd.DataFrame(columns=[i for i in range(NUM)])

"""
getStatus 根據陣列長度，產生五個隨機數，分別是五個旋轉盤的狀態值。

狀態值的範圍是 0 到 (陣列長度 - 1)，與陣列的索引值範圍相同。
"""


def getStatus(_element_length):
     status = []
     for j in range(NUM):
          rand = randint(0, _element_length - 1)
          status.append(rand)
          
     return status

"""
在 current_date 小於 end_date 之前，持續將 current_date 作為行的名稱，五個旋轉盤
的狀態值 作為數據，加入表格當中。

迴圈最後一行，利用 current_date += timedelta(days=1) 取得"下一天"的日期，一直重複
直到 current_date 超過 11 月，這樣表格就完成了。
"""
element_length = len(element)
while current_date < end_date:
     index = current_date.strftime("%Y-%m-%d")
     status_df.loc[index] = getStatus(element_length)
     current_date += timedelta(days=1)

print(status_df.head())
print(status_df.tail())

status_df.to_csv("rotors_status.csv")

""""""
current_date = datetime(2019, 11, 1)
end_date = datetime(2019, 12, 1)

choose_rotor = pd.DataFrame(columns=[i for i in range(3)])
rotor_num = ['I', 'II', 'III', 'IV', 'V']
while current_date < end_date:
     shuffle(rotor_num)
     index = current_date.strftime("%Y-%m-%d")
     choose_rotor.loc[index] = rotor_num[:3]
     current_date += timedelta(days=1)

print(choose_rotor.head())
print(choose_rotor.tail())

choose_rotor.to_csv("choose_rotor.csv")