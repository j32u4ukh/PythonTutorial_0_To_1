"""
教學大綱；シラバス；syllabus：
1. print
2. 註解；注釈(ちゅうしゃく)
3. len

＝＝＝＝＝
印出"Hello World"應該是所有程式初學者共同的經歷了吧。
"Hello World"にプリントアウトすることは全てプログラムを勉強の人共通の経験だそ。
"""
print("Hello World")
print("炎")
print("あ")

"""
用 2 個單引號或雙引號包住的一串文字，我們稱為字串，可利用 print 呈現出來。
二つの一重(ひとえ)引用符(いんようふ)または二重(ふたえ)引用符で文字を取(と)り
囲む(かこむ)のことは紐(ひも)と呼ばれる。print　でプリントアウトはできる。

＝＝＝＝＝
而這段文字目前在的部分稱為多行註解，透過前後各 3 個單引號或雙引號包住，用來對程式碼做
補充說明，不會對程式碼本身產生影響。
この部分の文字は複数行(ふくすうぎょう)注釈と呼ばれる。前と後ろ三つの一重引用符
または二重引用符で内容を取り囲む(とりかこむ)。注釈はコードに説明している、コードが
影響されない。
"""

'''
單引號的效果等同雙引號。
一重引用符と二重引用符の効果(こうか)は同じだ。
'''

# 而這是單行註解的方式，在每行前面加井字號。
# これは単行(たんこう)注釈のやり方、各行(かくこう)の前にシャープをかける。

"""
print 除了可以印出字串之外，也可以印出數字。
print　は紐をプリントアウトができる、数字もできる。
"""
print(3)

"""
最後要介紹的是 len()，可以回傳字串或其他變數的長度，其他變數會在後面依序介紹。
最後は　len()　に紹介する。これで紐の長さとか他(ほか)の変数(へんすう)の長さとかを
返事ができる。他の変数は後で紹介する。

＝＝＝＝＝
大家可以嘗試換掉雙引號當中的內容，可以更加瞭解 len() 的作用喔。
皆は二重引用符中の内容を変えてやってみる、それてもっと　len()　の効果を分かる。

＝＝＝＝＝
"Hello World"的長度是 11，因為"空格"也被算進去了。
"Hello World"の長さは　11、なぜなら、スペースも数えられるだ。
"""
print(len("Hello"))        # 5
print(len("World"))        # 5
print(len("Hello World"))  # 11
print(len("炎"))           # 1
print(len("あ"))           # 1

"""
而這個檔案(Step0_05000000.py)通常稱之為腳本。
このファイル(Step0_05000000.py)はスクリプトと呼ばれる。
"""