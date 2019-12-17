"""
教學大綱；シラバス；syllabus：
1. if else
2. elif

這裡要介紹條件判斷的用法，白話來說就是執行：判斷是否正確，正確的話做什麼，不正確的話
做什麼。
ここに条件を判断することを紹介します。つまり、正しいかどうかを判断して、正しい場合と
正しくない場合、別々に説明します。

＝＝＝＝＝
if 後面接了條件句，條件句的結果是 True 或 False 這兩種邏輯型的資料。
if　の後は条件、その結果が True または False 、この二種類ロジックタイプのデータ。
"""
condition = True
if condition:  # if 條件
    print("I'm smart.")  # 正確的話做什麼
else:  # 否則
    print("It is impossible.")

"""
如果像前面的範例，在條件的部分直接寫 True，這麼做的意義不大，我們可以用來檢查一個字串
長度是否超過 5。
前の例と同じ、条件の部分直接 True に入れでなら、意味がないと思います。下は紐の長さが
五より大きいかどうか確認する。
"""
string = "Hello World"
if len(string) > 5:
    print("Length is longer than 5.")
else:
    print("Length is shorter than 5.")

string = "Hello"
if len(string) > 5:
    print("Length is longer than 5.")
else:
    print("Length is shorter than 5.")

"""
從這兩個範例，可以看到條件判斷都相同，輸入不同的字串就有了不同的結果。
この二つの例を見て、同じ条件の場合に、違う紐をあげて違う結果が得られった(うられった)。

＝＝＝＝＝
if else 將情況做了二分法，只有是或不是，在實際使用上也會出現三種(或以上)情況的時候，
就必須寫兩層  if else，實在不太方便。
if と else は状況を二種類に分かれています。でも、実際に使って時、三種類以上の場合は
沢山あります。if と else 二回以上をかけなければなりません、本当に不便だ。

＝＝＝＝＝
因此可以使用 elif，在第一個 if 判斷完之後繼續判斷，全部條件都不符合後才執行 else 
裡面的內容。
だから、 elif を使って、最初の判断したあと、続けて判断します。全ての条件が満たされない
(みたされない)後に実行する。

＝＝＝＝＝
下面兩種寫法等價，但使用 elif 可讓程式碼較簡潔。
したの二つ方法は同じ効果ができて、でも、 elif を使うならコードが簡潔(かんけつ)に
なります。
"""
number = 3

if number == 1:
    print("number is 1.")
else:
    if number == 2:
        print("number is 2.")
    else:
        if number == 3:
            print("number is 3.")
        else:
            if number == 4:
                print("number is 4.")
            else:
                print("number is 5.")

if number == 1:
    print("number is 1.")
elif number == 2:
    print("number is 2.")
elif number == 3:
    print("number is 3.")
elif number == 4:
    print("number is 4.")
else:
    print("number is 5.")
