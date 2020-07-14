# 教學大綱；シラバス；syllabus：

1. 建立 DataFrame；DataFrame を確立する; build DataFrame
2. 根據行數，取出資料；行のインデックスによて資料を読むこと; fetch data according to row's number
3. 根據欄位，取出資料；列のインデックスによて資料を読むこと; fetch data according to column's number
4. 迴圈印出日期；ループで<ruby>日付<rt>ひづけ</rt><ruby>をプリントアウト; print date time by loop
5. 資料寫出(rotors.xlsx ＆ rotors_status.xlsx)；資料を書き出します; output data as a file
6. 資料讀入；資料を読みます; fetch data from a file
7. as
8. datetime
9. loc
10. strftime

這次的課程大量地使用到了之前教的 from 和 import ，課程的目標除了讓各位初步認識 pandas 這個套件，還要為最終目標的 Enigma 做些準備。

今回のチュートリアルは教えた from と import <ruby>大量<rt>たいりょう</rt><ruby>な使って、目的が皆 pandas というのパッケージを簡単な了解する、そして、最後の目標 Enigma に準備する。

This course uses a lot of "from" and "import" previously taught. The goal of the course is not only to give you a preliminary understanding of the pandas package, but also to prepare for the final goal of Enigma.

---

首先將所需的套件都先引入。

先ずは必要なパッケージを全部インポートする。

First, import all packages that we need.

---

雖然需要時再引入也可以，但這樣對於管理與閱讀較為不便。

本当に必要な時にインポートしてもいいけど、インポートの管理とコードの読むことに不便だ。

Although we can import the package if necessary, it is more inconvenient for management and reading.

---

因此我通常會在最上方就將所需的套件全部引入。

だから、<ruby>通常<rt>つうじょう</rt><ruby>自分は最も上の所にパッケージを全部インポートする。

Therefore, I usually import all the required packages at the top.

```python
from datetime import datetime
from datetime import timedelta
from random import shuffle
from random import randint
import pandas as pd
```

pandas 相當於 Python 裡面的 Excel ，是個很好用的套件。 

pandas は Excel にとして Python の中に使われる、とてもべんりなパッケージ。

"Pandas" is a very useful package as Excel in Python.

---

pandas 後面的 as pd 表示以下我要用 pd 代表 pandas 的意思。

pandas のうしろの "as pd" の意味は "これから pd として pandas"’。

"as pd" after pandas means that I will use pd to mean pandas.

---

名稱可以自己取，但 pd 已是大家習慣的命名。

その名前は自分で命名すろことができる、だが、 pd に呼ばれるは皆の習慣になった。

The name can be taken by yourself, but pd is already a common name for everyone.

---

建議照樣使用 pd ，這樣互相看到就知道是在指 pandas 。

昔のような pd に呼ばれて続いて、それなら見ればわかる。

It is recommended to use pd as usual, so that when you see other's code, you will know that it is referring to pandas.

---

pandas 要建立表格時會利用 DataFrame ，括弧內利用字典，建立一欄一欄的數據。

pandas でフォームを<ruby>構築<rt>こうちく</rt></ruby>するとき、 DataFrame を利用して、丸括弧の中に辞書を入れって、一つ列一つ列でデータを構築する。

Pandas will use DataFrame to build a table, and put a dictionary into parentheses to create data column-by-column.

---

注意，每一欄數據的數量要相同才行喔。

注意！<ruby>各<rt>かく</rt></ruby>列データの数量は同じべきだ。

Note that the amount of data in each column must be the same.

```python
df = pd.DataFrame({'column 1': [i for i in range(10)],
                   'column 2': [i for i in range(10, 20)],
                   'column 3': [i for i in range(20, 30)]})
```

可以利用 print 把整個表格印出來，但當欄位或是行數很多的時候，無法一一看完。

フォーム全体をプリントアウトする、だが、行と列の数量が多い場合、一つ一つに見ることができない。

You can use print to print out the entire table, but when there are many columns or rows, you are not able to read each of them.

---

可以印出頭尾幾筆資料，來觀察內容與資料格式。

最初と最後のデータをプリントアウトして、内容とデータ形式を<ruby>観察<rt>かんさつ</rt></ruby>する。

You can print a few head or tail data to observe the content and data format.

---

利用 head 印出最前面幾筆，利用 tail 印出最後面幾筆。

head() で最初<ruby>数個<rt>すうこ</rt></ruby>データをプリントアウトして、tail() で最初数個データをプリントアウトする。

Use head function to print the first few data, and use tail function to print the last few data.

---

括弧內沒給數字時，預設會印出 5 筆數據，也可以根據需求指定行數。

丸括弧の中に行の数量を入れって、何も入れないの場合が 5 行をプリントアウトする。

When no numbers are given in parentheses, 5 data will be printed out by default, and the number of lines can also be specified as required.

```python
print(df)
print(df.head())
print(df.head(3))
print(df.tail())
print(df.tail(3))
```

以下正式開始替 Enigma 做準備。

これから<ruby>正式<rt>せいしき</rt></ruby>な Enigma に準備している。

The following officially started preparing for Enigma.

---

首先，因為這個專案是以三種語言為特色，因此將三種語言的元素作為範例。

先ず、このプロジェクトは三つ<ruby>言語<rt>げんご</rt></ruby>を<ruby>特徴<rt>とくちょう</rt></ruby>として。だから、三つ言語の要素を例として紹介する。

First, this project features three languages, so the elements of the three languages are used as examples.

---

getTaiwanElement()、getJapanElement()、getEnglishElement() 分別將三種語言的元素加入陣列並回傳。

getTaiwanElement() と getJapanElement() と getEnglishElement() それぞれ三つ言語の要素を配列に追加して結果を<ruby>戻<rt>もど</rt></ruby>る。

getTaiwanElement()、getJapanElement()、getEnglishElement() will add the elements of three languages to the array and return them separately.

---

由於相同語言的 ASCII 基本上都是連續的。

基本的に、同じ言語の ASCII は<ruby>連続的<rt>れんぞくてき</rt></ruby>。

Because ASCII in the same language is basically continuous.

---

因此可以利用 for 迴圈取得他們的 ASCII 再利用 chr 轉換成字串，這樣就不用一一輸入了。

だから、 for ループを利用してASCII を<ruby>入手<rt>にゅうしゅ</rt></ruby>して、 chr で紐になると、一つずつ<ruby>入力<rt>にゅうりょく</rt></ruby>必要がない。

So we can use for loop to get their ASCII and then use chr function to convert to string, without to enter them one by one.

```
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
```

taiwan_element、japan_element、english_element 分別儲存了各自語言的元素，透過 + 將三個陣列結合，形成 element 。

taiwan_element と japan_element と english_element それぞれ三つの言語の要素を<ruby>収納<rt>しゅうのう</rt></ruby>して、たす記号を使って、三つの配列を組み合わせて、 element になる。

taiwan_element, japan_element, and english_element respectively store the elements of their respective languages. We will combine the three arrays through + to form "element".

```python
taiwan_element = getTaiwanElement()
japan_element = getJapanElement()
english_element = getEnglishElement()
element = taiwan_element + japan_element + english_element
```

shuffleElements 中的 temp 透過 element.copy() 取得，因此 element 本身的順序並沒有被打亂。每次回傳的都是由原本的 element 的順序去進行打亂。

shuffleElements の中の temp は element.copy() でもらったので、 element の順番が<ruby>混乱<rt>こんらん</rt></ruby>されない。毎回戻って配列は最初の順番から混乱される。

The temp in shuffleElements is obtained through element.copy(), so the order of element itself is not disturbed. Each time it is sent back, the original element sequence is used to disrupt it.

```python
def shuffleElements(_element):
    temp = _element.copy()
    shuffle(temp)
    return temp
```

I, II, III, IV, V 是羅馬數字的一到五，分別代表五個旋轉盤，擁有著"元素相同，但順序不同"的五個陣列，用於之後存取。

I, II, III, IV, V はローマ数字の一から五まで、読むことのため五つスクランブラーそれぞれ五つ”同じ要素、違う順番の配列”を<ruby>代表<rt>だいひょう</rt></ruby>する。

I, II, III, IV, V are one to five Roman numerals, representing five rotators, respectively, with five arrays of "same elements, but different order" for later access.

---

後面將會把這五個陣列記錄下來，未來使用相同旋轉盤與相同狀態去進行加密解密時，才會有一致的結果。

これから五つ配列を記録して、将来同じスクランブラーと状態を使って暗号化と解読しているとき、同じ結果をもらう。

These five arrays will be recorded later, and when same rotators and the same state are used for encryption and decryption in the future, there will be consistent results.

```python
I = shuffleElements(element)
II = shuffleElements(element)
III = shuffleElements(element)
IV = shuffleElements(element)
V = shuffleElements(element)
```

重新建立一個表格，用來存放接下來的數據。

データを入れってため、新しいフォームを<ruby>構築<rt>こうちく</rt></ruby>する。

Re-create a table to store the following data.

---

由於現在還沒有數據，因此在 DataFrame 當中利用 columns 事先建立所需欄位。

今はまだデータがいないので、columns を使って<ruby>事前<rt>じぜん</rt></ruby>に列を<ruby>設立<rt>せつりつ</rt></ruby>。

Since there is no data yet, use columns in the DataFrame to create the required columns in advance.

---

若是建立的同時就給予數據， pandas 會自己判斷有多少欄位。

もし構築しているとき、データもうありますなら、pandas が自分で列の数量を判断する。

If the data is given while we build a table, pandas will determine how many columns it needs.

---

.loc 後面使用中括弧將該行的名稱包起來，新增或讀取都是利用這個方式。

.loc の後ろ<ruby>角括弧<rt>かくがっこ</rt></ruby>で列の名前を取り囲んで、追加と読むもこの方法を利用する。

Use brackets after .loc to enclose the name of the row. This method is used for adding or reading.

```python
rotor_df = pd.DataFrame(columns=[i for i in range(len(element))])
rotor_df.loc["I"] = I
rotor_df.loc["II"] = II
rotor_df.loc["III"] = III
rotor_df.loc["IV"] = IV
rotor_df.loc["V"] = V

print(rotor_df.head())
print(rotor_df.tail())
```

這個表格在最後一個課程當中會需要用到，所以這裡利用 to_csv 把它寫成 csv 檔，保存在電腦中。

このフォームは最後のチュートリアルの時に使われるので、ここで to_csv を利用して csv のファイルになる、コンピューターに収納する。

This form will be used in the last course, so use to_csv to write it as a csv file and save it on the computer.

---

括弧內寫的是儲存的檔案(相對)路徑。

丸括弧の中にはファイルの(<ruby>相対<rt>そうたい</rt></ruby>)パス。

What is written in brackets is the (relative) path of the stored file.

```python
rotor_df.to_csv("rotors.csv")
```

之後如果要再使用這個表格，可以利用 read_csv 根據檔案路徑把資料讀進來。

将来もう一度このフォームを利用したいなら、 read_csv でファイルのパスによると、データを読みます。

If we want to use this table in the future, we can use read_csv to load the data according to the file path.

---

header=0 與 index_col=0 分別代表了橫向第一行是 header (前面說的 columns) 以及縱向第一行是 index(I, II, III, IV, V)。

header=0 と index_col=0 それぞれ”横方向第一行は header (前の columns)と縦方向第一行は index(I, II, III, IV, V)”。

header=0 and index_col=0 represent the horizontal first row is the header (columns mentioned earlier) and the vertical first row is the index (I, II, III, IV, V).

```python
read_df = pd.read_csv("rotors.csv", header=0, index_col=0)
print(read_df.head())
print(read_df.tail())
```

除了三種語言的元素，還需要所謂的狀態值，提供 Enigma 的旋轉盤當作參數使用。

三つ言語の上で、スクランブラーの状態値も必要だ。Enigma のスクランブラーのパラメータとして使います。

In addition to the elements of the three languages, so-called status values ​​are required to provide Enigma as parameters of rotators.

---

旋轉盤的狀態將隨著日期，每天做變動，因此下面這個表格將利用日期作為每一行的名稱。

<ruby>日付<rt>ひづけ</rt></ruby>によるとスクランブラーの状態値は毎日変えます。だから、下のフォームは日付を利用して行の名前になる。

The status of the rotator will change every day with the date, so the following table will use the date as the name of each row.

---

datetime 是 Python 在處理日期時間方面的套件之一，利用 datetime.today() 可以取得現在的日期與時間。

datetime は Python のパッケージの一つ、日付と時間の問題に対処する。datetime.today() を利用して、今の日付と時間をもらう。

datetime is one of Python's packages for dealing with date and time. Using datetime.today() can get the current date and time.

```python
today = datetime.today()
print(today)
```

若直接在 datetime 後面輸入年月日，便可產生指定日期的 datetime 。

datetime の後ろに日付を直接的に輸入したら、特定日付の datetime をもらう。

If we enter the year, month, and day directly after datetime, it will generate the datetime for the specified date.

---

我準備透過迴圈建立 2019 年 11 月一整個月的日期，因此先分別建立 11 月 1 日與 12 月 1 日的 datetime 。

これからループで 2019 年 11 月一か月の日付を構築しての予定ので、先ずはそれぞれ 11 月 1 日と 12 月 1 日の datetime を構築する。

I am going to create dates for the entire month of November 2019 through a loop, so first create datetimes for November 1st and December 1st respectively.

---

datetime 可以加減與比較大小的性質，讓我可以這麼做。

datetime は計算できると比較できるの<ruby>性質<rt>せいしつ</rt></ruby>によて、後ろのことができます。

The nature of datetime can add and subtract and compare sizes, so I can do that.

```python
current_date = datetime(2019, 11, 1)
end_date = datetime(2019, 12, 1)
```

預設為 5 組旋轉盤的狀態，同樣這裡先告訴 pandas 我要建立 NUM 個欄位，如果有需要可以將 NUM 的數值做修改。

デフォルトのスクランブラー数量は NUM 個、 pandas で NUM 列を構築して。NUM の数値が 5 、必要ならこの数値を変えて大丈夫です。

The default is the state of 5 sets of rotators. Also tell pandas here that I want to create NUM columns. If necessary, we can modify the value of NUM.

```python
NUM = 5
status_df = pd.DataFrame(columns=[i for i in range(NUM)])


def getStatus(_element_length):
    status = []
    for j in range(NUM):
        rand = randint(0, _element_length - 1)
        status.append(rand)

    return status
```

getStatus 根據陣列長度，產生五個隨機數，分別是五個旋轉盤的狀態值。

getStatus は配列の長さによて、五つ<ruby>乱数<rt>らんすう</rt></ruby>を<ruby>生成<rt>せいせい</rt></ruby>する。それぞれ五つスクランブラーの<ruby>状態<rt>じょうたい</rt></ruby>値です。

According to the length of the array, getStatus generates five random numbers, which are the status values ​​of the five rotators respectively.

---

狀態值的範圍是 0 到 (陣列長度 - 1)，與陣列的索引值範圍相同。

状態値の範囲はゼロから”配列の長さ引く一”、配列のインデックスの範囲と同じ。

The status value range is 0 to (array length-1), which is the same as the array index value range.

---

在 current_date 小於 end_date 之前，持續將 current_date 作為行的名稱，五個旋轉盤的狀態值 作為數據，加入表格當中。

current_date は end_date より小さい前、current_date が行の名前として、五つスクランブラーの状態値をデータとしてフォームに追加することを繰り返します。

Before current_date is less than end_date, it will continue to use current_date as the name of the row and the status values ​​of the five rotators as data to add to the table.

---

迴圈最後一行，利用 current_date += timedelta(days=1) 取得"下一天"的日期，一直重複直到 current_date 超過 11 月，這樣表格就完成了。

ループの最後一部分は current_date += timedelta(days=1) を利用して、明日の日付をもらって、 current_date が 11 月<ruby>越える<rt>こえる</rt></ruby>前に繰り返します。

The last line of loop will "use current_date += timedelta(days=1)" to get the date of the "next day" repeatly until the current_date exceeds November, and the form will be completed.

---

current_date.strftime("%Y-%m-%d") 將 current_date 的時間格式化成"年-月-日"的形式。

current_date.strftime("%Y-%m-%d") で current_date の時間をフォーマットして”年-月-日”の<ruby>形式<rt>けいしき</rt></ruby>になる。

current_date.strftime("%Y-%m-%d") will format the time of current_date into "year-month-day".

---

之後利用日期讀取時，也利用相同方式把日期格式化，不需要去考慮時分秒等數值。

将来日付利用して読むとき、同じ方法を利用すればいい。時、分、秒の数値なら考えて必要はないだ。

When reading the date in the future, the date is also formatted in the same way, without the need to consider values ​​such as hours, minutes, and seconds.

```python
element_length = len(element)
while current_date < end_date:
    index = current_date.strftime("%Y-%m-%d")
    status_df.loc[index] = getStatus(element_length)
    current_date += timedelta(days=1)

print(status_df.head())
print(status_df.tail())

status_df.to_csv("rotors_status.csv")


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
```