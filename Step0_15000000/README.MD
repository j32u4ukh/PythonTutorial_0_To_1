教學大綱；シラバス；syllabus：
1. +, -, *, /, %
2. +=, -=, *=, /=, %=
3. ==
4. variable_name


這個部分要介紹數學運算所使用的符號。

この部分は<ruby>計算<rt>けいさん</rt></ruby>で使われる<ruby>記号<rt>きごう</rt></ruby>。

This part is going to introduce symbols used in mathematical operations.

---

首先，利用前面教過的變數，將一些數字"賦值"給左邊的變數。

先ず、教えた変数を使って、変数を数字に代入する。

First, use what was taught earlier concept "variable" to assign some numbers to variables at left side.

```python
a = 2
b = 3
c = 5
d = 8
e = 13

print(a + b)  # 5   足（た）す     足（た）し算（ざん）
print(d - c)  # 3   引（ひ）く     引（ひ）き算
print(a * e)  # 26  掛（か）ける   掛（か）け算   
print(c / a)  # 2.5 割（わ）る     割（わ）り算
print(d / a)  # 4.0 
```

c / a = 2.5 表示 c 無法被 a 整除，若想知道餘數為何，便可利用"%"。

c / a = 2.5 の意味は” c が a で<ruby>割<rt>わ</rt></ruby>り<ruby>切<rt>き</rt></ruby>れない”。<ruby>残<rt>のこ</rt></ruby>りの数字を知りたければ、"%"で使えば分かる。

"c / a = 2.5" means c can't be divided by a. We can use "%" to check the remainder if we want to know that.

* 〜れば〜分かる:常用

---

求餘數可以用在判斷是否整除(是否為某數的倍數)等，是很常使用的符號喔。

残り数字を計算することは割り切れるかどうか（ある数字の何倍）を判断できる。よく使われる記号だよ。

Computing the remainder is used to determine whether it can be divisible (whether it is a multiple of a number) or not. A symbol that using frequency is very high.

---

印出 a + b = 5 之後再印一次 a 會發現它還是 2，若想改變 a 的值，就需要再賦值一次。

a + b = 5 をプリントアウトして、もう一度 a をプリントアウトしたら、a が 2 だった。a の数字を変えたいなら、もう一度代入することが必要だ。

When we print "a" again after printing "a + b = 5", we will find that "a" still be two. If we want to change the value of "a", we need to assign again.

* 〜たら〜だった/でした：做了...發現...

```python
a = 2
b = 3
c = 5
d = 8
e = 13

print(c % a)  # 1
print(d % a)  # 0
print(e % c)  # 3

print(a)  # 2
print(b)  # 3
```

右邊的 a + b 等於 5 ，將這個值"賦值"給左邊的 a ，因此現在的 a 等於 5 ，右邊是"賦值"之前的 a ，所以數值是 2。

右の a + b は 5 に<ruby>等<rt>ひと</rt><ruby>しく、この数値を左の a に代入して、今の a が 5 になっている。右の a は代入された前の数値だから、数値が 2 だ。

"a + b" at the right side is equal to five, and then assign this value to "a" at left side, so "a" is equal to five right now. The right side is original "a", so it's value is two.

* ~ている: 狀態的維持，因為 a 變成 5 之後會維持在 5 的狀態。

```python
a = 2
b = 3
a = a + b
print(a)  # 5
print(b)  # 3
```

+= 這個符號，效果和上面的一樣，但它在進行加法的同時便進行"賦值"，因此這種寫法看起來更為簡潔。

記号 += の効果は上と同じ、でもこれは足し算と代入すること同時に実行する。これはもっと<ruby>簡潔<rt>かんけつ</rt></ruby>なやり方です。

The symbol "+=" has effect same as above, but it can do addition and assign value at the same time. So this kind of writing looks more concise.

```python
a = 2
b = 3
a += b
print(a)  # 5
print(b)  # 3
```

-=, *=, /=, %= 的效果也在此示範，都是先做右邊符號的動作，然後再"賦值"給左邊的變數。

-=, *=, /=, %=　の効果はここで<ruby>実証<rt>じっしょう</rt></ruby>される。右側記号の計算を始めて、そして左の変数を計算の結果に代入する。

Show the effect of "-=, *=, /=, %=" at here, all of them are doing the right side calculation first, and assign the value to variable at left side.

* -=, *=, /=, %= 的效果被示範，因此要用被動型 実証される

```python
a = 8
b = 3

a -= b
print(a)  # 5

a *= b
print(a)  # 15

a /= b
print(a)  # 5

a %= b
print(a)  # 2.0
```

那如果是 == 又是什麼意思呢？這用在判斷左右兩邊的數值是否相等。

じゃ、== の意味は何でしょうか？これで左と右の数値が同じかどうかを判断する。

What is "==" meaning about? This is used to determine whether values are same at the left side and right side.

```python
print(2 + 1 == 3)  # True
print(2 + 5 == 3)  # False
```

若要判斷左右兩邊的數值是否'不相等'，則要使用 !=。

左の数値は右の(数値)に等しくないかどうかを判断するなら、!= を使ってください。

* 等しい: 相等
* 同じ：一樣

If we want to determine that whether the left and right values are different, we will use "!=".

```python
print(2 + 1 != 3)  # False
print(2 + 5 != 3)  # True
```

最後要提一下，變數命名規則，不同的語言可能會有不同的地方，以下介紹我的命名習慣，感興趣的可以上網找找各種語言的命名規則。

最後、変数を命名のルールはプログラムによって異なっている。今から、自分のルールを紹介する。興味があるなら、ネットで探してみましょう。

At last, the rule of naming of variables. Different program language may have different rule, I will introduce naming convention of myself. If you have interesting to this, you can search on the internet by yourself.

* 〜によって異なっている：因...而異
* これから：時間比較遠 vs 今から: 馬上接著
* 探してみましょう: 試著搜尋、尋找
---

變數基本上都會使用小寫英文字、數字以及部分特殊符號組成，且是有意義的單字，例: number1。

変数とは基本的に<ruby>小文字<rt>こもじ</rt></ruby>の英単語や数字や一部分特別な記号が使用されてい、ほとんど意味がある単語です、例えば：number1。

*　中止型: 使用されてい(る)
*　ほぼ："大約、大致"，(adv)，後不接名詞 vs ほとんど: "幾乎"，(adj)

Normally, variable will combine with lowercase alphabet, numbers and part of special symbol, to form a Meaningful word, for example: number1.

---

如果是多個單字組成，會利用"_"連接單字，例: breathe_of_water。

複数の単語　だったら・の場合　、"_"で<ruby>接続<rt>せつぞく</rt></ruby>する、例えば： breathe_of_water。

The situation of combining with multiple words will use "_" to combine, for example: breathe_of_water.

* なら：後多為建議

---

若全為大寫的變數，通常是常數，即不會改變數值的數，例: 圓周率 PI = 3.14159....。

英単語は全て<ruby>大文字<rt>おおもじ</rt></ruby>で表示される場合は、普通は定数、つまり、数値が変えられない数字だ。例えば： PI = 3.14159....。

If all words of the variable with capital, it is usally a constant value. It means the value will not be changed, for example: PI = 3.14159....

---

其他情況的命名規則，就等遇到了再做說明吧。

他のルールは、必要な時に説明する。

Other naming rules will be illustrated when we need to use them.
