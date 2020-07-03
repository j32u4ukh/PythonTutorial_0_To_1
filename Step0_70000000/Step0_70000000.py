"""
教學大綱；シラバス；syllabus：
1. 預設值；デフォルト値
2. assert
3. *args

之前提到函式可以透過參數執行'大部分相同，只有些許部分不同'的內容，這次要對參數做
進一步的介紹。
この前言った、関数はパラメータで”大体同じ、少し違う内容”を実行ができる。今回は
パラメータに詳しくな紹介をします。

＝＝＝＝＝
函式的參數可以事先給予值，如果這個數值適用我們當下的情形時，可以省略不給予值。下方
函式中的 multiply=2 就是預設值的例子。
関数のパラメータは事前(じぜん)に数値をあげて、もしこの数値が今の状況にとて適切だったら、
略ことが大丈夫だ。下の関数中の multiply=2 はデフォルト値の例だ。

＝＝＝＝＝
若想修改值，就和原本教的一樣，給予想要的數值即可。
もし数値を変えたいなら、教えた通り、数値を入れていい。
"""


def computeMultiply(_value, multiply=2):
    return _value * multiply


value = 3
value = computeMultiply(value)  # 6 = 3 * 2
print(value)
value = computeMultiply(value)  # 12 = 6 * 2
print(value)
value = computeMultiply(value, 5)  # 60
print(value)
"""
我們除了可以根據參數去執行函式之外，還可以對這些參數設定一些要求與限制。
パラメータにとて関数を実行するの上に、パラメータにリクエストと制限(せいげん)を加えて
ができる。

＝＝＝＝＝
例如做正整數除法時，利用 assert 限制分母一定要大於 0，當不符合限制時，
會產生 AssertionError，並回饋給使用者逗號後面的資訊。
例えば：正の整数の割(わ)り算の場合に assert で分母(ぶんぼ)必ず 0 大なり、制限に
到達(とうたつ)できないの場合、 AssertionError が発生(はっせい)して、後ろの
情報(じょうほう)をユーザーに伝える。
"""


def divide(_numerator, _denominator):
    assert _denominator > 0, "分母一定要大於 0"

    return _numerator / _denominator


print(divide(5, -2))
print(divide(5, 2))
"""
最後，如果我們在規劃函式的時候不確定會有幾個參數，在參數的地方利用 *args 表示
不定數量參數是個好方法，函式內部使用時，則不需要米字號。
最後、もし関数を計画しているときパラメータの数量はまだ決まっていない、 *args で
不確実な数量のパラメータに表示(ひょうじ)してがいい方法だ。関数の中に星印(ほしじるし)
の必要がいない。
"""


def getSum(*args):
    _sum = 0
    for i in args:
        _sum += i

    return _sum


print(getSum(1, 2, 3, 4, 5))
print(getSum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
