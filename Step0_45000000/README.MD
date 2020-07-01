教學大綱；シラバス；syllabus：
1. break
2. continue

---

之前在教迴圈的時候提到，for 和 while 會重複執行迴圈內的程式碼，直到達成中止條件。

ループを教えた時に言った、 for と while ループは終了条件に到達する前にループ内でコードを繰り返し実行する。

We had taught that "for" and "while" will execute the code in the block repeatedly until they reach abort condition.

---

這次要教的 break 和 continue 能讓我們在使用迴圈時更加的彈性

今回は break と continue を教えます、これらコードを使って、もっとフレキシブルな使い方になります。

In this chapter, we will teach you "break" and "continue" which make it more flexible when we using loop function.

---

中止條件是在一開始就設定好，倘若在迴圈執行的過程中，達到了其他的中止條件，希望直接停止迴圈時，便可使用 break ，中途停止迴圈。

終了条件は最初の時に設定した。もしループを実行するの間に他の終了条件に到達した、ループを直接的に<ruby>中止<rt>ちゅうし</rt></ruby>してなら、 break を使ってループをやめる。

Abort condition is defined at the begining. If we want to stop the loop directly when during the execution of the loop, other abort conditions are reached, we can use "break" to do it.

---

例如：迴圈的中止條件為變數 i 大於等於 0 小於 10，但如果變數 i 可以被 7 整除且不是 0，那就停止迴圈。

例えば：ループの終了条件は変数 i が<ruby>大<rt>だい</rt></ruby>なりイコールゼロ、<ruby>小<rt>しょう</rt></ruby>なり 10 。その上に、変数 i が 7 に割り切れて、数値が 0 じゃなくて、ループを中止する。

For example, the stopping condition of the loop is that the variable "i" is greater than or equal to 0 and less than 10, but if the variable "i" is divisible by 7 and is not 0, then the loop will be stopped.

---

像這種複合條件，就會需要使用之前教的 and, or 來連接。

こうな複数の条件の場合なら、教えたの and とか or とかが必要だ。

Like this compound condition, we will need to use the "and" and "or" taught before to connect.

```python
for i in range(10):
    print("for i:", i)

    if i % 7 == 0 and i != 0:
        break
print("=" * 10)

i = 0
while i < 10:
    print("while i:", i)
    if i % 7 == 0 and i != 0:
        break
    i += 1
```

另一方面，倘若在迴圈執行的過程中，某個條件下不執行，但其他仍照樣執行，則需使用 continue。

一方、もしループは実行しているの途中で、特定条件の場合コードが実行しないて、他の場合がまだ実行する。この状況なら、 continue を使ってください。

On the other hand, if during loop execution, we don't want to run the code under some condition, but other's situation still execute, we will need "continue".

---

例如：印出大於等於 0 小於 10 的奇數。這個例子不使用 continue 也可以做到。

例えば：数値は 0 <ruby>大<rt>だい</rt></ruby>なりイコール、<ruby>小<rt>しょう</rt></ruby>なり 10 の<ruby>奇数<rt>きすう/rt></ruby>。この例なら、 continue を使わないでも達成することができる。

For example: print out odd numbers greater than or equal to 0 and less than 10. This example can be done without using continue.

---

我將兩個版本都寫出來，讓各位比較一下，先不使用 continue ，之後再使用 continue

2つのバージョンも書いて、皆に比較する。最初は continue バージョン。

The following part will write two kinds of code to compare difference. First without "continue", and then using with "continue".

```python
# no continue
for i in range(10):
    # 注意差異；違いに注意してください; Note the difference
    if i & 1 != 0:
        print("for i:", i)

print("=" * 10)
i = 0
while i < 10:
    # 注意差異；違いに注意してください; Note the difference
    if i & 1 != 0:
        print("while i:", i)
    i += 1

# with continue
for i in range(10):
    # 注意差異；違いに注意してください; Note the difference
    if i & 1 == 0:
        continue
    print("for i:", i)

print("=" * 10)
# 注意差異；違いに注意してください; Note the difference
i = -1
while i < 10:
    i += 1

    # 注意差異；違いに注意してください; Note the difference
    if i & 1 == 0:
        continue
    print("while i:", i)
```
