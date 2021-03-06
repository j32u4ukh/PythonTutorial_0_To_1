"""
教學大綱：
1. try, except
2. Error

在程式執行的過程中，有時會發生無法預期的錯誤。
プログラムを実行している途中で時々予想できないエラーが発生している。

＝＝＝＝＝
如果不是十分嚴重的問題，我們也不會希望程式因此而停止運行，因此需要使用到 try, except。
とても酷い問題じゃないなら、私たちもこの原因(げいいん)のせいてプログラムを中止(ちゅうし)したくない。
だからこそ、 try と except は必要だ。

＝＝＝＝＝
程式會先嘗試(try)執行 try 區域內的程式碼，當發生錯誤時，會執行 except 區域內的程式碼。
一般的な場合プログラムは try 下のコードを実行して、エラーが発生したら、 except 下のコードを実行する。

＝＝＝＝＝
首先示範會發生錯誤程式碼，再透過 try, except 的形式處理。以 value = 7 / 0 為例，
我們知道分母不可以是 0 ，因此此時程式會爆出下方的錯誤，
ZeroDivisionError: division by zero。
先ずはエラーが発生しているのコードを例として、そして、 try, except の形で対処して。 value = 7 / 0 を例として、
私たちは’分母(ぶんぼ)を 0 にすることはできません’が知っている、だからこの時下のようなエラーが発生する：
ZeroDivisionError: division by zero。
"""
numerator = 7
denominator = 0

# エラーがあります。
value = numerator / denominator

# エラーを対処して。
try:
    value = numerator / denominator
except ZeroDivisionError:
    print("deal with except")
    value = numerator

print("value:", value)

"""
前面的例子，除以 0 之後跳出了 ZeroDivisionError，可以猜想的到，還有其他類型的錯誤，
比如用超出陣列範圍的索引值去取出當中的值是 IndexError。
前の例には、 0 に割った(わった)後 ZeroDivisionError が発生しました、この上で想像できる、他のタイプエラーもあります。
例えば、インデックスで配列の範囲以外のところに数値を読んだら、 IndexError が発生する。

＝＝＝＝＝
利用數值去取出陣列的索引值時，使用了不存在陣列中的數值，會發生報錯 ValueError。
数値を利用して、配列のインデックス値をもらうとき、配列の中にいない数値を使ったら、 ValueError が発生する。

＝＝＝＝＝
except 區域如何處理錯誤，就看各位的需求去撰寫，這裡的作法只是示範而已。
except エリアはどうやってエラーを対処するのは皆の需要(じゅよう)によると書きます。ここの書き方はただの例です。
"""
array = [i for i in range(10) if i % 3 == 0]
print("array:", array)

try:
    print(array[5])
except IndexError:
    print("array length is {}".format(len(array)))

value = 7
try:
    print(array.index(value))
except ValueError:
    array.append(value)
    print("array:", array)
