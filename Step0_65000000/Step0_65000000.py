# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:46:56 2019

@author: j32u4ukh

教學大綱；シラバス；syllabus：
1. function
2. return
3. _variable_name

前面我們曾利用迴圈去添加元素到陣列當中，重複執行相似的程式碼，將內容寫到迴圈當中。
この前教えた、ループを利用して配列に要素を追加して、似(に)ているコードの実行を
繰り返し(くりかえし)、コンテンツをループに書き込みます(こみます)。

＝＝＝＝＝
當我們要做一些重複的事情，除了利用迴圈，還會透過 def 來使用'函式'來將這些內容重複呼叫。
繰り返しやることがありますとき、ループ以外 def で”関数”使うこともあります。

＝＝＝＝＝
其實前面所使用的 print() 、 len() 、 append() 、、、都是函式(def)的例子。
実は、使えたの print() 、 len() 、 append() 、、、も関数の例だ。
"""
def printAToZ():
     a_to_z = []
     for i in range(97, 97 + 26):
          _char = chr(i)
          a_to_z.append(_char)
          
     print(a_to_z)


printAToZ()
printAToZ()
"""
上方例子 printAToZ() 的括弧中沒有東西，也沒有使用到外部的變數，因此每次執行的結果
都是相同的。
上の printAToZ() 、丸括弧(まるかっこ)の中には何もいない、外の変数も使わない、だから
毎回実行したの結果も同じ。

＝＝＝＝＝
括弧中可以放一些變數，又可稱為參數，讓我們可以執行'大部分相同，只有些許部分不同'的內容。
丸括弧の中に変数を入れることはできます、これら変数がパラメータと呼ばれる。”大体同じ、
少し違う内容”を実行することができます。
"""


def elementIndex(_array, _element):
     try:
          _index = _array.index(_element)
     except ValueError:
          _array.append(_element)
          # sort array
          _array.sort()
     
          _index = _array.index(_element)
     
     print("element:{} @index:{}, array = {}".format(
               _element,
               _index,
               _array
           ))
     

array = [1, 3, 5, 7, 9]
elementIndex(array, 5)
elementIndex(array, 6)

array = [0, 2, 4, 6, 8]
elementIndex(array, 5)
elementIndex(array, 6)
"""
可以看到，一樣的函式根據不同的參數，可以執行'大部分相同，只有些許部分不同'的內容。
上から見える、同じ関数が違うパラメータに”大体同じ、少し違う内容”を実行している。

＝＝＝＝＝
函式除了單純執行程式碼，還可以回傳數值。比如幫我計算完 BMI 後，透過最後一行的
return 將結果回傳出來。
関数はコードを実行することができて加えて数値を戻ってもできます。例えば： BMI の数値を
計算したあと、最後の return で結果を戻って。
"""


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
"""
從前面幾個函式的使用，應該可以發現一些命名規則，例如函式名稱的開頭單字是小寫，後面的
單字都只有開頭是大寫，其他都是小寫。
前の関数の使い方を見ると、いくつかの命名(めいめい)規則(きそく)を見つけることができる
はずです。例えば：関数名(めい)の先頭(せんとう)は小文字(こもじ)です、後ろの単語が先頭
だけ大文字(だいもんじ)で使て、他のは小文字です。

＝＝＝＝＝
而且，函式名稱大多會使用動詞，可以讓其他人一眼就知道這個函式的作用為何，但這只是習慣而已，
並不保證全部函式都會這麼命名。
それに、関数名は大体動詞(どうし)を使て、他の人にこの関数の役割(やくわり)を見てわかる。
でも、しかし、これは単なる(たんなる)習慣であり、すべての関数がこの方法で命名される
という保証(ほしょう)はありません。

＝＝＝＝＝
而參數通常會以底線'_'作為開頭。這是為了方便區分函式內外的變數，避免混淆的做法。
大体パラメータの先頭はボトムライン'_'。これは、関数の内部(ないぶ)と外部(がいぶ)の
変数の区別(くべつ)を容易(ようい)にし、混乱(こんらん)を避ける(よける)ためです。

＝＝＝＝＝
以下示範函式內使用到函式外的變數的例子，一般即便不使用 global 來宣告 value 為全域變數
也可使用，但函式結束後對全域變數的操作便無效了。
下は関数の内部で外部の変数を使っているの例です。普通、 global を使って value が
グローバル変数を発表(はっぴょう)することをしないでもグローバル変数が使える。だが、関数
は終わりとき、グローバル変数にしたことがいなくなります、外部のグローバル変数の数値も
変えない。

＝＝＝＝＝
應該是因為我目前是使用 Spyder 的編譯器，變得必須使用 global 。使用 global 的效果便是
在函式內的操作在函式結束後依然有效。
多分今使うコンパイラは Spyder 、 global を使わなければなりません。 global を使って、
関数内部に変数を操作(そうさ)したの結果がなくすことがない。
"""
value = 7

def sumValue(_new_value):
     global value
     value += _new_value
     
     print("value:", value)
     

sumValue(3)
sumValue(3)