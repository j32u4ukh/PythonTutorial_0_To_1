教學大綱；シラバス；syllabus：
1. dict 建立；確立する
2. dict 取值；読んでいる
3. dict 新增；追加する

---

除了陣列之外，還有一種基本的資料儲存方式，叫做'字典'。

配列に加えて、「辞書」と呼ばれるデータを<ruby>保存<rt>ほぞん</rt></ruby>する基本的な方法があります。

In addition to "array", there is a basic way of storing data, called'dictionary'.

---

透過 {key1:value1, key2:value2} 的形式來組成。

{key1：value1、key2：value2}の<ruby>形式<rt>けいしき</rt></ruby>で<ruby>構成<rt>こうせい</rt></ruby>されています。

Composed in the form of {key1:value1, key2:value2}.

---

就像字典透過單字去查找單字的解釋一樣，Python 的字典透過 key 去取得它所代表的 value 。

辞書のような<ruby>単語<rt>たんご</rt></ruby>で単語の意味を見つける、Python の辞書は key でこれが表すの value 。

Just as a dictionary uses words to find the interpretation of a word, a Python dictionary uses the key to obtain the value it represents.

---

字典的建立是透過大括弧將內容包起來，先輸入 key 然後冒號後面接著它所代表的 value ，這是一組資料，要建立第二組時，一樣透過逗號將它們分開。

辞書を確立することは<ruby>中括弧<rt>ちゅうかっこ</rt></ruby>で内容を取り囲んで、コロンの左は key 、右はこれが表すの value 。これは一つグループです。グループとグループの間は読点で別れる。

The creation of the dictionary is to wrap the content through braces, first enter the key and then the colon followed by the value it represents. This is a set of data. To create the second set, they are also separated by commas.

```python
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {1: 'a', 2: 'b', 3: 'c'}
d3 = {'a': [1, 2, 3],
      'b': {"w": "up", "s": "down", "a": "left", "d": "right"}
      }
```

從上面的示範中可以知道，key 可以是字串或數字，而 value 基本上各種資料都可以放進去，甚至是在字典當中，放入另一個字典。

前の例と同じ、 key は紐とか数字とかなタイプ、 value ならはほぼ全てタイプの資料が入れられる、他の辞書までも入れられる。

As can be seen from the above demonstration, key can be a string or a number, and value can basically put all kinds of data into it, even in a dictionary, put another dictionary.

---

當我們想取出字典中的值時，有兩種方法，第一種是像陣列，在字典變數名稱後面加上中括弧，括弧當中放入要取出的值的 key 。

辞書から値を読みたいなら、二つ方法があります。一つは配列のような、変数の名前の後ろ<ruby>角括弧<rt>かくがっこ</rt></ruby>の中に key を入れて、値が読める。 

When we want to fetch the value in the dictionary, there are two methods. The first is like an array. Put the brackets after the dictionary variable name, and put the key of the value to be fetched in the brackets.

---

因為是 key ，所以也就不是從 0 開始計算了。

key だから、 0 から計算されません。

Because it is a key, it is not calculated from 0.

---

另一種則是透過 get 去取得，這種方式較為安全。因為當我們透過中括弧去取出一個不在字典當中的值時就會產生錯誤。

二つは get で読む、これはもっと安全な方法です。角括弧を使用して辞書の中にいない値を<ruby>取得<rt>しゅとく</rt></ruby>すると、エラーが<ruby>発生<rt>はっせい</rt></ruby>するためです。

The other is obtained through get, which is much more secure. Because when we take out a value that is not in the dictionary through the brackets, an error will occur.

---

但若是透過 get 去取得則只是返回 None ，不影響程式繼續執行。

もし get で読むなら、 None をもらっただけ、プログラムの実行に影響がない。

But if it is obtained by get, it will just return None, which will not affect the program to continue to run.

```python
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {1: 'a', 2: 'b', 3: 'c'}
d3 = {'a': [1, 2, 3],
      'b': {"w": "up", "s": "down", "a": "left", "d": "right"}
      }
print(d1['a'])
print(d2[1])
try:
    print(d3['c'])
except KeyError:
    print("""c 並不在 d3 的 key 當中。
c は d3 の key の中にありません。
c is not in the keys of d3.""")
     
print(d1.get('b'))
print(d2.get(4))
d3_b = d3.get('b')
print(d3_b)
print(d3.get('c'))
```

當我們想要往字典當中新增 key-value 的時候，可以透過中括弧把 key 包住，讓它等於你所希望賦予的值。

辞書の中に新しい key-value 追加しているとき、角括弧の中に key を入れて、イコールの右は値を代入する。

When we want to add key-value into the dictionary, we can wrap the key with brackets after the dictionary variable name to make it equal to the value you want to assign.

---

這點和陣列也是十分不同，陣列這樣做的話可是會報錯的。

これは配列とはとても違います、配列がそうすると、エラーが発生する。

This is very different from the array. If the array does this, an error will be reported.

```python
d1 = {'a': 1, 'b': 2, 'c': 3}
print(d1)
d1['d'] = 4
print(d1)
```