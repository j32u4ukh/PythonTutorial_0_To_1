教學大綱；シラバス；syllabus：
1. if else
2. elif

---

這裡要介紹條件判斷的用法，白話來說就是執行：判斷是否正確，正確的話做什麼，不正確的話做什麼。

ここで条件の判断し方について紹介する。簡単に言うと、正しいかどうかを判断して、正しい場合と正しくない場合、別々に説明する。

Here we will introduce the usage of conditional judgment, in other words, determine whether it is correct, what to do if it is correct, and what to do if it is not.

に：表存在
で：在這裡幹嘛
つまり：用於結論、總結

---

if 後面接了條件句，條件句的結果是 True 或 False 這兩種邏輯型的資料。

if の後ろに条件句（く）しか来ない。条件句の結果は　True　か　False　というこの二種類のロジックタイプのデータしかない。

Condition which write after "if" has two type of logical data, "True" or "False".

```python
condition = True
if condition:  # if 條件
    print("I'm smart.")  # 正確的話做什麼
else:  # 否則
    print("It is impossible.")
```

如果像前面的範例，在條件的部分直接寫 True，這麼做的意義不大，我們可以用來檢查一個字串長度是否超過 5。

もし、前の例と同じで条件の部分そのまま True に入れたのは意味がないと思う。下は文字列の長さが五を超えるかどうか確認する。

It is not meaningful if we give "True" to the condition like the demo above. We can check whether the length of string is greater than 5 or not as a condition.

```python
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
```

從這兩個範例，可以看到條件判斷都相同，輸入不同的字串就有了不同的結果。

この二つの例から、同じ条件の場合でも、違う文字列を入力したら、違う結果を得られることが分かった。

We can see the same condition inputs with different string and get different result from these two demos.

*　この二つの例から見てみましょう: 邀約問句
*　見える：自然而然看到

---

if else 將情況做了二分法，只有是或不是，在實際使用上也會出現三種(或以上)情況的時候，就必須寫兩層 if else，實在不太方便。

"if" と "else" によって、状況が二種類に分かれている。だが、実際に使う時、三種類以上の場合は沢山ある。

そのとき、"if" と "else" 二回以上を書かなければならない、本当に不便だ。

"if" and "else" divide the situation into two, "True" or "False". But when there are three(or more) situations, we have to write two layer of "if esle", which is not convenient.

---

因此可以使用 elif，在第一個 if 判斷完之後繼續判斷，全部條件都不符合後才執行 else 裡面的內容。

だから、"elif" を使って、一番目 if を判断し終わったと続けて判断する。

全ての条件が<ruby>満<rt>み</rt></ruby>たされなっかたら "else" の内容を実行する。

So, we will determine the condition of "elif" after judgment of first "if", when these conditions are all invalid, execute the content in the "else" block.

---

下面兩種寫法等價，但使用 elif 可讓程式碼較簡潔。

下記の二つの書き方は同じ効果がある。でも、elif を使ったほうがコードが<ruby>簡潔<rt>かんけつ</rt></ruby>になる。

The following two writing styles are equivalent, but using "elif" can make the code more concise.

*　下記の書き方が二つある。

```python
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
```