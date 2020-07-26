教學大綱；シラバス；syllabus：
1. 十進制；１０進數; Decimal
2. 二進制；バイナリ; Binary
3. 二進制應用；バイナリの<ruby>申<rt>もう</rt></ruby>し込み; application of binary 

---

一般我們所在使用的數字就是"十進制"，應該很好理解，數字為 0~9，超過 9 就會進位變成 10。

普通私たちが使っている数字は"10進數"で理解しやすいだろう。数字の<ruby>範囲<rt>はんい</rt></ruby>は 0 から 9 まで。9 を<ruby>超<rt>こ</rt></ruby>えたら、キャリーが発生し、9 が 10 になる。

Gernally, the number we use is "decimal". I think this is easily to understand, the range of number is from 0 to 9, if it exceeds 9, it will carry to 10.

* "10進數"で理解：不能直接接句子，改使用中止型的 で 來連接
* キャリー: 當作名詞

---

而"二進制"是電腦的進位方式，數字為 0~1，超過 1 就會進位變成 10，通常會 8 位或 16 位一起寫。

そして、バイナリとはコンピューターがキャリーするやり方。数字の範囲は 0 から 1 までで、1 を超えたら、数字が 10 になる。普通、8 桁か 16 桁で<ruby>表示<rt>ひょうじ</rt></ruby>する。

"Binary" is the way computers use, the range of number is from 0 to 1, if it exceeds 1, it will carry to 10. Usally uses with 8 or 16 numbers to represent a value.

* するのやり方 -> するやり方: する、動詞原型、普通型 可以直接接名詞。
* <ruby>桁<rt>けた</rt></ruby>: 位數。
* 數字:直書時用漢字；橫書用阿拉伯數字。

---

例(左邊十進制，右邊二進制)

例えば(左側は" 10 進數"、右側はバイナリ)

For example (the left side is decimal, and the right side is binary)

0  → 00000000
1  → 00000001
2  → 00000010
3  → 00000011
4  → 00000100
...
10 → 00001010
11 → 00001011

---

透過 Python 內建方法可輕鬆的進行十進制和二進制兩者的轉換。

Python 組み込み<ruby>関数<rt>かんすう</rt></ruby>で" 10 進數"とバイナリの間に楽に変換できる。

By using Python's build in function, it will easily to transform between decimal and binary.

* メソッド 方法
* 楽に：和動詞放在一起，順序對其實就可以，但放一起可明確表示是在形容誰。

```python
decimal = 11
binary = "1011"
# 十進制 → 二進制
print(bin(decimal))

# 二進制 → 十進制
print(int(binary, 2))
```

接著是本篇的重點，二進制應用。在這個專案的利用上是判斷奇偶。

そして、今回のポイントは、バイナリの申し込みだ。バイナリはこのプロジェクトで奇数または偶数を判断するのに使う。

It is coming to the focal point of this article, binary applications. It will use to determine a number is odd or even in this project.

* <ruby>焦点<rt>しょうてん</rt></ruby>
*　のに： 表用途，後接特定動詞 EX 使う、ひつよう

---

判斷奇偶可也可用之前教的"%"，但利用二進制的性質，可以更有效率的進行。

奇数または偶数は前教えた "%" でも判断できるけど、バイナリの<ruby>性質<rt>せいしつ</rt></ruby>を利用すると、もっと効率的に実行できる。

To determine a number is odd or even can use "%" which we had been teached symbol, but to use the feature of binary can be more efficiently.

11 → 00001011
1  → 00000001

* パリティ 奇偶性
* 以前: 用於時間點的劃分(多用於久遠的時間點)； 前: 較近時間點的之前
*　効率的な -> 効率的に: 形容詞變副詞 な -> に

```python
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
```