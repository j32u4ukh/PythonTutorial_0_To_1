教學大綱；シラバス；syllabus：
1. 預設值；デフォルト値
2. assert
3. *args

---

之前提到函式可以透過參數執行'大部分相同，只有些許部分不同'的內容，這次要對參數做進一步的介紹。

この前言った、関数はパラメータで”大体同じ、少し違う内容”を実行ができる。今回はパラメータに詳しくな紹介をします。

As mentioned earlier, the function can perform'mostly the same, only slightly different' content through parameters. This time we will further introduce the parameters.

---

函式的參數可以事先給予值，如果這個數值適用我們當下的情形時，可以省略不給予值。

関数のパラメータは<ruby>事前<rt>じぜん</rt></ruby>に数値をあげて、もしこの数値が今の状況にとて適切だったら、略ことが大丈夫だ。

The parameters of the function can be given values ​​in advance. If this value is suitable for our current situation, the value assignment can be omitted.

---

下方函式中的 "multiply=2" 就是預設值的例子。

下の関数中の "multiply=2" はデフォルト値の例だ。

"Multiply=2" in the function below is an example of the default value.

---

若想修改值，就和原本教的一樣，給予想要的數值即可。

もし数値を変えたいなら、教えた通り、数値を入れていい。

If you want to modify the value, just like what we taught before to give the value what you want.

```python
def computeMultiply(_value, multiply=2):
    return _value * multiply


value = 3
value = computeMultiply(value)  # 6 = 3 * 2
print(value)
value = computeMultiply(value)  # 12 = 6 * 2
print(value)
value = computeMultiply(value, 5)  # 60
print(value)
```

我們除了可以根據參數去執行函式之外，還可以對這些參數設定一些要求與限制。

パラメータにとて関数を実行するの上に、パラメータにリクエストと<ruby>制限<rt>せいげん</rt></ruby>を加えてができる。

In addition to executing functions based on parameters, we can also set some requirements and restrictions on these parameters.

---

例如做正整數除法時，利用 "assert" 限制分母一定要大於 0。

例えば：正の整数の<ruby>割<rt>わ</rt></ruby>り算の場合に assert で<ruby>分母<rt>ぶんぼ</rt></ruby>必ず 0 大なり。

For example, when doing positive integer division, use "assert" to limit the denominator to greater than 0.

---

當不符合限制時，會報出 "AssertionError"，並回饋給使用者逗號後面的資訊。

制限に<ruby>到達<rt>とうたつ</rt></ruby>できないの場合、AssertionError が<ruby>発生<rt>はっせい</rt></ruby>して、後ろの<ruby>情報<rt>じょうほう</rt></ruby>をユーザーに伝える。

When the limit is not met, an "AssertionError" will be reported, and the information after the comma will be returned to the user.
"""

```python
def divide(numerator, denominator):
    assert denominator > 0, "分母一定要大於 0"

    return numerator / denominator


print(divide(5, -2))
print(divide(5, 2))
```

最後，如果我們在規劃函式的時候不確定會有幾個參數，在參數的地方利用 "*args" 表示不定數量參數是個好方法。

最後、もし関数を計画しているときパラメータの数量はまだ決まっていない、 *args で不確実な数量のパラメータに<ruby>表示<rt>ひょうじ</rt></ruby>してがいい方法だ。

Finally, if we are not sure about several parameters when planning a function, it is a good idea to use "*args" to indicate an indefinite number of parameters in the parameter area.

---

函式內部使用時，則不需要米字號。

関数の中に<ruby>星印<rt>ほしじるし</rt></ruby>の必要がいない。

When it is used inside a function, star signs are not required.

```python
def getSum(*args):
    cum_sum = 0
    for i in args:
        cum_sum += i

    return cum_sum


print(getSum(1, 2, 3, 4, 5))
print(getSum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
```