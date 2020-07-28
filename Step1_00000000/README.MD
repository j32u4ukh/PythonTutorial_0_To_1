```python
class Pipeline:
    def __init__(self, items):
        self.origin_sequence = items.copy()
        self.origin_sequence.sort()

        self.shuffle_sequence = items.copy()
        self.length = len(items)

    def getIndex(self, char):
        try:
            return self.origin_sequence.index(char)
        except ValueError:
            return -1

    def getChar(self, _index):
        if _index < 0:
            _index += self.length

        if self.length <= _index:
            _index %= self.length

        return self.origin_sequence[_index]


class Reflector(Pipeline):
    def __init__(self, items):
        super().__init__(items)

    def swap(self, input_data):
        _index = self.shuffle_sequence.index(input_data)

        if (_index & 1) == 1:
            char = self.shuffle_sequence[_index - 1]
        else:
            char = self.shuffle_sequence[_index + 1]

        return char


class Rotor(Pipeline):
    def __init__(self, items, _pointer=0):
        super().__init__(items)
        self.pointer = _pointer
        self.carry = 1
        self.counter = 0

        self.forward = []
        self.backward = []
        self.setSwap()

    def setSwap(self):
        self.forward = [0 for _ in range(self.length)]
        self.backward = [0 for _ in range(self.length)]

        for i in range(self.length):
            _currchar = self.shuffle_sequence[i]
            _curr_index = self.getIndex(_currchar)

            _next = i + 1
            if _next == self.length:
                _next = 0

            _nextchar = self.shuffle_sequence[_next]
            _next_index = self.getIndex(_nextchar)

            _next_gap = _next_index - _curr_index

            self.forward[_curr_index] = _next_gap

        for i in range(self.length):
            _back_index = i + self.forward[i]
            self.backward[_back_index] = -self.forward[i]

    def forwardSwap(self, input_data):
        self.counter += 1
        _index = self.getIndex(input_data)

        _swap_index = (_index + self.pointer) % self.length
        output = _index + self.forward[_swap_index]

        return self.getChar(output)

    def backwardSwap(self, input_data):
        _index = self.getIndex(input_data)

        _swap_index = (_index + self.pointer) % self.length
        output = _index + self.backward[_swap_index]

        return self.getChar(output)

    def checkRotate(self):
        if self.counter % self.carry == 0:
            self.pointer += 1
            self.pointer = self.pointer % self.length
```

依照需求添加旋轉盤，由於反射板的設計，元素數量必須為偶數個。

必要によてスクランブラーを追加する。スクランブラーの設計の原因で、要素の数量は必ず偶数だ。

According to need to append rotor. Due to the design of the reflector, the number of elements must be an even number.

```python
class Enigma:
    def __init__(self, items):
```

建立 Enigma 的同時，會利用傳入的 items 自動建立反射板。

Enigma を構築しているとき、 items を利用して、自分で反射板を構築する。

It will automatically create a reflector using the items passed in, when creating Enigma.

```python
        self.reflector = Reflector(items)
```

依序存放旋轉盤。

順番にスクランブラーを追加する。

Store the rotors in order.

```python
        self.rotors = []
```

添加旋轉盤。

スクランブラーを追加する。

Add rotors.

```python
    def add(self, rotor):
        assert type(rotor) is Rotor, "請添加旋轉盤"
```

將旋轉盤存放進 self.rotors 陣列。

スクランブラーを配列 self.rotors に入れる。

Store the rotor in the self.rotors array.

```python
        self.rotors.append(rotor)
```

添加完旋轉盤後，要進行編譯。

スクランブラーを追加することは終わった後、コンパイルが必要だ。

After adding rotors, compile it.

---

形成右邊旋轉盤轉1圈，左邊旋轉盤轉1次。

右側のスクランブラーは 1 ラウンドに回して、左側のスクランブラーは 1 回に回している。

To form that the right rotor turns a circle and then the left rotor turns 1 time.

---

compile 為 Python 的內建函數，因此這個函示名稱最後面加了底線以作區別。

compile は Python 自分の関数だから、この関数の名前の後ろにボトムラインを加えて、compile との違うがわかりやすい。

compile is a built-in function of Python, so we attach an underline symbol at the end of this function name to distinguish it.

```python
    def compile_(self):
        rotor_num = len(self.rotors)
        for r in range(rotor_num):
            if r == 0:
```

第 0 個旋轉盤不做處理，直接繼續下一個循環。

第 0 目スクランブラー何も対処しない、次のループを続いて。

Do nothing at the 0th rotor and then continue  to enter the next cycle directly.

```python
                continue
            else:
```

後面的旋轉盤的'進位值 carry' = 前面旋轉盤的'進位值 carry' 乘以 旋轉盤一圈有幾個元素。

後ろのスクランブラーのキャリー値 = 前のスクランブラーのキャリー値を要素の数量にかける。

The carry value of the next rotor equals to the carry value of the previous rotor multiplied by the number of elements in one turn of the rotor.

```python
                self.rotors[r].carry = self.rotors[r - 1].carry * self.rotors[r].length
```

使用這個函式，將明文加密。

この関数を使って、クリアテキストを<ruby>暗号化<rt>あんごうか</rt></ruby>する。

Use this function to encrypt the plaintext.

```python
    def swap(self, input_data):
        output = ""
        rotor_num = len(self.rotors)
```

將句子或單字一次一個元素進行循環。

文または言葉の要素を一つつにループして。

Loop the sentence or word one element at a time.

```python
        for char in input_data:
```

元素依序從輸入，經過數個旋轉盤。

要素は順番に輸入から、数個スクランブラーを通して。

The elements will pass through several rotating disks in sequence from the input.

```python
            for r in range(rotor_num):
                char = self.rotors[r].forwardSwap(char)
```

元素被反射板轉換成另一個元素。

要素は反射板に他の要素へ変換する。

The element will be converted into another element by the reflector.

```python
            char = self.reflector.swap(char)
```

元素依序從反射板，再次經過數個旋轉盤，但這次的順序是反過來的。

要素は反射板から、数個スクランブラーを通してが、今回のスクランブラーの順番は逆だ。

The elements pass from the reflector through several rotors in sequence again, but this time the order is reversed.

```python
            for r in range(rotor_num - 1, -1, -1):
                char = self.rotors[r].backwardSwap(char)
```

每加密一個元素之後，就檢查是否需要轉動旋轉盤。

一つ要素を暗号化した後、スクランブラーを回すことが必要かどうかをチェックする。

After each element is encrypted, we will check whether the rotor needs to be rotated.

```python
            for r in range(rotor_num):
                self.rotors[r].checkRotate()
```

將加密後的元素，加入 output。

暗号化した要素が output に入れる。

Add the encrypted element to output.

```python
            output += char
```

全部元素被加密後都加入 output，返回被加密後的結果。

全ての要素は暗号化して output に入れて、暗号化するの結果を戻る。

After all elements are encrypted and are added to output, return the encrypted result.

```python
        return output
```

旋轉盤加密後會旋轉，因此與最初的位置已大不相同，透過此函式重新設置這個旋轉盤的初始位置。

暗号化した後スクランブラーが回すだから、最初の順番ととても違う、だから、この関数でこのスクランブラー最初の順番に戻す。

The rotor will rotate after doing encryption, so the current position is very different from the original position. Use this function to reset the initial position of the rotor.

```python
    def setRotors(self, *args):
        for r in range(len(self.rotors)):
```

counter 在記錄加密/解密次數，因為重新設置，所以 counter = 0。

counter は暗号化と解読することが何回をしましたを記録する。リセットするだから、counter もゼロになる。

The counter is recording the times of encryption/decryption. Because we reset it, counter = 0.

```python
            self.rotors[r].counter = 0
            try:
```

將第 r 個旋轉盤初始位置設為 args 的第 r 個值。

第 r 目スクランブラーの<ruby>位置<rt>いち</rt></ruby>は args の第 r 目数値を代入する。

Set the initial position of the r-th rotor to the r-th value of args.

```python
                self.rotors[r].pointer = args[r]
            except IndexError:
```

若發生參數比旋轉盤數量少，將剩下的旋轉盤初始位置設為 0。

もし args のパラメータの数量はスクランブラーの数量より少ないなら、残ったスクランブラーの位置が全部 0 を代入する。

If the parameter is less than the number of rotors, it will set the initial position of the remaining rotors to 0.

```python
                self.rotors[r].pointer = 0
```

完整版；完全版；Full version

```python
class Enigma:
    def __init__(self, items):
        self.reflector = Reflector(items)
        self.rotors = []

    def add(self, rotor):
        assert type(rotor) is Rotor, "請添加旋轉盤"
        self.rotors.append(rotor)

    def compile_(self):
        rotor_num = len(self.rotors)
        for r in range(rotor_num):
            if r == 0:
                continue
            else:
                self.rotors[r].carry = self.rotors[r - 1].carry * self.rotors[r].length

    def swap(self, input_data):
        output = ""
        rotor_num = len(self.rotors)

        for char in input_data:

            for r in range(rotor_num):
                char = self.rotors[r].forwardSwap(char)

            char = self.reflector.swap(char)

            for r in range(rotor_num - 1, -1, -1):
                char = self.rotors[r].backwardSwap(char)

            for r in range(rotor_num):
                self.rotors[r].checkRotate()

            output += char
        return output

    def setRotors(self, *args):
        for r in range(len(self.rotors)):
            self.rotors[r].counter = 0
            try:
                self.rotors[r].pointer = args[r]
            except IndexError:
                self.rotors[r].pointer = 0
```

```python
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
    items = ['H', 'e', 'l', 'o', 'W', 'r', 'd', 's']

    rotor = Rotor(items, 0)
    reflactor = Reflector(items)
    _word = "HelloWorld"

    _encode = ""
    for i in _word:
        char = rotor.forwardSwap(i)
        char = reflactor.swap(char)
        _encode += rotor.backwardSwap(char)

        rotor.checkRotate()

    print("encode:", _encode)

    """ 還原 rotor 狀態 """
    rotor = Rotor(items, 0)
    _decode = ""
    for i in _encode:
        char = rotor.forwardSwap(i)
        char = reflactor.swap(char)
        _decode += rotor.backwardSwap(char)

        rotor.checkRotate()

    print("decode:", _decode)


def rotorTest2():
    items = ['H', 'e', 'l', 'o', 'W', 'r', 'd', 's']
    items1 = ['H', 'o', 'W', 'r', 'd', 'e', 'l', 's']
    items2 = ['H', 'd', 's', 'e', 'l', 'o', 'W', 'r']
    _word = "HelloWorld"

    reflactor = Reflector(items)
    rotor1 = Rotor(items1, 0)
    rotor2 = Rotor(items2, 3)
    rotor2.carry = len(items2)

    _encode = ""
    for i in _word:
        char = rotor1.forwardSwap(i)
        char = rotor2.forwardSwap(char)
        char = reflactor.swap(char)
        char = rotor2.backwardSwap(char)
        _encode += rotor1.backwardSwap(char)

        rotor1.checkRotate()
        rotor2.checkRotate()

    print("encode:", _encode)

    """ 還原 rotor 狀態 """
    rotor1 = Rotor(items1, 0)
    rotor2 = Rotor(items2, 3)
    rotor2.carry = len(items2)

    _decode = ""
    for i in _encode:
        char = rotor1.forwardSwap(i)
        char = rotor2.forwardSwap(char)
        char = reflactor.swap(char)
        char = rotor2.backwardSwap(char)
        _decode += rotor1.backwardSwap(char)

        rotor1.checkRotate()
        rotor2.checkRotate()

    print("decode:", _decode)


def enigmaTest():
    items = ['H', 'e', 'l', 'o', 'W', 'r', 'd', 's']
    _word = "HelloWorld"

    _enigma = Enigma(items)
    rotor = Rotor(items, 0)
    _enigma.add(rotor)
    _enigma.compile_()

    _encode = ""
    for i in _word:
        _encode += _enigma.swap(i)

    print("encode:", _encode)

    _enigma = Enigma(items)
    rotor = Rotor(items, 0)
    _enigma.add(rotor)
    _enigma.compile_()

    _decode = ""
    for i in _encode:
        _decode += _enigma.swap(i)

    print("decode:", _decode)


def enigmaTest2():
    items = ['H', 'e', 'W', 'r', 'd', 's', 'l', 'o']
    items1 = ['H', 'o', 'W', 'r', 'd', 'e', 'l', 's']
    items2 = ['H', 'W', 'r', 's', 'e', 'l', 'o', 'd']
    items3 = ['r', 'H', 'o', 'W', 'l', 'd', 's', 'e']
    items4 = items.copy()
    items4.sort()
    _word = "HelloWorld"

    _enigma = Enigma(items)
    rotor1 = Rotor(items1, 4)
    rotor2 = Rotor(items2, 7)
    rotor3 = Rotor(items3, 3)
    rotor4 = Rotor(items4, 9)
    _enigma.add(rotor1)
    _enigma.add(rotor2)
    _enigma.add(rotor3)
    _enigma.add(rotor4)
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
```
