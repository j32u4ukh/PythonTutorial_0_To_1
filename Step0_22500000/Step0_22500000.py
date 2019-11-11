# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:40:42 2019

@author: j32u4ukh

教學大綱；シラバス；syllabus：
1. 十進制；１０進數
2. 二進制；バイナリ
3. 二進制應用；バイナリの申し込み(もうしこみ)

一般我們所在使用的數字就是"十進制"，應該很好理解，數字為 0~9，超過 9 就會進位變成 10。
普通私たちが使う数字は"１０進數"、理解しやすいだろう。数字の範囲(はんい)はゼロから九まで
、これ以上がキャリーを発生して、九が十になります。

＝＝＝＝＝
而"二進制"是電腦的進位方式，數字為 0~1，超過 1 就會進位變成 10，通常會 8 位或 
16 位一起寫。
そして、バイナリはコンピューターをキャリーするのやり方。数字の範囲は 0 から 1 まで
、これ以上がキャリーを発生して、1 が 10 になります。普通、八つや十六個数字で
表示(ひょうじ)する。

＝＝＝＝＝
例：左邊十進制，右邊二進制
例えば：左側は"１０進數"、右側はバイナリ
0  → 00000000
1  → 00000001
2  → 00000010
3  → 00000011
4  → 00000100
...
10 → 00001010
11 → 00001011

＝＝＝＝＝
透過　Python 內建方法可輕鬆的進行十進制和二進制兩者的轉換。
Python　自分の関数(かんすう)で楽に"１０進數"とバイナリ間の交換する。
"""
decimal = 11
binary = "1011"
# 十進制 → 二進制
print(bin(decimal))

# 二進制 → 十進制
print(int(binary, 2))

"""
接著是本篇的重點，二進制應用。在這個專案的利用上是判斷奇偶。
そして、今回の焦点(しょうてん)、バイナリの申し込みだ。このプロジェクトには奇数または
偶数を判断する。

判斷奇偶可也可用之前教的"%"，但利用二進制的性質，可以更有效率的進行。
奇数または偶数は以前教えた"%"でで判断することもできるけど、バイナリの性質(せいしつ)を
利用して、もっと効率的なする。

11 → 00001011
1  → 00000001
"""
odd = 11
even = 12

# %
if odd % 2 == 0:
     print("偶數")
else:
     print("奇數")
     
if even % 2 == 0:
     print("偶數")
else:
     print("奇數")
     
# 二進制應用
if odd and 1 == 0:
     print("偶數")
else:
     print("奇數")
     
if even and 1 == 0:
     print("偶數")
else:
     print("奇數")