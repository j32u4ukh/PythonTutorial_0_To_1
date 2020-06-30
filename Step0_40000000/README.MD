教學大綱；シラバス；syllabus：
1. for, range
2. while
3. str.format()

---

這篇主要是要教迴圈的使用，分別為 for 和 while 兩種。這兩種迴圈都是在中止條件前，重複執行迴圈內的程式碼，但形式略有不同罷了。

今回はループの使い方を紹介します、for と while の二種類があります。この二つループも<ruby>終了条件<rt>しゅうりょうじょうけん</rt></ruby>に<ruby>到達<rt>とうたつ</rt></ruby>する前にループ<ruby>内<rt>うち</rt></ruby>でコードを<ruby>繰り返し<rt>くりかえし</rt>実行<rt>じっこう</rt></ruby>する、使い方がちょっと違うだけ。

This chapter will teach you to use two types of loops, "for" and "while". Two types of loops repeatly executue the code between loop block before the abort condition. They are just different on form.

---

for 的中止條件較為明確，而 while 的中止條件可以更為多樣。

for の終了条件はもっとかっちり、 while の終了条件はもっと多い様子があります。

The abort condition of "for" is much more clarifly, and abort conditions of "while" are much more diversify. 

---

若忘記加上中止條件，程式將不停地執行，進而造成電腦負擔，又被稱為無窮迴圈，請一定要避免這種情況發生喔。

終了条件を加えていないなら、無限ループと呼ばれて、コードがずっと実行して、コンピューターの<ruby>負担<rt>ふたん</rt></ruby>になります。このような事態は避けてください。

But when we forget to add abort condition to "while" loop, the programming will keep executing and cause burden to computer. We must avoid this situation.

---

因此我建議，有明確的次數時使用 for 迴圈，若沒有明確次數，而是某些條件符合才執行時使用 while 迴圈。

だから、自分の<ruby>提案<rt>ていあん</rt></ruby>はかっちりな終了条件があれば、for ループを使って、<ruby>特定<rt>とくてい</rt></ruby>の条件が<ruby>満<rt>み</rt></ruby>たされている場合だけ実行するなら、while ループを使ってください。

Therefore, I suggest to use "for" loop when there is a clear number of times. If there is no clarifly executing times, only execute the code when certain conditions are met, then use a "while" loop.

```python
array1 = [1, 2, 3, 4, 5]
for i in array1:
    print(i)
```

上面的 i 將依序到 array1 裡面取值，原本需要 5 行才能把全部印出來，現在 2 行就完成了。

i は array1 の中で順番に数値を持って、本来は 5 <ruby>行<rt>ぎょう</rt></ruby>を掛かって、今はただ 2 行ができる。

The "i" above will take values in array1 in sequence. Originally, it takes 5 lines to print all of them, and now we just need to use 2 lines to do the same thing.

---

而 while 則需要透過中括號與索引值來取值的方式進行。

while は<ruby>角括弧<rt>かくがっこ</rt></ruby>とインデックス利用して、数値を読んでいる。

In this case, "while" will need square brackets and indexs to take the value.

```python
array1 = [1, 2, 3, 4, 5]
i = 0
while i < len(array1):
    print(array1[i])
    i += 1
```

while 後面接的是終止條件，只要索引值小於長度值，就是重複印出陣列中第 i 個值。

while の後ろは終了条件、意味はインデックスが配列の長さより小さいなら、配列の第 i 目にプリントアウトする。

Followed by "while" is the abort condition which means that as long as the index value is less than the length value, the i-th value in the array is printed repeatedly.

---

緊接在印出的程式碼後面，i += 1 讓索引值每次加一，下次執行時印出的便會是下一個值，隨著索引值每次加一，最終將與長度值相等，並結束這個迴圈。

プリントアウトの下、 i += 1 でインデックスに一を<ruby>足<rt>た</rt></ruby>す、次回実行する時は第 i 目を読んでいます。インデックス<ruby>値<rt>ち</rt></ruby>は毎回 1 ずつ<ruby>増加<rt>ぞうか</rt></ruby>するため、<ruby>最終的<rt>さいしゅうてき</rt></ruby>に長さの値と<ruby>等<rt>ひと</rt></ruby>しくなり、ループを終了します。

Below the print function, "i += 1" will let index plus one each time. Next executing will print the next value. As the index value increases by one each time, it will eventually equal the length value and end the loop.

---

如果不知道為什麼"索引值小於長度值"才會印出的話，可以複習前面在教陣列的內容喔，以下示範其他應用的 for 和 while 迴圈。

どうして”インデックスが配列の長さより小さいの場合だけプリントアウトする”はわかりませんなら、前に教えた配列の内容を復習方がいいよ。これから for と while ループの他の<ruby>応用<rt>おうよう</rt></ruby>を実証する。

If you don't know why "it will print only when index value less than length of array", please review the chapter of array before. 

```python
print("for loop")
array2 = ['あ', 'い', 'う', 'え', 'お']
for i in array2:
    print(i)

print("while loop")
i = 0
while i < len(array2):
    print(array2[i])
    i += 1
```

如果 for 迴圈也想根據索引值去取出陣列中的值，想必會需要有個東西，依序取出時會是 [0, 1, 2, 3, 4]，那就是 range(5)。

もし for ループもインデックスを利用して、数値を読んでいるなら、きっとあるもの、順番に出す時は [0, 1, 2, 3, 4] 。そのものは range(5) だ。

If we want to use index to take the value of array, we will need something that return value sequentially with [0, 1, 2, 3, 4]. That one is "range(5)".

---

range(5) 表示從 0 開始，到 5 為止(不包含)，每次加 1 ，相當於 range(0, 5) 或 range(0, 5, 1)。

range(5) の意味はゼロから五まで(五は<ruby>含<rt>こ</rt></ruby>まれていない)、毎回 1 ずつ増加して。range(0, 5) と同じ、または range(0, 5, 1)。

"range(5)" means that it will return value starting from 0 and ending at 5(not include), plus one each time, also equal to range(0, 5) or range(0, 5, 1).

---

只有一個值時，預設第一個值為 0 ，且第三個值為 1；兩個值時，預設第三個值為 1。

一つ数字だけなら、初め数値のプリセットは 0 、第三目は 1；二つ数字あげるなら、第三目は 1。

If there is only one value, the default first value is 0, and third is 1; if there are two values, the default third value is 1.

---

如果想從 1 開始，到 5 為止(不包含)，每次加 2 ，則寫成 range(1, 5, 2)。

一から五まで(五が含まれていない)、毎回二つ増加してなら、 range(1, 5, 2) に書かれる。

If we want to start from 1 and end at 5(not include), plus 2 at each time, we can use range(1, 5, 2) to get the target.

```python
array2 = ['あ', 'い', 'う', 'え', 'お']
for i in range(5):
    print(array2[i])

for i in range(0, 5, 1):
    print(array2[i])

for i in range(1, 5, 2):
    print(array2[i])
```

迴圈搭配字串格式化，便可印出連續變化的字串等，不需要一個一個打。

ループと紐フォーマットすることを<ruby>協力<rt>きょうりょく</rt></ruby>して、続いて変化しての紐をプリントアウトして、一つ一つで書いての必要はない。

Loop function combine with string formating will print out continuously changing strings without needing to type one by one.

---

字串格式化可利用 {} 與 format() ，依序將數值放入即可。

紐フォーマットは {} と format() 利用して、順番に数値を入れていい。

One of ways to do string formating is {} and format function. Inputs values sequentially.

---

若只是要印出，更可透過逗號 "," 將內容依序排列即可。

プリントアウトの場合は "," で紐と数字を分かれていい。

If you just want to print out the value, you can put "," and content intervally.

```python
num = 0
for i in range(1, 6):
    print("i = ", i)
    num += i
    print("loop {}: num = {}".format(i, num))
```

字串可透過 * 號，乘上次數，形成多個字串連接的單一字串。搭配迴圈可印出一些有趣的圖案。

紐は "*" で<ruby>回数<rt>かいすう</rt></ruby>を<ruby>掛<rt>か</rt></ruby>けて、複数の紐に<ruby>接続<rt>せつぞく</rt></ruby>して、一つ紐になります。ループに加えて面白い<ruby>画像<rt>がぞう</rt></ruby>をプリントアウトする。

String can use symbol "*" to time the number to form a sigle string combin with multiple strings. With loop function, some interesting patterns can be printed.

```python
for i in range(1, 6):
    print("*" * i)
```

陣列也經常使用迴圈去新增或讀取。

配列もよくループを使って数値に<ruby>追加<rt>ついか</rt></ruby>または読むこと。

Arrays also often use loops to add or read.

```python
array3 = []
for i in range(5):
    array3.append(i)

for i in range(5):
    print(array3[i])

print(array3)
```
