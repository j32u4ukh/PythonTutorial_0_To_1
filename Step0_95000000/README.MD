教學大綱；シラバス；syllabus：
1. Rotor
2. if __name__ == "__main__":

---

這次一樣要以 Enigma 中使用到的另一個物件為例。

今回も Enigma の中に使ったオブジェクトを例として。

This time we will also take another object used in Enigma as an example.

---

其內容牽涉到程式的運用與 Enigma 本身機制的理解，會較困難。

それの内容はプログラムの<ruby>使用<rt>しよう</rt></ruby>とEnigma 自身のメカニズムの理解程度を<ruby>関与<rt>かんよ</rt></ruby>してだから、もっと難しいだ。

Its content involves the use of the program and the understanding of Enigma's own mechanism, which will be more difficult.

---

可以先回頭複習當中使用到的程式，再將對 Enigma 的說明與程式碼兩者搭配一起理解。

使ったのプログラムを<ruby>復習<rt>ふくしゅう</rt></ruby>して、Enigma の説明とコードを一緒に理解する。

You can go back and review the programs used in it, and then understand the Enigma's instructions and the code together.

---

這次要實做的是"旋轉盤"，與反射板一樣是對輸入的元素進行轉換。

今回実装するのオブジェクトは’スクランブラー’、反射板と同じ、輸入の要素に<ruby>変換<rt>へんかん</rt></ruby>する。

This time we will implement the "Rotor", which is the same as the reflector to transform the input elements.

---

但不同的是，旋轉盤具有方向性且並非兩兩互換。

違うのは、スクランブラーは<ruby>方向性<rt>ほうこうせい</rt></ruby>があり、そして、ペアワイズ交換ではないだ。

But the difference is that the rotator is directional and non-pairwise interchange.

---

方向性："從輸入到反射板" 與 "從反射板到輸出"。

方向性：”輸入から反射板まで” または ”反射板から輸出まで”

Directivity: "from input to reflector" and "from reflector to output".

---

非兩兩互換："從輸入到反射板"時，a 會轉換成 b ，但 b 會轉換成 f 。"從反射板到輸出"時， b 會轉換成 a ，而 f 會轉換成 b 。
           
ペアワイズ交換ではない：”輸入から反射板まで”とき、a は b に変換してが b は f に変換する。”反射板から輸出まで”とき、b は a に変換してが f は b に変換する。

Non-pairwise interchange: When "from input to reflector", "a" will be converted to "b", but "b" will be converted to "f". When "from reflector to output", "b" will be converted to "a", and "f" will be converted to "b".

---

兩兩互換：無論方向，a 會轉換成 b ，而 b 會轉換成 a 。

ペアワイズ交換：どちらの方向でも、a は b に変換してが b は f に変換する。

Pairwise interchange: Regardless of the direction, "a" will be converted to "b", and "b" will be converted to "a".

---

Pipeline 作為'反射板'(Reflector)和'旋轉盤'(Rotor)的父類別，包含共同使用的函式或參數，可避免重複內容的撰寫。

Pipeline は反射板とスクランブラーの親オブジェクトをとして、共通の関数とパラメータを持ち、<ruby>重複<rt>じゅうふく</rt></ruby>な内容を省略してできる。

Pipeline, as the parent class of 'Reflector' and 'Rotor', contains jointly used functions or parameters, which can avoid the writing of duplicate content.

```python
class Pipeline:
    def __init__(self, items):
        self.origin_sequence = items.copy()
        self.origin_sequence.sort()

        self.shuffle_sequence = items.copy()
        self.length = len(items)

    def getIndex(self, _char):
        try:
            return self.origin_sequence.index(_char)
        except ValueError:
            return -1

    def getChar(self, index):
        if index < 0:
            index += self.length

        if self.length <= index:
            index %= self.length

        return self.origin_sequence[index]
```

旋轉盤的說明請看 PythonTutorial_0_To_1/Enigma/。

スクランブラーの説明には PythonTutorial_0_To_1/Enigma/ を見せてください。

Please see PythonTutorial_0_To_1/Enigma/ for the illustration of the Rotor.

```python
class Rotor(Pipeline):
    def __init__(self, items, pointer=0):
```

Rotor 繼承 Pipeline，Pipeline 做得到的 Rotor 一樣可以。

Rotor は Pipeline を<ruby>継承<rt>けいしょう</rt></ruby>し、Pipeline ができるなら Rotor もできる。

Rotor inherits from Pipeline, so Rotor can do what Pipeline can do.

```python
        super().__init__(items)
```

self.pointer 指向 self.forward 和 self.backward 的位置。        

self.pointer は self.forward と self.backward の<ruby>場所<rt>ばしょ</rt></ruby>を指して。

self.pointer points to the location of self.forward and self.backward.

---

當 self.pointer + 1，代表換下一組元素轉換規則。

つまり、self.pointer + 1 のとき、「要素変換ルール」は次のセットに変える。

When self.pointer + 1, it represents changing to the next set of element conversion rules.

---

模擬旋轉盤在旋轉的樣子。

スクランブラーが<ruby>回転<rt>かいてん</rt></ruby>していると同じの<ruby>効果<rt>こうか</rt></ruby>のためです。

Simulate the rotating of the rotor.

```python
        self.pointer = pointer
```

進位值，每加密多少次'更改一次加密組合' = pointer + 1 = 旋轉盤轉動一次。

キャリー値：何回暗号化したあと、暗号のルールを変える。 = pointer + 1 = スクランブラーを一度回す。

Carry value, "change a encryption set once after encrypting how many times", = pointer + 1 = rotates the rotor once.

```python
        self.carry = 1
```

紀錄加密/解密次數，用於判斷是否需要進位。

暗号化と解読することは何回をしましたを記録して、キャリーかどうかを判断する。

Record the number of encryption/decryption, used to determine whether a carry is needed.

```python
        self.counter = 0
```

self.forward 儲存'輸入往反射板'方向的元素轉換規則。

self.forward は「輸入からリフレクターへ」の「要素変換ルール」。

```python
        self.forward = []
```

self.backward 儲存'反射板往輸出'方向的元素轉換規則。

self.forward は「リフレクターから輸出へ」の「要素変換ルール」。

```python
        self.backward = []
```

初始化 self.forward 和 self.backward 的元素轉換規則。

self.forward と self.backward の「要素変換ルール」を<ruby>初期化<rt>しょきか</rt></ruby>する。

```python
        self.setSwap()
```

根據建立物件時傳入的 items 來形成元素轉換規則。

オブジェクトを建立している時の items で、「要素変換ルール」を決める。

```python
    def setSwap(self):
```

初始化 self.forward 和 self.backward，長度為 self.length。

self.forward と self.backward を初期化して、長さは self.length。

```python
        self.forward = [0 for _ in range(self.length)]
        self.backward = [0 for _ in range(self.length)]
```

self.shuffle_sequence 保存了 items 的原始順序，因此以下透過 self.shufEnigmafle_sequence 來存取元素。

self.shuffle_sequence は items 元の順番は保存したので、下は self.shuffle_sequence から要素をアクセスする。

```python
        for i in range(self.length):
```

取得 'self.shuffle_sequence' 第 i 個元素，命名為 curr_char。

self.shuffle_sequence の第 i 目要素をアクセスして、curr_char を命名する。

---

再取得 curr_char 在'self.origin_sequence'中的索引值，命名為 curr_index 。

そして、self.origin_sequence 中の curr_char のインデックスをもって、curr_index を命名する。

---

注意：這裡使用了'順序不同'但'元素相同'的兩個陣列。

注意：ここは「順番は違うでも要素は同じ」の二つ配列を使いました。

```python
            curr_char = self.shuffle_sequence[i]
            curr_index = self.getIndex(curr_char)
```

next_idx 為下一個索引值，若超過陣列範圍，則索引值設為 0。

next_idx は次のインデックス、もし配列の範囲を<ruby>超<rt>こ</rt></ruby>えて、インデックスが 0 になる。

```python
            next_idx = i + 1
            if next_idx == self.length:
                next_idx = 0
```

同樣，取得 'self.shuffle_sequence' 第 next_idx 個元素，命名為 next_char。

self.shuffle_sequence の第 next_idx 目要素をアクセスして、next_char を命名する。

---

再取得 next_char 在'self.origin_sequence'中的索引值，命名為 next_index 。

そして、self.origin_sequence 中の next_char のインデックスをもって、next_index を命名する。

```python
            next_char = self.shuffle_sequence[next_idx]
            next_index = self.getIndex(next_char)
```

原始陣列；元の配列

self.shuffle_sequence = items.copy() = ['ㄅ', 'あ', 'a']

---

排序後形成；順番を並んだ後の配列

self.origin_sequence = items.copy().sort() = ['a', 'あ', 'ㄅ']

---

元素轉換規則(curr_char → next_char)；要素変換ルール

元素:   'ㄅ' → 'あ'；'あ' → 'a'；'a' → 'ㄅ'

索引;インデックス:         2   →  1  ； 1   →  0 ； 0  →  2

索引變化;インデックスの変化:    -1    ；     -1   ；    +2

self.forward = [-1, -1, +2]

---

注意：元素和索引分別參考不同陣列。

注意：要素とインデックスは別々の配列をからだ。

```python
            _next_gap = next_index - curr_index
            self.forward[curr_index] = _next_gap
```

正序的元素交換規則與反序地剛好互相對應。

輸入からの要素変換ルールと輸出からのルールを対して。

---

例如：正序時，第 0 個元素 +3 變為第 3 個元素；反序時，第 3 個元素 -3 變為第 0 個元素。

例えば、輸入からとき、第 0 目要素 3 を足すと第 3 目要素になて、そして、輸出からとき、第 3 目要素 3 をひくと第 3 目要素になる。

---

self.forward 和 self.backward 中儲存的值代表的意義請在此理解清楚，可以畫在紙上幫助你思考。

self.forward と self.backward に保存した数値の意味をここで理解してください、紙で書いて考えることに助けて。

---

當中的值本文中會稱為'元素轉換規則'或'偏移值'，請記得這兩個詞的意義。

この数値が'要素変換ルール'または'オフセット值'と呼ばれて、この二つ<ruby>言葉<rt>ことば</rt></ruby>の意味を覚えてください。

---

第 0 個元素變為第 3 個元素，'偏移值'為 +3。

要素変換ルールは”第 0 目要素を第 3 目要素になて”の場合なら、オフセット值は +3。

---

第 7 個元素變為第 2 個元素，'偏移值'為 -5。

要素変換ルールは”第 7 目要素を第 2 目要素になて”の場合なら、オフセット值は -5。


```python
            for i in range(self.length):
                _back_index = i + self.forward[i]
                self.backward[_back_index] = -self.forward[i]
```

'輸入往反射板'方向的元素轉換。

”輸入から反射板まで”の方向の要素変換。

```python
    def forwardSwap(self, input_data):
```

加密/解密次數 +1。

暗号化と解読することの回数に 1 を足す。

```python
        self.counter += 1
```

取得輸入元素在 self.origin_sequence 當中的索引值。

輸入要素は self.origin_sequence のどこにいます、そのインデックスをもらう。

```python
        index = self.getIndex(input_data)
```

下方兩行應一起理解。

下の二つ行を一緒に理解してべきだ。

---

index + self.forward[swap_index] 表示原本的元素索引值變成新的索引值。

index + self.forward[swap_index] の意味は本来の要素のインデックスを新しいインデックスになって。

---

例如：0 → 3；7 → 2，達到元素轉換的效果。

例えば、0 → 3；7 → 2、要素変換の効果を到達する。

---

原本元素在陣列中第幾個位置(index)，就會採用 self.forward 中第幾個位置的'偏移值'。

元の要素は配列の第何目(index)、self.forward の第何目のオフセット值を使って。

---

但這裡又加上 self.pointer，本次的轉換就會採用 self.forward 中第 (index + self.pointer) 個位置的'偏移值'。

でもここはその上で self.pointer を足して、self.forward の第 (index + self.pointer) 目のオフセット值を使う。

---

後面的'% self.length'是在確保前面數值不會超過陣列範圍。

後ろの '% self.length' は前の数値が配列の範囲を超えらないを<ruby>確保<rt>かくほ</rt></ruby>する。

```python
        swap_index = (index + self.pointer) % self.length
        output_data = index + self.forward[swap_index]
```

index + self.forward[swap_index] 後的 output_data 或許會超過陣列範圍。

index + self.forward[swap_index] 後の output_data は配列の範囲に超えてかもしれません。

---

透過 self.getChar 回傳元素，確保它不會超過陣列範圍。

self.getChar を使って要素を戻り、範囲を超えらないを確保する。

```python
        return self.getChar(output_data)
```

'反射板往輸出'方向的元素轉換規則。

'反射板から輸出まで'方向の要素変換ルール。

```python
    def backwardSwap(self, input_data):
```

取得輸入元素在 self.origin_sequence 當中的索引值。

輸入要素は self.origin_sequence のどこにいます、そのインデックスをもらう。

```python
        index = self.getIndex(input_data)
```

基本上和 forwardSwap 相同，但'偏移值'的來源從 self.forward 變成 self.backward。

forwardSwap と<ruby>殆<rt>ほとん</rt></ruby>ど同じが、オフセット值は self.forward からでなく、self.backward からです。

```python
        swap_index = (index + self.pointer) % self.length
        output_data = index + self.backward[swap_index]

        return self.getChar(output_data)
```

檢查是否需要轉動旋轉盤，即 self.pointer += 1。

スクランブラーを回すの必要かどうかチェックして、つまり、self.pointer += 1。

```python
    def checkRotate(self):
```

加密/解密次數(self.counter) 被 進位值(self.carry) 整除，轉動旋轉盤一次。

暗号化と解読することの回数はキャリー値に割り切れる場合なら、スクランブラーを<ruby>回<rt>まわ</rt></ruby>して一回。

```python
        if self.counter % self.carry == 0:
```

轉動旋轉盤，改變元素轉換規則。

スクランブラーを回して、要素変換ルールを変える。

```python
            self.pointer += 1
            self.pointer = self.pointer % self.length
```

完整版；完全版；Full version

```python
class Rotor(Pipeline):
    def __init__(self, items, pointer=0):
        super().__init__(items)
        self.pointer = pointer
        self.carry = 1
        self.counter = 0
        self.forward = []
        self.backward = []
        self.setSwap()

    def setSwap(self):
        self.forward = [0 for _ in range(self.length)]
        self.backward = [0 for _ in range(self.length)]

        for i in range(self.length):
            curr_char = self.shuffle_sequence[i]
            curr_index = self.getIndex(curr_char)

            next_idx = i + 1
            if next_idx == self.length:
                next_idx = 0

            next_char = self.shuffle_sequence[next_idx]
            next_index = self.getIndex(next_char)

            _next_gap = next_index - curr_index
            self.forward[curr_index] = _next_gap

            for i in range(self.length):
                _back_index = i + self.forward[i]
                self.backward[_back_index] = -self.forward[i]

    def forwardSwap(self, input_data):

        self.counter += 1

        index = self.getIndex(input_data)

        swap_index = (index + self.pointer) % self.length
        output_data = index + self.forward[swap_index]

        return self.getChar(output_data)

    def backwardSwap(self, input_data):

        index = self.getIndex(input_data)

        swap_index = (index + self.pointer) % self.length
        output_data = index + self.backward[swap_index]

        return self.getChar(output_data)

    def checkRotate(self):
        if self.counter % self.carry == 0:
            self.pointer += 1
            self.pointer = self.pointer % self.length
```

```python
def rotorTest():
    items = ['H', 'e', 'l', 'o', 'W', 'r', 'd', 's']

    rotor = Rotor(items)
    print("origin: {}".format(rotor.origin_sequence))
    print("shuffle: {}".format(rotor.shuffle_sequence))

    for idx in range(rotor.length):
        if idx == (rotor.length - 1):
            next_idx = 0
        else:
            next_idx = idx + 1

        curr_shuffle_char = rotor.shuffle_sequence[idx]
        next_shuffle_char = rotor.shuffle_sequence[next_idx]

        curr_origin_idx = rotor.getIndex(curr_shuffle_char)
        next_origin_idx = rotor.getIndex(next_shuffle_char)

        print("element {} change to element {}".format(
            curr_origin_idx,
            next_origin_idx))
```

之前的課程曾經介紹過 import ，透過 import 可以將之前寫好的程式碼再次拿來使用。

前のチュートリアルは import を紹介した、import で書いたコードをもう一度利用する。

---

但若這個腳本中不只有單純定義函式或物件，還使用了它們，那再使用 import 的同時，這些程式碼也都會被執行。

だが、もしこのスクリプトの中には関数とオブジェクトだけでなく、他のコードを実行するもありますなら、import を利用するとき、それも実行されている。

---

為避免上述情形，就要透過 if __name__ == "__main__": 這行程式碼，只有在符合 __name__ == "__main__" 的條件下，下方的程式碼才會被執行。

上の状況を<ruby>避<rt>さ</rt></ruby>けるため、コード if __name__ == "__main__": を利用して、条件 __name__ == "__main__" が満たされている場合は下のコードを行されている。

---

而 __name__ == "__main__" 表示的就是這段程式碼是被當前這個腳本所執行，而不是透過 import 而被執行的。

__name__ == "__main__" の意味は”今のコードが今のスクリプトに実行されて、import されるではない”。

```python
if __name__ == "__main__":
    rotorTest()
```
