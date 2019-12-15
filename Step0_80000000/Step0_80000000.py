# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:47:26 2019

@author: j32u4ukh

教學大綱；シラバス；syllabus：
1. 建立 DataFrame； DataFrame を確立する
2. 根據行數，取出資料；行のインデックスによて資料を読むこと
3. 根據欄位，取出資料；列のインデックスによて資料を読むこと
4. 迴圈印出日期；ループで日付(ひづけ)をプリントアウト
5. 資料寫出(rotors.xlsx ＆ rotors_status.xlsx)；資料を書き出します
6. 資料讀入；資料を読みます
7. as
8. datetime
9. loc
10. strftime

這次的課程大量地使用到了之前教的 from 和 import ，課程的目標除了讓各位初步認識
pandas 這個套件，還要為最終目標的 Enigma 做些準備。
今回のチュートリアルは教えた from と import 大量(たいりょう)な使って、目的が皆に
pandas というのパッケージを簡単な了解する、そして、最後の目標 Enigma に準備する。

＝＝＝＝＝
首先將所需的套件都先引入。雖然需要時再引入也可以，但這樣對於管理與閱讀較為不便，
因此我通常會在最上方就將所需的套件全部引入。
先ずは必要なパッケージを全部インポートする。本当に必要な時にインポートしてもいいけど、
インポートの管理とコードの読むことに不便だ。だから、通常(つうじょう)自分は最も上の
所にパッケージを全部インポートする。
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
pandas は Excel にとして Python の中に使われる、とてもべんりなパッケージ。pandas の
うしろの’ as pd ’の意味は’これから pd として pandas ’。その名前は自分で命名すろこと
ができる、だが、 pd に呼ばれるは皆の習慣になった。昔のような pd に呼ばれて続いて、
それなら見ればわかる。

＝＝＝＝＝
pandas 要建立表格時會利用 DataFrame ，括弧內利用字典，建立一欄一欄的數據。
pandas でフォームを構築(こうちく)するとき、 DataFrame を利用して、丸括弧の中に辞書
を入れって、一つ列一つ列でデータを構築する。

＝＝＝＝＝
注意，每一欄數據的數量要相同才行喔。
注意！各(かく)列データの数量は同じべきだ。
"""
df = pd.DataFrame({'column 1': [i for i in range(10)],
                   'column 2': [i for i in range(10, 20)],
                   'column 3': [i for i in range(20, 30)]})

"""
可以利用 print 把整個表格印出來，但當欄位或是行數很多的時候，無法一一看完，可以印出
頭尾幾筆資料，來觀察內容與資料格式。
フォーム全体をプリントアウトする、だが、行と列の数量が多い場合、一つ一つに見ることが
できない。最初と最後のデータをプリントアウトして、内容とデータ形式を観察(かんさつ)
する。

＝＝＝＝＝
利用 head 印出最前面幾筆，利用 tail 印出最後面幾筆。括弧內沒給數字時，預設會印出 5 筆
數據，也可以根據需求指定行數。
head() で最初数個(すうこ)データをプリントアウトして、tail() で最初数個データ
をプリントアウトする。丸括弧の中に行の数量を入れって、何も入れないの場合が 5 行を
プリントアウトする。
"""
print(df)
print(df.head())
print(df.head(3))
print(df.tail())
print(df.tail(3))
"""
以下正式開始替 Enigma 做準備，首先，因為這個專案是以三種語言為特色，因此將三種語言的
元素作為範例。
これから正式(せいしき)な Enigma に準備している。先ず、このプロジェクトは三つ
言語(げんご)を特徴(とくちょう)として。だから、三つ言語の要素を例として紹介する。

＝＝＝＝＝
getTaiwanElement()、getJapanElement()、getEnglishElement() 分別將三種語言的元素
加入陣列並回傳。
getTaiwanElement() と getJapanElement() と getEnglishElement() それぞれ三つ
言語の要素を配列に追加して結果を戻る(もどる)。

＝＝＝＝＝
由於相同語言的 ASCII 基本上都是連續的，因此可以利用 for 迴圈取得他們的 ASCII 
再利用 chr 轉換成字串，這樣就不用一一輸入了。
基本的に、同じ言語の ASCII は連続的(れんぞくてき)、だから、 for ループを利用して
ASCII を入手(にゅうしゅ)して、 chr で紐になると、一つずつ入力(にゅうりょく)必要
がない。
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
taiwan_element と japan_element と english_element それぞれ三つの言語の要素を
収納(しゅうのう)して、たす記号を使って、三つの配列を組み合わせて、 element になる。
"""
taiwan_element = getTaiwanElement()
japan_element = getJapanElement()
english_element = getEnglishElement()
element = taiwan_element + japan_element + english_element
"""
shuffleElements 中的 temp 透過 element.copy() 取得，因此 element 本身的順序並沒有
被打亂。每次回傳的都是由原本的 element 的順序去進行打亂。
shuffleElements の中の temp は element.copy() でもらったので、 element の順番が
混乱(こんらん)されない。毎回戻って配列は最初の順番から混乱される。
"""


def shuffleElements(_element):
    temp = _element.copy()
    shuffle(temp)
    return temp


"""
I, II, III, IV, V 是羅馬數字的一到五，分別代表五個旋轉盤，擁有著"元素相同，但順序
不同"的五個陣列，用於之後存取。
I, II, III, IV, V はローマ数字の一から五まで、読むことのため五つスクランブラーそれ
ぞれ五つ”同じ要素、違う順番の配列”を代表(だいひょう)する。

＝＝＝＝＝
後面將會把這五個陣列記錄下來，未來使用相同旋轉盤與相同狀態去進行加密解密時，才會有
一致的結果。
これから五つ配列を記録して、将来同じスクランブラーと状態を使って暗号化と解読している
とき、同じ結果をもらう。
"""
I = shuffleElements(element)
II = shuffleElements(element)
III = shuffleElements(element)
IV = shuffleElements(element)
V = shuffleElements(element)

"""
重新建立一個表格，用來存放接下來的數據。由於現在還沒有數據，因此在 DataFrame 當中利用
 columns 事先建立所需欄位，若是建立的同時就給予數據， pandas 會自己判斷有多少欄位。
データを入れってため、新しいフォームを構築(こうちく)する。今はまだデータがいないので、
columns を使って事前(じぜん)に列を設立(せつりつ)。もし構築しているとき、データもう
ありますなら、 pandas が自分で列の数量を判断する。

＝＝＝＝＝
.loc 後面使用中括弧將該行的名稱包起來，新增或讀取都是利用這個方式。
.loc の後ろ角括弧(かくがっこ)で列の名前を取り囲んで、追加と読むもこの方法を利用する。
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
このフォームは最後のチュートリアルの時に使われるので、ここで to_csv を利用して csv 
のファイルになる、コンピューターに収納する。丸括弧の中にはファイルの(相対(そうたい))
パス。
"""
rotor_df.to_csv("rotors.csv")

"""
之後如果要再使用這個表格，可以利用 read_csv 根據檔案路徑把資料讀進來。
将来もう一度このフォームを利用したいなら、 read_csv でファイルのパスによると、データ
を読みます。

＝＝＝＝＝
header=0 與 index_col=0 分別代表了橫向第一行是 header (前面說的 columns) 以及
縱向第一行是 index(I, II, III, IV, V)
header=0 と index_col=0 それぞれ”横方向第一行は header (前の columns)と縦方向
第一行は index(I, II, III, IV, V)”。
"""
read_df = pd.read_csv("rotors.csv", header=0, index_col=0)
print(read_df.head())
print(read_df.tail())

"""
除了三種語言的元素，還需要所謂的狀態值，提供 Enigma 的旋轉盤當作參數使用。
三つ言語の上で、スクランブラーの状態値も必要だ。 Enigma のスクランブラーのパラメータ
として使います。

＝＝＝＝＝
旋轉盤的狀態將隨著日期，每天做變動，因此下面這個表格將利用日期作為每一行的名稱。
日付(ひづけ)によるとスクランブラーの状態値は毎日変えます。だから、下のフォームは
日付を利用して行の名前になる。

＝＝＝＝＝
datetime 是 Python 在處理日期時間方面的套件之一，利用 datetime.today() 可以取得
現在的日期與時間。
datetime は Python のパッケージの一つ、日付と時間の問題に対処する。
datetime.today() を利用して、今の日付と時間をもらう。
"""
today = datetime.today()
print(today)

"""
若直接在 datetime 後面輸入年月日，便可產生指定日期的 datetime 。
datetime の後ろに日付を直接的に輸入したら、特定日付の datetime をもらう。

＝＝＝＝＝
我準備透過迴圈建立 2019 年 11 月一整個月的日期，因此先分別建立 11 月 1 日與 
12 月 1 日的 datetime 。
これからループで 2019 年 11 月一か月の日付を構築しての予定ので、先ずはそれぞれ 
11 月 1 日と 12 月 1 日の datetime を構築する。

＝＝＝＝＝
datetime 可以加減與比較大小的性質，讓我可以這麼做。
datetime は計算できると比較できるの性質(せいしつ)によて、後ろのことができます。
"""
current_date = datetime(2019, 11, 1)
end_date = datetime(2019, 12, 1)

"""
預設為 5 組旋轉盤的狀態，同樣這裡先告訴 pandas 我要建立 NUM 個欄位，如果有需要可以
將 NUM 的數值做修改。
デフォルトのスクランブラー数量は NUM 個、 pandas で NUM 列を構築して。NUM の数値が 
5 、必要ならこの数値を変えて大丈夫です。
"""
NUM = 5
status_df = pd.DataFrame(columns=[i for i in range(NUM)])


def getStatus(_element_length):
    status = []
    for j in range(NUM):
        rand = randint(0, _element_length - 1)
        status.append(rand)

    return status


"""
getStatus 根據陣列長度，產生五個隨機數，分別是五個旋轉盤的狀態值。
getStatus は配列の長さによて、五つ乱数(らんすう)を生成(せいせい)する。それぞれ五つ
スクランブラーの状態(じょうたい)値です。

＝＝＝＝＝
狀態值的範圍是 0 到 (陣列長度 - 1)，與陣列的索引值範圍相同。
状態値の範囲(じょうたい)はゼロから”配列の長さ引く一”、配列のインデックスの範囲と同じ。

＝＝＝＝＝
在 current_date 小於 end_date 之前，持續將 current_date 作為行的名稱，五個旋轉盤
的狀態值 作為數據，加入表格當中。
current_date は end_date より小さい前、 current_date が行の名前として、五つ
スクランブラーの状態値をデータとしてフォームに追加することを繰り返します。

＝＝＝＝＝
迴圈最後一行，利用 current_date += timedelta(days=1) 取得"下一天"的日期，一直重複
直到 current_date 超過 11 月，這樣表格就完成了。
ループの最後一部分は current_date += timedelta(days=1) を利用して、明日の日付を
もらって、 current_date が 11 月越える(こえる)前に繰り返します。

＝＝＝＝＝
current_date.strftime("%Y-%m-%d") 將 current_date 的時間格式化成"年-月-日"的
形式，之後利用日期讀取時，也利用相同方式把日期格式化，不需要去考慮時分秒等數值。
current_date.strftime("%Y-%m-%d") で current_date の時間をフォーマットして
”年-月-日”の形式(けいしき)になる。将来日付利用して読むとき、同じ方法を利用すればいい。
時、分、秒の数値なら考えて必要はないだ。
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