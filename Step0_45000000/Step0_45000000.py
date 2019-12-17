"""
教學大綱；シラバス；syllabus：
1. break
2. continue

之前在教迴圈的時候提到，for 和 while 會重複執行迴圈內的程式碼，
直到達成中止條件，這次要教的 break 和 continue 能讓我們在使用迴圈時更加的彈性。
ループを教えた時に言った、 for と while ループは終了条件に到達する前にループ内で
コードを繰り返し実行する。今回は break と continue を教えます、これらコードを使って、
もっとフレキシブルな使い方になります。

＝＝＝＝＝
中止條件是在一開始就設定好，倘若在迴圈執行的過程中，達到了其他的中止條件，希望直接
停止迴圈時，便可使用 break ，中途停止迴圈。
終了条件は最初の時に設定した。もしループを実行するの間に他の終了条件に到達した、ループ
を直接的に中止(ちゅうし)してなら、 break を使ってループをやめる。

＝＝＝＝＝
例如：迴圈的中止條件為變數 i 大於等於 0 小於 10，但如果變數 i 可以被 7 整除
且不是 0，那就停止迴圈。像這種複合條件，就會需要使用之前教的 and, or 來連接。
例えば：ループの終了条件は変数 i が大なりイコール(だいなりイコール)ゼロ、
小なり(しょうなり) 10 。その上に、変数 i が 7 に割り切れて、数値が 0 じゃなくて、
ループを中止する。こうな複数の条件の場合なら、教えたの and とか or とかが必要だ。
"""
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

"""
另一方面，倘若在迴圈執行的過程中，某個條件下不執行，但其他仍照樣執行，則需使用
 continue。
一方、もしループは実行しているの途中で、特定条件の場合コードが実行しないて、他の場合が
まだ実行する。この状況なら、 continue を使ってください。

＝＝＝＝＝
例如：印出大於等於 0 小於 10 的奇數。這個例子不使用 continue 也可以做到，我將兩個
版本都寫出來，讓各位比較一下，先不使用 continue ，之後再使用 continue 。
例えば：数値は 0 大なりイコール(だいなりイコール)、小なり(しょうなり) 10 の
奇数(きすう)。この例なら、 continue を使わないでも達成することができる。2つの
バージョンも書いて、皆に比較する。最初は continue バージョン。
"""
# no continue
for i in range(10):
    # 注意差異；違いに注意してください
    if i & 1 != 0:
        print("for i:", i)

print("=" * 10)
i = 0
while i < 10:
    # 注意差異；違いに注意してください
    if i & 1 != 0:
        print("while i:", i)
    i += 1

# with continue
for i in range(10):
    # 注意差異；違いに注意してください
    if i & 1 == 0:
        continue
    print("for i:", i)

print("=" * 10)
# 注意差異；違いに注意してください
i = -1
while i < 10:
    i += 1

    # 注意差異；違いに注意してください
    if i & 1 == 0:
        continue
    print("while i:", i)
