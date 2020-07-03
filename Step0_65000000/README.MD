"""
教學大綱；シラバス；syllabus：
1. function
2. return
3. variable_name

---

前面我們曾利用迴圈去添加元素到陣列當中，將內容寫到迴圈當中，重複執行相似的程式碼。

この前教えた、ループを利用して配列に要素を追加して、コンテンツをループに書き<ruby>込<rt>こ</rt></ruby>みんで、<ruby>似<rt>に</rt></ruby>ているコードの実行を<ruby>繰<rt>く</rt></ruby>り<ruby>返<rt>かえ</rt></ruby>します。

Earlier we used the loop to add elements to the array, write the content in the loop, and repeatedly execute similar code.

---

當我們要做一些重複的事情，除了利用迴圈，還會透過 def 來定義'函式'，並將這些內容重複呼叫。

繰り返しやることがありますとき、ループ以外も def で”関数”を定義して、その内容に何度も使える。

When we want to do some repetitive things, in addition to using loops, we will also define'functions' through def and call these contents repeatedly.

---

其實前面所使用的 print() 、 len() 、 append() 、、、都是函式的例子。

実は、使えたの print() 、 len() 、 append() 、、、も関数の例だ。

In fact, the print(), len(), append()... are examples of functions.

```python
def printAToZ():
    a_to_z = []
    for i in range(97, 97 + 26):
        _char = chr(i)
        a_to_z.append(_char)

    print(a_to_z)


printAToZ()
printAToZ()
```

上方例子 printAToZ() 的括弧中沒有東西，也沒有使用到外部的變數，因此每次執行的結果都是相同的。

上の printAToZ() 、<ruby>丸括弧<rt>まるかっこ</rt></ruby>の中には何もいない、外の変数も使わない、だから毎回実行したの結果も同じ。

The above example printAToZ() has nothing in the parentheses and no external variables are used, so the result of each execution is the same.

---

括弧中可以放一些變數，又可稱為參數，讓我們可以執行'大部分相同，只有些許部分不同'的內容。

丸括弧の中に変数を入れることはできます、これら変数がパラメータと呼ばれる。”大体同じ、少し違う内容”を実行することができます。

We can place some variables which can also be called parameters  in parentheses, so that we can perform the content of 'almost is same, but only a little different'.

```python
def elementIndex(arr, element):
    try:
        index = arr.index(element)
    except ValueError:
        arr.append(element)
        # sort array
        arr.sort()

        index = arr.index(element)

    print("element:{} @ index:{}, array = {}".format(
        element,
        index,
        arr
    ))


array = [1, 3, 5, 7, 9]
elementIndex(array, 5)
elementIndex(array, 6)

array = [0, 2, 4, 6, 8]
elementIndex(array, 5)
elementIndex(array, 6)
```

可以看到，一樣的函式根據不同的參數，可以執行'大部分相同，只有些許部分不同'的內容。

上から見える、同じ関数が違うパラメータに”大体同じ、少し違う内容”を実行している。

As you can see  that the same function can execute'mostly the same content, but only slightly different' according to different parameters.

---

函式除了單純執行程式碼，還可以回傳數值。比如幫我計算完 BMI 後，透過最後一行的 return 將結果回傳出來。

関数はコードを実行することができて加えて数値を戻ってもできます。例えば： BMI の数値を計算したあと、最後の return で結果を戻って。

In addition to simply executing the code, the function can also return values. For example, after calculating the BMI for me, return the result through the "return" at the last line.

```python
def computeBmi(_height, _weight):
    try:
        # cm → m
        _height /= 100
        _bmi = _weight / (_height * _height)
    except ZeroDivisionError:
        _height = 1.6
        _bmi = _weight / (_height * _height)

    return _bmi


bmi = computeBmi(188, 70)
print("My bmi is ", bmi)
```

從前面幾個函式的使用，應該可以發現一些命名規則。

前の関数の使い方を見ると、いくつかの<ruby>命名<rt>めいめい</rt>規則<rt>きそく</rt></ruby>を見つけることができるはずです。

From the use of the previous functions, you should find some naming rules.

---

例如函式名稱的開頭單字是小寫，後面的單字都只有開頭是大寫，其他都是小寫。

例えば：関数<ruby>名<rt>めい</rt></ruby>の<ruby>先頭<rt>せんとう</rt></ruby>は<ruby>小文字<rt>こもじ</rt></ruby>です、後ろの単語が先頭だけ<ruby>大文字<rt>だいもんじ</rt></ruby>で使て、他のは小文字です。

For example, the first letter of the first word of a function name is lowercase, all the following words are only the first letter is uppercase, and the others are all lowercase.

---

而且，函式名稱大多會使用動詞，可以讓其他人一眼就知道這個函式的作用為何。

それに、関数名は大体<ruby>動詞<rt>どうし</rt></ruby>を使て、他の人にこの関数の<ruby>役割<rt>やくわり</rt></ruby>を見てわかる。

Moreover, most of the function names use verbs, so that others can know at a glance what the function does.

---

但這只是習慣而已，並不保證全部函式都會這麼命名。

でも、しかし、これは<ruby>単<rt>たん</rt></ruby>なる習慣であり、すべての関数がこの方法で命名されるという<ruby>保証<rt>ほしょう</rt></ruby>はありません。

But this is just a habit, and there is no guarantee that all functions will be so named.

---

以下演示是在函數中使用函數外部的變量的示例。

下は関数の内部で外部の変数を使っているの例です。

The following demo is an example that use a variable outside of function in the function.

---

一般即便不使用 global 來宣告 value 為全域變數也可使用。

普通、 global を使って value がグローバル変数を<ruby>発表<rt>はっぴょう</rt></ruby>することをしないでもグローバル変数が使える。

Generally, it can be used even if global is not used to declare value as a global variable.

---

但函式結束後對全域變數的操作便無效了。

だが、関数は終わりとき、グローバル変数にしたことがいなくなります、外部のグローバル変数の数値も変えない。

But after the function ends, the operation on the global variables is invalid.

---

使用 global 的效果便是在函式內的操作在函式結束後依然有效。

global を使って、関数内部に変数を<ruby>操作<rt>そうさ</rt></ruby>したの結果がなくすことがない。

The effect of using global is that the operations in the function are still valid after the function ends.

```python
value = 7


def sumValue(_new_value):
    global value

    value = value + _new_value
    print("value:", value)


sumValue(3)
sumValue(3)
```
