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


class Reflector(Pipeline):
    def __init__(self, _items):
        super().__init__(_items)

    def swap(self, _input):
        _index = self.shuffle_sequence.index(_input)

        if (_index & 1) == 1:
            _char = self.shuffle_sequence[_index - 1]
        else:
            _char = self.shuffle_sequence[_index + 1]

        return _char


class Rotor(Pipeline):
    def __init__(self, _items, _pointer=0):
        super().__init__(_items)
        self.pointer = _pointer
        self.carry = 1
        self.counter = 0

        self.forward = []
        self.backward = []
        self.setSwap()

    def setSwap(self):
        self.forward = [0 for i in range(self.length)]
        self.backward = [0 for i in range(self.length)]

        for i in range(self.length):
            _curr_char = self.shuffle_sequence[i]
            _curr_index = self.getIndex(_curr_char)

            _next = i + 1
            if _next == self.length:
                _next = 0

            _next_char = self.shuffle_sequence[_next]
            _next_index = self.getIndex(_next_char)

            _next_gap = _next_index - _curr_index

            self.forward[_curr_index] = _next_gap

        for i in range(self.length):
            _back_index = i + self.forward[i]
            self.backward[_back_index] = -self.forward[i]

    def forwardSwap(self, _input):
        self.counter += 1
        _index = self.getIndex(_input)

        _swap_index = (_index + self.pointer) % self.length
        _output = _index + self.forward[_swap_index]

        return self.getChar(_output)

    def backwardSwap(self, _input):
        _index = self.getIndex(_input)

        _swap_index = (_index + self.pointer) % self.length
        _output = _index + self.backward[_swap_index]

        return self.getChar(_output)

    def checkRotate(self):
        if self.counter % self.carry == 0:
            self.pointer += 1
            self.pointer = self.pointer % self.length


"""
依照需求添加旋轉盤，由於反射板的設計，元素數量必須為偶數個。
"""


class Enigma:
    def __init__(self, _items):
        """
        建立 Enigma 的同時，會利用傳入的 _items 自動建立反射板。
        """
        self.reflector = Reflector(_items)

        """
        依序存放旋轉盤。
        """
        self.rotors = []

    """
    添加旋轉盤。
    """

    def add(self, _rotor):
        assert type(_rotor) is Rotor, "請添加旋轉盤"

        """
        將旋轉盤存放進 self.rotors 陣列。
        """
        self.rotors.append(_rotor)

    """
    添加完旋轉盤後，要進行編譯，形成右邊旋轉盤轉1圈，左邊旋轉盤轉1次。

    compile 為 Python 的內建函數，因此這個函示名稱最後面加了底線以作區別。
    """

    def compile_(self):
        _rotor_num = len(self.rotors)
        for _r in range(_rotor_num):
            if _r == 0:
                """
                第0個旋轉盤不做處理，直接繼續下一個循環。
                """
                continue
            else:
                """
                後面的旋轉盤'進位值 carry' = 前面旋轉盤的'進位值 carry' 乘以 旋轉盤一圈有幾個元素。
                """
                self.rotors[_r].carry = self.rotors[_r - 1].carry * self.rotors[_r].length

    """
    使用這個函式，將明文加密。
    """

    def swap(self, _input):
        _output = ""
        _rotor_num = len(self.rotors)

        """
        將句子或單字一次一個元素進行循環。
        """
        for _char in _input:
            """
            元素依序從輸入，經過數個反射板。
            """
            for _r in range(_rotor_num):
                _char = self.rotors[_r].forwardSwap(_char)

            """
            元素被反射板轉換成另一個元素。
            """
            _char = self.reflector.swap(_char)

            """
            元素依序從反射板，再次經過數個反射板，但這次的順序是反過來的。
            """
            for _r in range(_rotor_num - 1, -1, -1):
                _char = self.rotors[_r].backwardSwap(_char)

            """
            每加密一個元素之後，就檢查是否需要轉動旋轉盤。
            """
            for _r in range(_rotor_num):
                self.rotors[_r].checkRotate()

            """
            將加密後的元素，加入 _output。
            """
            _output += _char

        """
        全部元素被加密後都加入 _output，返回被加密後的結果。
        """
        return _output

    """
    旋轉盤加密後會旋轉，因此與最初的位置已大不相同，透過此函式重新設置個個旋轉盤的初始位置。
    """

    def setRotors(self, *args):
        for _r in range(len(self.rotors)):
            """
            counter 在記錄加密/解密次數，因為重新設置，所以 counter = 0。
            """
            self.rotors[_r].counter = 0
            try:
                """
                將第 _r 個旋轉盤初始位置設為 args 的第 _r 個值。
                """
                self.rotors[_r].pointer = args[_r]
            except:
                """
                若發生參數比旋轉盤數量少，將剩下的旋轉盤初始位置設為 0。
                """
                self.rotors[_r].pointer = 0


def reflectorTest():
    items = ['H', 'e', 'l', 'o', 'W', 'r', 'd', 's']
    reflactor = Reflector(items)
    word = "Hello"

    encode = ""
    for i in word:
        encode += reflactor.swap(i)

    print("encode:", encode)

    decode = ""
    for i in encode:
        decode += reflactor.swap(i)

    print("decode:", decode)


def rotorTest():
    _items = ['H', 'e', 'l', 'o', 'W', 'r', 'd', 's']

    _rotor = Rotor(_items, 0)
    _reflactor = Reflector(_items)
    _word = "HelloWorld"

    _encode = ""
    for i in _word:
        _char = _rotor.forwardSwap(i)
        _char = _reflactor.swap(_char)
        _encode += _rotor.backwardSwap(_char)

        _rotor.checkRotate()

    print("encode:", _encode)

    """ 還原 rotor 狀態 """
    _rotor = Rotor(_items, 0)
    _decode = ""
    for i in _encode:
        _char = _rotor.forwardSwap(i)
        _char = _reflactor.swap(_char)
        _decode += _rotor.backwardSwap(_char)

        _rotor.checkRotate()

    print("decode:", _decode)


def rotorTest2():
    _items = ['H', 'e', 'l', 'o', 'W', 'r', 'd', 's']
    _items1 = ['H', 'o', 'W', 'r', 'd', 'e', 'l', 's']
    _items2 = ['H', 'd', 's', 'e', 'l', 'o', 'W', 'r']
    _word = "HelloWorld"

    _reflactor = Reflector(_items)
    _rotor1 = Rotor(_items1, 0)
    _rotor2 = Rotor(_items2, 3)
    _rotor2.carry = len(_items2)

    _encode = ""
    for i in _word:
        _char = _rotor1.forwardSwap(i)
        _char = _rotor2.forwardSwap(_char)
        _char = _reflactor.swap(_char)
        _char = _rotor2.backwardSwap(_char)
        _encode += _rotor1.backwardSwap(_char)

        _rotor1.checkRotate()
        _rotor2.checkRotate()

    print("encode:", _encode)

    """ 還原 rotor 狀態 """
    _rotor1 = Rotor(_items1, 0)
    _rotor2 = Rotor(_items2, 3)
    _rotor2.carry = len(_items2)

    _decode = ""
    for i in _encode:
        _char = _rotor1.forwardSwap(i)
        _char = _rotor2.forwardSwap(_char)
        _char = _reflactor.swap(_char)
        _char = _rotor2.backwardSwap(_char)
        _decode += _rotor1.backwardSwap(_char)

        _rotor1.checkRotate()
        _rotor2.checkRotate()

    print("decode:", _decode)


def enigmaTest():
    _items = ['H', 'e', 'l', 'o', 'W', 'r', 'd', 's']
    _word = "HelloWorld"

    _enigma = Enigma(_items)
    _rotor = Rotor(_items, 0)
    _enigma.add(_rotor)
    _enigma.compile_()

    _encode = ""
    for i in _word:
        _encode += _enigma.swap(i)

    print("encode:", _encode)

    _enigma = Enigma(_items)
    _rotor = Rotor(_items, 0)
    _enigma.add(_rotor)
    _enigma.compile_()

    _decode = ""
    for i in _encode:
        _decode += _enigma.swap(i)

    print("decode:", _decode)


def enigmaTest2():
    _items = ['H', 'e', 'W', 'r', 'd', 's', 'l', 'o']
    _items1 = ['H', 'o', 'W', 'r', 'd', 'e', 'l', 's']
    _items2 = ['H', 'W', 'r', 's', 'e', 'l', 'o', 'd']
    _items3 = ['r', 'H', 'o', 'W', 'l', 'd', 's', 'e']
    _items4 = _items.copy()
    _items4.sort()
    _word = "HelloWorld"

    _enigma = Enigma(_items)
    _rotor1 = Rotor(_items1, 4)
    _rotor2 = Rotor(_items2, 7)
    _rotor3 = Rotor(_items3, 3)
    _rotor4 = Rotor(_items4, 9)
    _enigma.add(_rotor1)
    _enigma.add(_rotor2)
    _enigma.add(_rotor3)
    _enigma.add(_rotor4)
    _enigma.compile_()

    _encode = _enigma.swap(_word)
    print("encode:", _encode)

    _enigma.setRotors(4, 7, 3, 9)
    _decode = _enigma.swap(_encode)

    print("decode:", _decode)


def argsTest(*args):
    for i in range(5):
        print(args[i])


if __name__ == "__main__":
    #    wardTest()
    #    reflectorTest()
    #    rotorTest()
    #    rotorTest2()
    #    enigmaTest()
    enigmaTest2()
