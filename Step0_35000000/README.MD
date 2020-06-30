教學大綱；シラバス；syllabus：
1. ord()
2. chr()
3. int()
4. float()

這裡要介紹 ASCII 碼與文字符號之間的轉換，ASCII 碼簡單來說就是為了讓電腦理解，因此用一串數字去表示許多文字或符號。

ここで ASCII コードとテキスト間の<ruby>変換<rt>へんかん</rt></ruby>を紹介します。単に話すと、ASCII コードはコンピューターにテキストを理解できるのため、数字で表すのコード。

Here is going to introduce transforming between ASCII code, character and symbol. Roughly speaking, the ASCII code is for the computer to understand, using a string of numbers to represent many characters and symbols.

---

至於精確地說明就請自行上網找來看吧。

詳しい紹介知りたいなら、自分でネットで探しましょう。

Much precisely explain, please searching on the net by yourself.

---

利用 ord() 將文字符號轉換成 ASCII 碼；chr()則可將 ASCII 碼轉換回文字符號。兩者是可以互相轉換的關係。

ord() でテキストに ASCII コードを変換する。chr() で ASCII コードにテキストを変換する。<ruby>両方<rt>りょうほう</rt></ruby>は<ruby>相互<rt>そうご</rt></ruby>変換ことができます。

Using ord function to transform character and symbol to ASCII code; using chr function to transform ASCII code to character and symbol. The two are mutually convertible.

```python
print(ord('a'))  # 97
print(chr(97))   # a

print(ord('z'))          # 122
print(chr(97 + 26 - 1))  # z
```

說個題外話，在前面的教學曾經教過利用"/"進行除法，以及利用"%"取得餘數，這裡要介紹如何取得商數。

ところで、前に教えて"/"で<ruby>割<rt>わ</rt></ruby>り算をすることと"%"で残りを計算すること。ここで商を紹介します。

To make a digression, in the previous teaching, I used "/" to divide and "%" to obtain the remainder. Here I will introduce how to obtain the quotient.

---

實際執行 5 / 2 你會得到 2.5 而非 2；若是 7 / 2 會得到 3.5 而非 3。

5 / 2 を計算したあと、 2 でなく 2.5 をもらいました。 7 / 2 を計算したあと、3 でなく 3.5 をもらいました。

Actually executing 5 / 2, you will get 2 instead of 2.5; if 7 / 2 will get 3 instead of 3.5.

---

但都可以觀察到，商數就是答案的整數部分，若能只取得整數部分，那就達到目的了，此時就是要使用 int()。

商は割り算の結果の<ruby>整数<rt>せいすう</rt></ruby>、整数を貰ってのため、 int() で使いましょう。

But we can see that the integer part of answer is quotient, if we can get the integer part only, we will get the quotient, it is time to use int function. 

```python
ans = 5 / 2
print(ans)       # 2.5
print(int(ans))  # 2

ans = 7 / 2
print(ans)       # 3.5
print(int(ans))  # 3
```

int() 可以忽略小數點，返回整數的部分。另一方面， float() 則可將整數變成浮點數。

int() は小数点数の部分を捨てて、整数の部分を帰す。ちなみに、float() は浮動小数点数を整数に変換します。

The int function will ignore the decimal point and return the integer part. On the other hand, float function can transform integers to floating-point numbers. 

---

實際上，int() 和 float() 也可以將字串形式的數值，分別變成整數和浮點數呢。

実は、int() と float() は文字列型の数字を整数と浮動小数点数に変えられる。

In fact, int and float function can transform the numeric values in string form into integers and floating-point numbers, respectively.

```python
num1 = 9
print(num1)         # 9
print(float(num1))  # 9.0

num2 = "11"
print(int(num2))    # 11
print(float(num2))  # 11.0

num3 = "9.8"
# print(int(num3)) 是不行的喔
print(float(num3))  # 11.0
```

哪些形式的內容可以變成你所需要的值，其實不急著在現在全部都了解，遇到那些需求時再去了解就可以了。

どうなタイプが別のタイプに変換することは今全部を分かる必要がないだ。<ruby>需要<rt>じゅよう</rt></ruby>がありますとき、勉強すればいい。

It is not have to know all kinds of form that the content with can transform to your need. It's enough to understand when you meet those needs.