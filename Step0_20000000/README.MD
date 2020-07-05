教學大綱；シラバス；syllabus：
1. True, False
2. and, or, not

---

True 和 False 是邏輯型的資料，正確或不正確，有效或無效，相等或不相等，以此類推。

True と False はロジックタイプのデータ。例えば：正解またはエラー？<ruby>有効<rt>ゆうこう</rt></ruby>または<ruby>無効<rt>むこう</rt></ruby>？等しいか等しくないか？

"True" and "False" are logical data, correct or incorrect, valid or invalid, equal or unequal, and so on.

```python
print(2 > 1)  # True
print(2 < 1)  # False
```

True 和 False 之間互相組合，可以產生許多變化。組合則是透過 and, or, not 等來達到。

True と False を<ruby>互<rt>たが</rt></ruby>いに<ruby>結合<rt>けつごう</rt></ruby>して、<ruby>色<rt>いろ</rt></ruby>んな変化が出る。組み合わせは and, or, not を通じて達成される。

"True" and "False" can combine with each other to create many different combination. By using "and", "or", "not" to produce different combination.

* <ruby>出<rt>だ</rt></ruby>せる：他動詞

---

and: 都是 True 才會是 True。

and: 全部 True だったら、結果が True になる。

"and": If components are all "True", and the result is "True".

* 〜を〜にする: 把它變成
* 〜が〜になる: 自然而然變成

```python
print(True and True)    # True
print(True and False)   # False
print(False and False)  # False
```

or: 其中一個 True 就會是 True。

or: ある一つの True は結果が True になる。

"or": One of components is "True", and the result is "True".

```python
print(True or True)    # True
print(True or False)   # True
print(False or False)  # False
```

not: True → False, False → True。

not: not を入れたら、True が False になり、False が True になる。

"not": Reverse the result between "True" and "False".

```python
print(not True)    # False
print(not False)   # True
```