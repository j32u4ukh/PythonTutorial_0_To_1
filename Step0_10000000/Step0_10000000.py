"""
教學大綱；シラバス；syllabus：
1. int
2. float
3. str
4. variable
5. type()

---

變數還有其他類型，但現在先教各位會需要使用的就可以了。

変数は他のタイプもあるが、今は使える変数だけ教える。

There are another kinds of variable, but now, learning the variable that will be used in the tutorail is enough.

---

首先是整數 int，如：1, 2, 3, 9527, ....。

先ずは整数 int、例えば：1, 2, 3, 9527, ....。

First one is "integer", for example: 1, 2, 3, 9527, ....。
"""
print(1)
print(2)
print(3)
print(9527)

"""
字串 str，之前的教學也提過，這裡就快速帶過。

文字列 str，前のレッスンで教えたので、ここは説明しない。

"String" which was teached before, so let's skip this part.

---

浮點數 float，也就是帶有小數點的數字。

浮動小数点数型 float　とは、小数点が付いている数字だ。

"Float" is the number with a decimal point.
"""
print(2.71828)
print(3.14159)
print(9.0)

"""
前面提的整數或字串等，可以利用"變數"代替，方便我們重複使用。

この前言った整数や文字列などは変数に交換できます。簡単に繰り返して使える。

Nouns like "integer" or "string" that we had been teached can replace with "variable" to use repeatly.

---

這個過程叫做"賦值"，將"右邊"的值給予"左邊"的變數，之後還會提到，請記得"賦值"的意思。

このプロセスは代入という、左側の変数に右側の数値を代入する。これからも何回も言うので、代入の意味を覚えてください。

The process is called "assign", giving the value of right to left variable. It will be metioned, please remember the meaning of this.
"""
t0 = 1
t1 = "字串"
t2 = 2.71828
j0 = 2
j1 = "さしすせそ"
j2 = 3.14159

print(t0)  # 1
print(t1)  # 字串
print(t2)  # 2.71828
print(j0)  # 2
print(j1)  # さしすせそ
print(j2)  # 3.14159

"""
當我們將整數、浮點數或字串存到變數裡面之後，我怎麼知道它是整數、浮點數還是字串呢？

整数とか浮動小数点数とか文字列を変数に代入した後、どうやってそれのタイプを知りますか？

When we assign a string, float or integer into variable, how can we konw that it type is?

---

可利用 type()，查看變數是屬於哪種類型喔。

type()　でこの変数のタイプをチェックはできます。

We can use type function to check the type of the variable.

---

<class 'int'>表示它屬於整數；<class 'str'>表示它屬於字串；<class 'float'>表示它屬於浮點數。

<class 'int'>の意味はこれは整数に属する；<class 'str'>は文字列に属する；<class 'float'>は浮動小数点数に属する。

<class 'int'> means that it is belonged to an integer; <class 'str'> means that it is belonged to a string；<class 'float'> means that it is belonged to an float.
"""
print(type(1))       # <class 'int'>
print(type(j0))      # <class 'int'>

print(type("字串"))  # <class 'str'>
print(type(j1))      # <class 'str'>

print(type(2.7182))  # <class 'float'>
print(type(j2))      # <class 'float'>
