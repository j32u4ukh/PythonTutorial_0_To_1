# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:40:19 2019

@author: j32u4ukh

教學大綱：
1. +, -, *, /, %
2. +=, -=, *=, /=, %=
3. ==
4. variable_name
"""
"""
這個部分要介紹數學運算所使用的符號。

首先，利用前面教過的變數，將一些數字"賦值"給左邊的變數。
"""
a = 2
b = 3
c = 5
d = 8
e = 13

print(a + b)  # 5
print(d - c)  # 3
print(a * e)  # 26
print(c / a)  # 2.5
print(d / a)  # 4.0

"""
c / a = 2.5 表示 c 無法被 a 整除，若想知道餘數為何，便可利用"%"。

求餘數可以用在判斷是否整除(是否為某數的倍數)等，是很常使用的符號喔。
"""
print(c % a)  # 1
print(d % a)  # 0
print(e % c)  # 3

"""
印出 a + b = 5 之後再印一次 a 會發現它還是 2，若想改變 a 的值，就需要再賦值一次。
"""
print(a)  # 2
print(b)  # 3

"""
右邊的 a + b 等於 5 ，將這個值"賦值"給左邊的 a ，因此現在的 a 等於 5 ，右邊是"賦值"
之前的 a ，所以數值是 2。
"""
a = a + b
print(a)  # 5
print(b)  # 3

"""
+= 這個符號，效果上面的一樣，但它在進行加法的同時便進行"賦值"，因此這種寫法看起來
更為簡潔。
"""
a = 2
b = 3
a += b
print(a)  # 5
print(b)  # 3

"""
-=, *=, /=, %= 的效果也在此示範，都是先做左邊符號的動作，然後再"賦值"給左邊的變數。
"""
a -= b
print(a)  # 5

a *= b
print(a)  # 15

a /= b
print(a)  # 5

a %= b
print(a)  # 2.0

"""
那如果是 == 又是什麼意思呢？這用在判斷左右兩邊的數值是否相等。
"""
print(2 + 1 == 3)  # True
print(2 + 5 == 3)  # False

"""
若要判斷左右兩邊的數值是否'不相等'，則要使用 !=。
"""
print(2 + 1 != 3)  # False
print(2 + 5 != 3)  # True

"""
最後要提一下，變數命名規則，不同的語言可能會有不同的地方，以下介紹我的命名習慣，
感興趣的可以上網找找各種語言的命名規則。

變數基本上都會使用小寫英文字、數字以及部分特殊符號組成，且是有意義的單字，例: _number1。

如果是多個單字組成，會利用"_"連接單字，例: breathe_of_water。

若全為大寫的變數，通常是常數，即不會改變數值的數，例: 圓周率 PI = 3.14159....。

其他情況的命名規則，就等遇到了再做說明吧。
"""