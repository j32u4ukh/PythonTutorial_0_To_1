"""
教學大綱；シラバス；syllabus：
1. [i for i in range]
2. index

---

在學了陣列與迴圈之後，要來介紹一種比較特別的'建立陣列的方式'。

配列とループを教えたあと、今回は特別な陣列に確立する方を紹介します。

After learning about arrays and loops, let's introduce a special "method of building arrays".

---

它的形式是 [i for i in range] ，會依序將迴圈前面的值加入陣列，也可以對這個值做一些計算，例如: [i + 1 for i in range]。

その形式は [i for i in range] 、順番にループ前の数値を配列に追加して。追加する前にこの数値を計算してもいい、例えば： [i + 1 for i in range]。

Its form is [i for i in range], and the value before the loop will be added to the array in sequence, and we can also do some calculations on this value, for example: [i + 1 for i in range].

```python
array1 = [i for i in range(5)]
print("array1:", array1)

array2 = [i + 1 for i in range(5)]
print("array2:", array2)
```

在這之上，還可以在後方加入條件句，進一步對 i 做操作。

その上、ループの後ろで条件を追加してもできる、<ruby>更<rt>さら</rt></ruby>に i を<ruby>操<rt>あやつ</rt></ruby>る。

Base on that, we can also attach a condition at the rear to further operate on i.

```python
array3 = [i for i in range(10) if i % 3 == 0]
print("array3:", array3)
```

另外，前面介紹過利用索引值去取出陣列中的值，倘若今天要用陣列中的值反過來取得索引值時，就需要使用 index()。

一方、この前言った”インデックスで配列中の数値をを読んで”、もし今は逆に配列中の数値でインデックスを問い合わせしてなら、 index() を使ってください。

In addition, the index value is used to retrieve the value in the array. If you want to use the value in the array to obtain the index value in turn, you need to use index().

---

使用前面示範的 array3 當例子，我想知道 6 這個數值在陣列中的索引值，使用 index 便會返回 2。

前の array3 を例として<ruby>使用<rt>しよう</rt></ruby>します、数字 6 は配列の中にインデックスを知りたいなら、 index() を使って 2 が<ruby>戻<rt>もど</rt></ruby>って。

Using the array3 shown above as an example, I want to know the index value of 6 in the array, and using index will return 2.

```python
array3 = [i for i in range(10) if i % 3 == 0]
print(array3.index(6))  # 2
```

萬一我使用了不存在陣列中的數值時，會發生什麼呢？答案是報錯，告訴我們發生了 ValueError。

もし配列の中にいないの数値を問い合わせしてなら、何が発生しますか？答えはエラーを<ruby>報告<rt>ほうこく</rt></ruby>する、私たちに ValueError が発生しましたと教える。

What happens if I use a value that does not exist in the array? The answer is showing an error which tells us that a ValueError has occurred.

---

至於什麼是 ValueError 在後面的教學當中會再提到，知道這是一種程式上的錯誤就好了。

ValueError とは何か、後でのチュートリアルがもう一度<ruby>言及<rt>げんきゅう</rt></ruby>します、これがプログラム上のエラーであることを知っているのは問題ありません。

As for what is ValueError, it will be mentioned again in the following teaching, just know that it is a kind of program error.

```python
array3 = [i for i in range(10) if i % 3 == 0]
print(array3.index(7))  # ValueError: 7 is not in list
```
