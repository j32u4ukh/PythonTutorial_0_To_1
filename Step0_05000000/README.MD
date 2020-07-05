教學大綱；シラバス；syllabus：
1. print
2. 註解 / <ruby>注釈<rt>ちゅうしゃく</rt></ruby> / comment
3. len

---

印出 "Hello World" 應該是所有程式初學者共同的經歷了吧。

"Hello World"をプリントアウトすることはプログラムを勉強する初心者なら誰でも経験があるだろう。

Printing the "Hello World" is a common exprience of all beginners who learns programming.

```python
print("Hello World")
print("炎")
print("あ")
```

用 2 個單引號或雙引號包住的一串文字，我們稱為字串，可利用 print 呈現出來。

二つの<ruby>一重<rt>ひとえ</rt>引用符<rt>いんようふ</rt></ruby>または<ruby>二重<rt>ふたえ</rt></ruby>引用符で文字を<ruby>取<rt>と</rt></ruby>り<ruby>囲<rt>かこ</rt></ruby>むのことは<ruby>文字列<rt>もじれつ</rt></ruby>と呼ばれる。print でプリントアウトできる。

A string of text enclosed in 2 single or double quotation marks, which we call "string", can be displayed by using print function. 

**<ruby>複数行<rt>ふくすうぎょう</rt></ruby>注釈**

* <ruby>効果<rt>こうか</rt></ruby>
* <ruby>各行<rt>かくこう</rt></ruby>
* <ruby>与<rt>あた</rt></ruby>えない

```python
"""
而這段文字目前在的部分稱為多行註解，透過前後各 3 個單引號或雙引號包住，用來對程式碼做補充說明，不會對程式碼本身產生影響。

この部分の文字は複数行注釈と呼ばれる。前と後ろ三つの一重引用符または二重引用符で内容を取り囲む。コードについて説明し、影響を与えない。

The current part of this text is called a multi-line comment. It is surrounded by three single or double quotation marks, to illustrate the effect of the code. It will not be executed.
"""

'''
單引號的效果等同雙引號。

一重引用符の効果は二重引用符と同じだ。

Single quotation mark is same as double one.
'''

# 而這是單行註解的方式，在每行前面加井字號。

# これは単行注釈のやり方で、各行の前にシャープをかける。

# Adding the pound sign in front of each line is the way of one-line comment.
```

* <ruby>単行<rt>たんこう</rt></ruby>
* ~で（す）：中止型，連接句子

---

print 除了可以印出字串之外，也可以印出數字。

print は<ruby>文字列<rt>もじれつ</rt></ruby>だけではなく、数字もプリントアウトできる。

Print function can print out not only a string but also numbers.

```python
print(3)
print(3.141592653589)
```

最後要介紹的是 len()，可以回傳字串或其他變數的長度，其他變數會在後面依序介紹。

最後は len() について紹介する。これで文字列の長さとか<ruby>他<rt>ほか</rt></ruby>の<ruby>変数<rt>へんすう</rt></ruby>の長さとかを返事ができる。他の変数は後で紹介する。

Finally, I'm going to introduce len function which can return the length of a string or other varibles. Other varibles will introduce sequentially at the coming chapters.

* について

---

大家可以嘗試換掉雙引號當中的內容，可以更加瞭解 len() 的作用喔。

皆さんは二重引用符中の内容を変えてみれば、len() の効果がもっと分かる。

* 変えてみれば: 試著改變
* 分かる： 助詞用 が
* 知る： 助詞用 を

You can try to change the contents of double quotation marks, which will help to understand the effect of len function deeply.

---

"Hello World"的長度是 11，因為"空格"也被算進去了。

"Hello World"の長さは 11 だ。なぜなら、スペースも数えられるからだ。

The length of "Hello World" is 11 because the space is also been counted.

```python
print(len("Hello"))        # 5
print(len("World"))        # 5
print(len("Hello World"))  # 11
print(len("炎"))           # 1
print(len("あ"))           # 1
```

而寫著這些程式的檔案(Step0_05000000.py)通常稱之為腳本。

このファイル(Step0_05000000.py)はスクリプトと呼ばれる。

These files that are writed with code are called "script".