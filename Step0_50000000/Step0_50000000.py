# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:45:25 2019

@author: j32u4ukh

教學大綱；シラバス；syllabus：
1. [i for i in range]
2. index

在學了陣列與迴圈之後，要來介紹一種比較特別的'建立陣列的方式'。
配列とループを教えたあと、今回は特別な陣列に確立する方を紹介します。

＝＝＝＝＝
它的形式是 [i for i in range] ，會依序將迴圈前面的值加入陣列，也可以對這個值做一些
計算，例如: [i + 1 for i in range]。
その形式は [i for i in range] 、順番にループ前の数値を配列に追加して。追加する前に
この数値を計算してもいい、例えば： [i + 1 for i in range]。
"""
array1 = [i for i in range(5)]
print("array1:", array1)

array2 = [i + 1 for i in range(5)]
print("array2:", array2)

"""
在這之上，還可以在後方加入條件句，進一步對 i 做操作。
その上、ループの後ろで条件を追加してもできる、更に(さらに) i を操る(あやつる)。
"""
array3 = [i for i in range(10) if i % 3 == 0]
print("array3:", array3)

"""
另外，前面介紹過利用索引值去取出陣列中的值，倘若今天要用陣列中的值反過來取得索引值時，
就需要使用 index()。
一方、この前言った”インデックスで配列中の数値をを読んで”、もし今は逆に配列中の数値で
インデックスを問い合わせしてなら、 index() を使ってください。

＝＝＝＝＝
使用前面示範的 array3 當例子，我想知道 6 這個數值在陣列中的索引值，使用 index 便會
返回 2。
前の array3 を例として使用(しよう)します、数字 6 は配列の中にインデックスを知りたい
なら、 index() を使って 2 が戻って(もどって)。
"""
print(array3.index(6))  # 2

"""
萬一我使用了不存在陣列中的數值時，會發生什麼呢？答案是報錯，告訴我們發生了 ValueError。
もし配列の中にいないの数値を問い合わせしてなら、何が発生しますか？答えはエラーを
報告(ほうこく)する、私たちに ValueError が発生しましたと教える。

至於什麼是 ValueError 在後面的教學當中會再提到，知道這是一種程式上的錯誤就好了。
ValueError とは何か、後でのチュートリアルがもう一度言及(げんきゅう)します、これが
プログラム上のエラーであることを知っているのは問題ありません。
"""
print(array3.index(7))  # ValueError: 7 is not in list