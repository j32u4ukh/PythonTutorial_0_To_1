# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 08:12:23 2019

@author: user
"""

"""'反射板'和'旋轉盤'的父類別，包含共同使用的函式或參數"""
class Pipeline:
    """  __init__
    建立 Pipeline 物件的同時會執行 __init__ 內定義的程式碼。
    
    オブジェクト　Pipeline　を建立（こんりゅう）する時、__init__で
    定義（ていぎ）したのコードも実行（じっこう）する。
    """
    def __init__(self, _items): 
        """
        參數 _items 提供 self.origin_sequence '順序不同'但'元素相同'的陣列，
        例如：[1, 2, 3], [1, 3, 2], [3, 1, 2]。
        
        パラメータ　_items　は　self.origin_sequence　に「順番（じゅんばん）は
        違うでも要素（ようそ）は同じ」の配列（はいれつ）を提供（ていきょう）する。
        例えば：[1, 2, 3], [1, 3, 2], [3, 1, 2]。
        """
        self.origin_sequence = _items.copy()
        
        """
        將 self.origin_sequence 排序，獲得相同順序的元素陣列。
        例如：[1, 3, 2], [3, 1, 2] → [1, 2, 3], [1, 2, 3]。
        
        同じ順番の要素配列のために、self.origin_sequence を並べ替えする。
        例えば：[1, 3, 2], [3, 1, 2] → [1, 2, 3], [1, 2, 3]。
        """
        self.origin_sequence.sort()
        
        """
        self.shuffle_sequence 保留原本輸入時的順序，用於建立元素轉換規則，
        例如：1 → 2；5 → 3；2 → 7。
        
        輸入（ゆにゅう）したの順番を保存するの　self.shuffle_sequence で「要素変換
        （へんかん）ルール」を建立する。
        """
        self.shuffle_sequence = _items.copy()
        
        """
        self.length 儲存陣列長度。
        
        self.length　は配列の長さを保存する。
        """
        self.length = len(_items)
        
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
        self.pointer 指向 self.forward 和 self.backward 的位置，
        當 self.pointer + 1，代表換下一組元素轉換規則，模擬旋轉盤在旋轉的樣子。
        
        self.pointer　は　self.forward と self.backward　の場所（ばしょ）を指して。
        つまり、self.pointer + 1　のとき、「要素変換ルール」は次のセットに変える。
        スクランブラーが回転（かいてん）していると同じの効果（こうか）のためです。
        """
        self.pointer = 0
        
        """
        初始化 self.forward 和 self.backward 的元素轉換規則。
        
        self.forward と self.backward　の「要素変換ルール」を初期化（しょきか）する。
        """
        self.setSwap()
    
    """
    返回 _char 在 self.origin_sequence 中的索引值，若不在當中則返回 -1。
    """    
    def getIndex(self, _char):        
        try:
            """
            返回 _char 在 self.origin_sequence 中的索引值，若不在當中則產生 ValueError。
            """
            return self.origin_sequence.index(_char)        
        except ValueError:
            """
            _char 不在 self.origin_sequence 當中，則返回 -1。尚未處理返回 -1時的情形。
            """
            return -1
    
    """
    根據索引值取得字元，處理超出範圍的索引值，使其產生以下效果：
    索引值最後一位 +1 後回到第一位，同樣的，第一位 -1 後回到最後一位。
    """
    def getChar(self, _index):
        """
        索引值小於0時，索引值加陣列長度。
        """
        if _index < 0:
            _index += self.length
        
        """
        索引值大於陣列長度時，索引值取'除以陣列長度'後的餘數。
        """
        if self.length <= _index:
            _index %= self.length
        
        """
        返回調整後的索引值指向的陣列中的字元。
        """
        return self.origin_sequence[_index]
    
    """
    根據建立物件時傳入的 _items 來形成元素轉換規則，細節請看 PythonTutorial_0_To_1/Enigma/。
    
    オブジェクトを建立している時の　_items　で、「要素変換ルール」を決める。
    詳しくな紹介なら、PythonTutorial_0_To_1/Enigma/　を見てください。
    """    
    def setSwap(self):
        """
        初始化 self.forward 和 self.backward，長度為 self.length。
        """
        self.forward = [0 for i in range(self.length)]
        self.backward = [0 for i in range(self.length)]
        
        """
        self.shuffle_sequence 保存了 _items 的原始順序，因此以下透過 self.shuffle_sequence
        來存取元素。        
        """
        for i in range(self.length):
            """
            取得'self.shuffle_sequence'第 i 個元素，命名為 _curr_char。
            再取得 _curr_char 在'self.origin_sequence'中的索引值，命名為 _curr_index 。
            注意：這裡使用了'順序不同'但'元素相同'的兩個陣列。
            """
            _curr_char = self.shuffle_sequence[i]
            _curr_index = self.getIndex(_curr_char)
            
            """
            _next 為下一個索引值，若超過陣列範圍，則索引值設為 0。 
            """
            _next = i + 1            
            if _next == self.length:
                _next = 0
            
            """
            同樣，取得'self.shuffle_sequence'第 _next 個元素，命名為 _next_char 。
            再取得 _next_char 在'self.origin_sequence'中的索引值，命名為 _next_index 。
            """
            _next_char = self.shuffle_sequence[_next]
            _next_index = self.getIndex(_next_char)
            
            """
            原始陣列
            self.shuffle_sequence = _items.copy() = ['ㄅ', 'あ', 'a']
            
            排序後形成
            self.origin_sequence = _items.copy().sort() = ['a', 'あ', 'ㄅ']
            
            元素轉換規則(_curr_char → _next_char)
            元素:   'ㄅ' → 'あ'；'あ' → 'a'；'a' → 'ㄅ'
            索引:    2   →  1  ； 1   →  0 ； 0  →  2
            索引變化:    -1    ；     -1   ；     +2
            self.forward = [-1, -1, +2]
            
            注意：元素和索引分別參考不同陣列。
            """
            _next_gap = _next_index - _curr_index
                
            self.forward[_curr_index] = _next_gap
        
        """
        正序的元素交換規則與反序地剛好互相對應，例如：
        正序時，第 0 個元素 +3 變為第 3 個元素；
        反序時，第 3 個元素 -3 變為第 0 個元素。
        """
        for i in range(self.length):
            _back_index = i + self.forward[i]                
            self.backward[_back_index] = -self.forward[i]
            
        """
        self.forward 和 self.backward 中儲存的值代表的意義請在此理解清楚，可以畫在
        紙上或執行函式 wardTest()，幫助你思考。當中的值本文中會稱為'元素轉換規則'或
        '偏移值'，請記得這兩個詞的意義。
        
        第 0 個元素變為第 3 個元素，'偏移值'為 +3；第 7 個元素變為第 2 個元素，'偏移值'為 -5。
        """


"""
反射板的說明請看 PythonTutorial_0_To_1/Enigma/。
"""
class Reflector(Pipeline):
    def __init__(self, _items):
        """
        Reflector 繼承 Pipeline，Pipeline 做得到的 Reflector 一樣可以。
        super().__init__(_items) 執行了 Pipeline 當中的 __init__()，
        並給予參數 _items。
        """
        super().__init__(_items)
    
    """
    Reflector 的設計為兩兩互換，這裡讓第 0 和第 1 互換，第 2 和第 3 互換，以此類推。
    """
    def swap(self, _input):
        _index = self.getIndex(_input)
        
        """_index & 1
        採用二進制規則來判斷奇偶，結果為 0 是偶數，結果為 1 是奇數，例如：
        
        _index = 4(十進制) = 00000100
                 1(十進制) = 00000001
        _index & 1        =  00000000 = 0
        
        _index = 5(十進制) = 00000101
                 1(十進制) = 00000001
        _index & 1        =  00000001 = 1
        """
        if (_index & 1) == 1:
            """
            奇數：和前一個元素互換。
            """
            _char = self.getChar(_index - 1)
        else:
            """
            偶數：和後一個元素互換。
            """
            _char = self.getChar(_index + 1)
            
        return _char
    
    def printStatus(self):
        _output_sequense = []
        for i in self.origin_sequence:
            _output_sequense.append(self.swap(i))
            
        print("[r-i]:{}".format(self.origin_sequence))
        print("[r-o]:{}".format(_output_sequense))


"""
旋轉盤的說明請看 PythonTutorial_0_To_1/Enigma/。
"""
class Rotor(Pipeline):
    def __init__(self, _items, _pointer):
        """
        Rotor 繼承 Pipeline，Pipeline 做得到的 Rotor 一樣可以。
        super().__init__(_items) 執行了 Pipeline 當中的 __init__()，
        並給予參數 _items。
        """
        super().__init__(_items)
        
        """
        self.pointer 相當於採用第幾組元素轉換規則。
        """
        self.pointer = _pointer
        
        """
        進位值，每加密多少次'更改一次加密組合' = pointer + 1 = 旋轉盤轉動一次。
        """
        self.carry = 1
        
        """
        紀錄加密/解密次數，用於判斷是否需要進位。
        """
        self.counter = 0
    
    """
    '輸入往反射板'方向的元素轉換。
    """
    def forwardSwap(self, _input):
        """
        加密/解密次數 +1。
        """
        self.counter += 1
        
        """
        取得輸入元素在 self.origin_sequence 當中的索引值。
        """
        _index = self.getIndex(_input)
        
        
        """
        下方兩行應一起理解，_index + self.forward[_swap_index] 表示
        原本的元素索引值變成新的索引值，例如：0 → 3；7 → 2，達到元素轉換的效果。
        
        原本元素在陣列中第幾個位置(_index)，就會採用 self.forward 中第幾個位置
        的'偏移值'，但這裡又加上 self.pointer，本次的轉換就會採用 self.forward 中
        第 (_index + self.pointer) 個位置的'偏移值'，後面的'% self.length'是在
        確保前面數值不會超過陣列範圍。        
        """
        _swap_index = (_index + self.pointer) % self.length
        _output = _index + self.forward[_swap_index]
        
        """
        _index + self.forward[_swap_index] 後的 _output 或許會超過陣列範圍，透過
        self.getChar回傳元素，確保它不會超過陣列範圍。
        """
        return self.getChar(_output)
    
    """
    '反射板往輸出'方向的元素轉換規則。
    """
    def backwardSwap(self, _input):
        """
        取得輸入元素在 self.origin_sequence 當中的索引值。
        """
        _index = self.getIndex(_input)
        
        """
        基本上和 forwardSwap 相同，但'偏移值'的來源從 self.forward 變成 self.backward。
        """
        _swap_index = (_index + self.pointer) % self.length            
        _output = _index + self.backward[_swap_index]
        
        return self.getChar(_output)
    
    """
    檢查是否需要轉動旋轉盤，即 self.pointer += 1。
    """
    def checkRotate(self):
        """
        加密/解密次數(self.counter) 被 進位值(self.carry) 整除，轉動旋轉盤一次。        
        """
        if self.counter % self.carry == 0:
            """
            轉動旋轉盤，改變元素轉換規則。
            """
            self.pointer += 1
            self.pointer = self.pointer % self.length
            
    def printStatus(self):
        _forward_output = []
        _backward_output = []
        
        for i in self.origin_sequence:
            _forward_output.append(self.forwardSwap(i))
            self.counter -= 1
            _backward_output.append(self.backwardSwap(i))
            
        print("[t-i]:{}".format(self.origin_sequence))
        print("[t-f]:{}".format(_forward_output))
        print("[t-b]:{}".format(_backward_output))


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
    def resetRotors(self, *args):
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


def wardTest():
    _items1 =  ['H', 'e', 'l', 'o', 'W', 'r', 'd', 's']
    _items2 = ['H', 'd', 's', 'e', 'l', 'o', 'W', 'r']
    _pipeline1 = Pipeline(_items1)
    _pipeline2 = Pipeline(_items2)
    
    """
    將元素順序進行排列，確保不同旋轉盤或反射板有相同的'參考順序'。
    """
    print("self.origin_sequence1:", _pipeline1.origin_sequence)
    print("self.origin_sequence2:", _pipeline2.origin_sequence)
    
    """
    順序與輸入時相同。
    """
    print("self.shuffle_sequence1:", _pipeline1.shuffle_sequence)
    print("self.shuffle_sequence2:", _pipeline2.shuffle_sequence)
    
    """
    _pipeline1 的 forward 和 backward 元素轉換
    """
    print("self.forward1:", _pipeline1.forward)
    print("self.backward1:", _pipeline1.backward)
    
    """
    _pipeline2 的 forward 和 backward 元素轉換
    """
    print("self.forward2:", _pipeline2.forward)
    print("self.backward2:", _pipeline2.backward)
    
    
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
    _rotor = Rotor(0, _items)
    _decode = ""
    for i in _encode:
        _char = _rotor.forwardSwap(i)
        _char = _reflactor.swap(_char)
        _decode += _rotor.backwardSwap(_char)
        
        _rotor.checkRotate()        
        
    print("decode:", _decode)
    
    
def rotorTest2():
    _items =  ['H', 'e', 'l', 'o', 'W', 'r', 'd', 's']
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
    _items =  ['H', 'e', 'l', 'o', 'W', 'r', 'd', 's']
    _items1 = ['H', 'o', 'W', 'r', 'd', 'e', 'l', 's']
    _items2 = ['H', 'd', 's', 'e', 'l', 'o', 'W', 'r']
    _items3 = ['r', 'd', 's', 'e', 'H', 'o', 'W', 'l']
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
    
    _enigma.resetRotors(4, 7, 3, 9)
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
