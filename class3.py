# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:48:17 2019

@author: j32u4ukh

教學大綱：
1. Rotor
2. if __name__ == "__main__":
     
這次一樣要以 Enigma 中使用到的另一個物件為例，其內容牽涉到程式的運用與 Enigma 本身
機制的理解，會較困難，可以先回頭複習當中使用到的程式，再將對 Enigma 的說明與程式碼
兩者搭配一起理解。

這次要實做的是"旋轉盤"，與反射板一樣是對數入的元素進行轉換，但不同的是，反射板具有
方向性且並非兩兩互換。

方向性："從輸入到反射板" 與 "從反射板到輸出"。
非兩兩互換："從輸入到反射板"時， a 會轉換成 b ，但 b 會轉換成 f 。
           "從反射板到輸出"時， b 會轉換成 a ，而 f 會轉換成 b 。
兩兩互換：無論方向，a 會轉換成 b ，而 b 會轉換成 a 。

Pipeline 作為'反射板'(Reflector)和'旋轉盤'(Rotor)的父類別，包含共同使用的函式或參數
，可避免重複內容的撰寫。
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
"""


class Rotor(Pipeline):
    def __init__(self, _items, _pointer=0):
        """
        Rotor 繼承 Pipeline，Pipeline 做得到的 Rotor 一樣可以。
        super().__init__(_items) 執行了 Pipeline 當中的 __init__()，
        並給予參數 _items。
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
        """
        self.carry = 1
        
        """
        紀錄加密/解密次數，用於判斷是否需要進位。
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
這個腳本中部只有單純定義函式或物件，還使用了它們，那再使用 import 的同時，這些程式碼
也都會被執行。

為避免上述情形，就要透過 if __name__ == "__main__": 這行程式碼，只有在符合 
__name__ == "__main__" 的條件下，下方的程式碼才會被執行。

而 __name__ == "__main__" 表示的就是這段程式碼是被當前這個腳本所執行，而不是透過 
import 而被執行的。
"""
if __name__ == "__main__":
     rotorTest()
     


