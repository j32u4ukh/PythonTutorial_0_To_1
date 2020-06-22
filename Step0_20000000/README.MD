教學大綱；シラバス；syllabus：
1. True, False
2. and, or, not

---

True 和 False 是邏輯型的資料，正確或不正確，成立或不成立，相等或不相等，以此類推。

True と False はロジックタイプのデータ。例えば：正解またはエラー？<ruby>有効<rt>ゆうこう</rt></ruby>または<ruby>無効<rt>むこう</rt></ruby>？等しいか等しくないか？

```python
print(2 > 1)  # True
print(2 < 1)  # False
```

True 和 False 之間互相組合，可以產生許多變化。組合則是透過 and, or, not 等來達到。

True と False の<ruby>互<rt>たが</rt></ruby>いに<ruby>結合<rt>けつごう</rt></ruby>して、多い変化が出せます。組み合わせは and, or, not を通じて達成されます。

---

and: 都是 True 才會是 True。

and: 全部 True なら、結果を True になります。

```python
print(True and True)    # True
print(True and False)   # False
print(False and False)  # False
```

or: 其中一個 True 就會是 True。

or: ある一つ True は結果を True になります。

```python
print(True or True)    # True
print(True or False)   # True
print(False or False)  # False
```

not: True → False, False → True。

not: True を False になります、False を True になります。

```python
print(not True)    # False
print(not False)   # True
```