"""
教學大綱；シラバス；syllabus：
1. Rotor
2. if __name__ == "__main__":

這次一樣要以 Enigma 中使用到的另一個物件為例，其內容牽涉到程式的運用與 Enigma 本身
機制的理解，會較困難，可以先回頭複習當中使用到的程式，再將對 Enigma 的說明與程式碼
兩者搭配一起理解。
今回も Enigma の中に使ったオブジェクトを例として、それの内容はプログラムの使用(しよう)と
Enigma 自身のメカニズムの理解程度を関与(かんよ)してだから、もっと難しいだ。使ったのプログラムを
復習(ふくしゅう)して、 Enigma の説明とコードを一緒に理解する。

＝＝＝＝＝
這次要實做的是"旋轉盤"，與反射板一樣是對輸入的元素進行轉換，但不同的是，旋轉盤具有
方向性且並非兩兩互換。
今回実装するのは’スクランブラー’、反射板と同じ、輸入の要素に変換(へんかん)している。違うのは、スクランブラーは
方向性(ほうこうせい)があります、そして、ペアワイズ交換ではないだ。

＝＝＝＝＝
方向性："從輸入到反射板" 與 "從反射板到輸出"。
方向性：”輸入から反射板まで” または ”反射板から輸出まで”

＝＝＝＝＝
非兩兩互換："從輸入到反射板"時， a 會轉換成 b ，但 b 會轉換成 f 。
           "從反射板到輸出"時， b 會轉換成 a ，而 f 會轉換成 b 。
ペアワイズ交換ではない：”輸入から反射板まで”とき、 a は b に変換してが b は f に変換する。
                    　”反射板から輸出まで”とき、 b は a に変換してが f は b に変換する。

＝＝＝＝＝
兩兩互換：無論方向，a 會轉換成 b ，而 b 會轉換成 a 。
ペアワイズ交換：どちらの方向でも、 a は b に変換してが b は f に変換する。

＝＝＝＝＝
Pipeline 作為'反射板'(Reflector)和'旋轉盤'(Rotor)的父類別，包含共同使用的函式或參數
，可避免重複內容的撰寫。
Pipeline は反射板とスクランブラーの親オブジェクトをとして、共通の関数とパラメータを持って、
重複な内容を省略してできる。
"""


class Pipeline:
    def __init__(self, _items):
        self.origin_sequence = _items.copy()
        self.origin_sequence.sort()

        self.shuffle_sequence = _items.copy()
        self.length = len(_items)

    def getIndex(self, _char):
        try:
            return self.origin_sequence.index(_char)
        except ValueError:
            return -1

    def getChar(self, _index):
        if _index < 0:
            _index += self.length

        if self.length <= _index:
            _index %= self.length

        return self.origin_sequence[_index]


"""
旋轉盤的說明請看 PythonTutorial_0_To_1/Enigma/。

スクランブラーの説明には PythonTutorial_0_To_1/Enigma/ を見せてください。
"""


class Rotor(Pipeline):
    def __init__(self, _items, _pointer=0):
        """
        Rotor 繼承 Pipeline，Pipeline 做得到的 Rotor 一樣可以。

        Rotor は Pipeline を継承(けいしょう)して、Pipeline ができるなら Rotor もできる。
        """
        super().__init__(_items)

        """
        self.pointer 指向 self.forward 和 self.backward 的位置，
        當 self.pointer + 1，代表換下一組元素轉換規則，模擬旋轉盤在旋轉的樣子。        
        
        self.pointer　は　self.forward と self.backward　の場所（ばしょ）を指して。
        つまり、self.pointer + 1　のとき、「要素変換ルール」は次のセットに変える。
        スクランブラーが回転（かいてん）していると同じの効果（こうか）のためです。
        """
        self.pointer = _pointer

        """
        進位值，每加密多少次'更改一次加密組合' = pointer + 1 = 旋轉盤轉動一次。
        
        キャリー値：何回暗号化したあと、暗号のルールを変える。 = pointer + 1 = スクランブラーを一度回す。
        """
        self.carry = 1

        """
        紀錄加密/解密次數，用於判斷是否需要進位。
        
        暗号化と解読することは何回をしましたを記録して、キャリーかどうかを判断する。
        """
        self.counter = 0

        """
        self.forward 儲存'輸入往反射板'方向的元素轉換規則。

        self.forward　は「輸入からリフレクターへ」の「要素変換ルール」。
        """
        self.forward = []

        """
        self.backward 儲存'反射板往輸出'方向的元素轉換規則。

        self.forward　は「リフレクターから輸出へ」の「要素変換ルール」。
        """
        self.backward = []

        """
        初始化 self.forward 和 self.backward 的元素轉換規則。

        self.forward と self.backward　の「要素変換ルール」を初期化（しょきか）する。
        """
        self.setSwap()

    """
    根據建立物件時傳入的 _items 來形成元素轉換規則。

    オブジェクトを建立している時の　_items　で、「要素変換ルール」を決める。
    """

    def setSwap(self):
        """
        初始化 self.forward 和 self.backward，長度為 self.length。

        self.forward と self.backward を初期化(しょきか)して、長さは self.length。
        """
        self.forward = [0 for _ in range(self.length)]
        self.backward = [0 for _ in range(self.length)]

        """
        self.shuffle_sequence 保存了 _items 的原始順序，因此以下透過 self.shufEnigmafle_sequence
        來存取元素。
        
        self.shuffle_sequence は _items 元の順番は保存したので、下は self.shuffle_sequence から
        要素をアクセスする。
        """
        for i in range(self.length):
            """
            取得'self.shuffle_sequence'第 i 個元素，命名為 _curr_char。
            再取得 _curr_char 在'self.origin_sequence'中的索引值，命名為 _curr_index 。
            注意：這裡使用了'順序不同'但'元素相同'的兩個陣列。
            
            self.shuffle_sequence の第 i 目要素をアクセスして、 _curr_char と読んで、
            そして、 self.origin_sequence 中の _curr_char のインデックスをもって、 _curr_index と呼びます。
            注意：ここは「順番は違うでも要素は同じ」の二つ配列を使いました。
            """
            _curr_char = self.shuffle_sequence[i]
            _curr_index = self.getIndex(_curr_char)

            """
            _next 為下一個索引值，若超過陣列範圍，則索引值設為 0。
            
            _next は次のインデックス、もし配列の範囲を超えて(こえて)、インデックスが 0 になる。
            """
            _next = i + 1
            if _next == self.length:
                _next = 0

            """
            同樣，取得'self.shuffle_sequence'第 _next 個元素，命名為 _next_char 。
            再取得 _next_char 在'self.origin_sequence'中的索引值，命名為 _next_index 。
            
            self.shuffle_sequence の第 _next 目要素をアクセスして、 _next_char と読んで、
            そして、 self.origin_sequence 中の _next_char のインデックスをもって、 _next_index と呼びます。
            """
            _next_char = self.shuffle_sequence[_next]
            _next_index = self.getIndex(_next_char)

            """
            原始陣列；元の配列
            self.shuffle_sequence = _items.copy() = ['ㄅ', 'あ', 'a']
            
            ＝＝＝＝＝
            排序後形成；順番を並んだ後の配列
            self.origin_sequence = _items.copy().sort() = ['a', 'あ', 'ㄅ']
            
            ＝＝＝＝＝
            元素轉換規則(_curr_char → _next_char)；要素変換ルール
            元素:   'ㄅ' → 'あ'；'あ' → 'a'；'a' → 'ㄅ'
            索引:    2   →  1  ； 1   →  0 ； 0  →  2    （インデックス）
            索引變化:    -1    ；     -1   ；     +2      （インデックス）
            self.forward = [-1, -1, +2]
            
            ＝＝＝＝＝
            注意：元素和索引分別參考不同陣列。
            注意：要素とインデックスは別々の配列をからだ。
            """
            _next_gap = _next_index - _curr_index

            self.forward[_curr_index] = _next_gap

        """
        正序的元素交換規則與反序地剛好互相對應，例如：
        正序時，第 0 個元素 +3 變為第 3 個元素；
        反序時，第 3 個元素 -3 變為第 0 個元素。
        輸入からの要素変換ルールと輸出からのルールを対して、例えば、
        輸入からとき、第 0 目要素 3 を足すと第 3 目要素になて、そして、
        輸出からとき、第 3 目要素 3 をひくと第 3 目要素になる。
        """
        for i in range(self.length):
            _back_index = i + self.forward[i]
            self.backward[_back_index] = -self.forward[i]

        """
        self.forward 和 self.backward 中儲存的值代表的意義請在此理解清楚，可以畫在
        紙上幫助你思考。當中的值本文中會稱為'元素轉換規則'或'偏移值'，請記得這兩個詞的意義。
        self.forward と self.backward に保存した数値の意味をここで理解してください、紙で書いて
        考えることに助けて。この数値が'要素変換ルール'または'オフセット值'と呼ばれて、この二つ
        言葉(ことば)の意味を覚えてください。
        
        ＝＝＝＝＝
        第 0 個元素變為第 3 個元素，'偏移值'為 +3；第 7 個元素變為第 2 個元素，'偏移值'為 -5。
        要素変換ルールは”第 0 目要素を第 3 目要素になて”の場合なら、オフセット值は +3；
        要素変換ルールは”第 7 目要素を第 2 目要素になて”の場合なら、オフセット值は -5。
        """

    """
    '輸入往反射板'方向的元素轉換。
    ”輸入から反射板まで”の方向の要素変換。
    """

    def forwardSwap(self, _input):
        """
        加密/解密次數 +1。
        暗号化と解読することの回数に 1 を足す。
        """
        self.counter += 1

        """
        取得輸入元素在 self.origin_sequence 當中的索引值。
        輸入要素は self.origin_sequence のどこにいます、そのインデックスをもらう。
        """
        _index = self.getIndex(_input)

        """
        下方兩行應一起理解，_index + self.forward[_swap_index] 表示
        原本的元素索引值變成新的索引值，例如：0 → 3；7 → 2，達到元素轉換的效果。
        下の二つ行を一緒に理解してべきだ、 _index + self.forward[_swap_index] の意味は
        本来の要素のインデックスを新しいインデックスになって、例えば、0 → 3；7 → 2、要素変換
        の効果を到達する。
        
        ＝＝＝＝＝
        原本元素在陣列中第幾個位置(_index)，就會採用 self.forward 中第幾個位置
        的'偏移值'，但這裡又加上 self.pointer，本次的轉換就會採用 self.forward 中
        第 (_index + self.pointer) 個位置的'偏移值'，後面的'% self.length'是在
        確保前面數值不會超過陣列範圍。
        元の要素は配列の第何目(_index)、 self.forward の第何目のオフセット值を使って、
        でもここはその上で self.pointer を足して、 self.forward の第 (_index + self.pointer) 目
        のオフセット值を使う。後ろの '% self.length' は前の数値が配列の範囲を超えらないを確保(かくほ)する。
        """
        _swap_index = (_index + self.pointer) % self.length
        _output = _index + self.forward[_swap_index]

        """
        _index + self.forward[_swap_index] 後的 _output 或許會超過陣列範圍，透過
        self.getChar 回傳元素，確保它不會超過陣列範圍。
        _index + self.forward[_swap_index] 後の _output は配列の範囲に超えてかもしれません、
        self.getChar を使って要素を戻って、範囲を超えらないを確保(かくほ)する。
        """
        return self.getChar(_output)

    """
    '反射板往輸出'方向的元素轉換規則。
    '反射板から輸出まで'方向の要素変換ルール。
    """

    def backwardSwap(self, _input):
        """
        取得輸入元素在 self.origin_sequence 當中的索引值。
        輸入要素は self.origin_sequence のどこにいます、そのインデックスをもらう。
        """
        _index = self.getIndex(_input)

        """
        基本上和 forwardSwap 相同，但'偏移值'的來源從 self.forward 變成 self.backward。
        forwardSwap と殆ど(ほとんど)同じが、オフセット值は self.forward からでなく、 self.backward からです。
        """
        _swap_index = (_index + self.pointer) % self.length
        _output = _index + self.backward[_swap_index]

        return self.getChar(_output)

    """
    檢查是否需要轉動旋轉盤，即 self.pointer += 1。
    スクランブラーを回すの必要かどうかチェックして、つまり、 self.pointer += 1。
    """

    def checkRotate(self):
        """
        加密/解密次數(self.counter) 被 進位值(self.carry) 整除，轉動旋轉盤一次。
        暗号化と解読することの回数はキャリー値に割り切れる場合なら、スクランブラーを回して(まわして)一回。
        """
        if self.counter % self.carry == 0:
            """
            轉動旋轉盤，改變元素轉換規則。
            スクランブラーを回して、要素変換ルールを変える。
            """
            self.pointer += 1
            self.pointer = self.pointer % self.length


def rotorTest():
    _items = ['H', 'e', 'l', 'o', 'W', 'r', 'd', 's']

    _rotor = Rotor(_items)
    print("origin: {}".format(_rotor.origin_sequence))
    print("shuffle: {}".format(_rotor.shuffle_sequence))

    for idx in range(_rotor.length):
        if idx == (_rotor.length - 1):
            next_idx = 0
        else:
            next_idx = idx + 1

        _curr_shuffle_char = _rotor.shuffle_sequence[idx]
        _next_shuffle_char = _rotor.shuffle_sequence[next_idx]

        _curr_origin_idx = _rotor.getIndex(_curr_shuffle_char)
        _next_origin_idx = _rotor.getIndex(_next_shuffle_char)

        print("element {} change to element {}".format(
            _curr_origin_idx,
            _next_origin_idx))


"""
之前的課程曾經介紹過 import ，透過 import 可以將之前寫好的程式碼再次拿來使用，但若
這個腳本中不只有單純定義函式或物件，還使用了它們，那再使用 import 的同時，這些程式碼
也都會被執行。
前のチュートリアルは import を紹介した、 import で書いたコードをもう一度利用する。だが、もしこの
スクリプトの中には関数とオブジェクトだけでなく、他のコードを実行するもありますなら、 import を利用する
とき、それも実行されている。

＝＝＝＝＝
為避免上述情形，就要透過 if __name__ == "__main__": 這行程式碼，只有在符合 
__name__ == "__main__" 的條件下，下方的程式碼才會被執行。
上の状況を避ける(さける)ため、コード if __name__ == "__main__": を利用して、条件 __name__ == "__main__" が
満たされている場合は下のコードを行されている。

＝＝＝＝＝
而 __name__ == "__main__" 表示的就是這段程式碼是被當前這個腳本所執行，而不是透過 
import 而被執行的。
__name__ == "__main__" の意味は”今のコードが今のスクリプトに実行されて、 import されるではない”。
"""
if __name__ == "__main__":
    rotorTest()
