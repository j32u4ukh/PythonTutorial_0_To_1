# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 08:12:23 2019

@author: user
"""
class Pipeline:
    def __init__(self):
        """初始字元順序"""
        self.origin_sequence = []
        self.shuffle_sequence = []
        self.length = 0
        self.forward = []
        self.backward = []
        self.pointer = 0
        
    def addOriginItems(self, _items):
        for _item in _items:
            self.addOriginItem(_item)            
        
        # 保存長度資訊
        self.length = len(self.origin_sequence)
            
    def addOriginItem(self, _item):
        """將 _item 的值放入 self.origin_sequence"""
        assert (type(_item) is chr) or (type(_item) is str), "_item 的類型必須是 chr 或 str"
        self.origin_sequence.append(_item)
        
    def defaultShuffle(self):
        _length = self.length
        self.shuffle_sequence = [0 for i in range(_length)]        
        _is_odd = False
        
        # 是奇數個
        if _length & 1 == 1:
            _is_odd = True
            _length -= 1
            
        for i in range(0, _length, 2):
            try:
                self.shuffle_sequence[i] = self.origin_sequence[i + 1]
                self.shuffle_sequence[i + 1] = self.origin_sequence[i]
            except IndexError:
                print("length:{}, require index:{}".format(self.length, i + 1))
                
        if _is_odd:
            self.shuffle_sequence[_length] = self.origin_sequence[_length]
        
    def setSwap(self, _temp_array):
        """ 例子；例；For example
        origin:        ['r', 'd', 'e', 'H', 'W', 'o', 'l']
                       [  0,   1,   2,   3,   4,   5,   6]
        temp_sequence: ['H', 'e', 'l', 'd', 'r', 'W', 'o']
                       [  3,   2,   6,   1,   0,   4,   5]
        length = 7
        forward:       [ +4,  -1,  +4,  -1,  +1,  -2,  -5]        
        backward:      [ +1,  +5,  +1,  +2,  -4,  -1,  -4]
        """
        _temp_seq_index = []
        for t in _temp_array:
            _temp_seq_index.append(self.getIndex(t))
        # print("temp_seq_index:", _temp_seq_index)
        self.forward = [0 for i in range(self.length)]
        self.backward = [0 for i in range(self.length)]
        
        for i in range(self.length):
            """ 例子；例；For example i = 0, _curr_char = 'H' """
            _curr_char = _temp_array[i]
            """ 例子；例；For example _curr_index = 3 """
            _curr_index = self.getIndex(_curr_char)

            """ 例子；例；For example _next = 1 """
            _next = i + 1
            
            if _next == self.length:
                _next = 0
            
            """ 例子；例；For example _next_char = 'e' """
            _next_char = _temp_array[_next]
            """ 例子；例；For example _next_index = 2 """
            _next_index = self.getIndex(_next_char)
            
            # set forward 後減前
            """ 例子；例；For example _next_gap = 2 - 3 = -1 """
            _next_gap = _next_index - _curr_index
                
            """ 例子；例；For example self.forward[3] = -1 """
            self.forward[_curr_index] = _next_gap
        
        for i in range(self.length):
            _back_index = i + self.forward[i]                
            self.backward[_back_index] = -self.forward[i] 
        
    def getIndex(self, _char):
        for _index, _item in enumerate(self.origin_sequence):
            if _item == _char:
                return _index
        
        """查詢的字元不在 self.origin_sequence 當中"""
        return -1
    
    def getChar(self, _index):
        if _index < 0:
            _index += self.length
        
        if self.length <= _index:
            _index %= self.length
        
        return self.origin_sequence[_index]


# 反射板應為兩兩互換
class Reflector(Pipeline):
    def __init__(self, _items):
        super().__init__()
        self.addOriginItems(_items)        
        self.defaultShuffle()
        
    def swap(self, _input):
        _index = self.getIndex(_input)
            
        if (_index & 1) == 1:
            _char = self.getChar(_index - 1)
        else:
            _char = self.getChar(_index + 1)
            
        return _char
    
    def printStatus(self):
        _output_sequense = []
        for i in self.origin_sequence:
            _output_sequense.append(self.swap(i))
            
        print("[r-i]:{}".format(self.origin_sequence))
        print("[r-o]:{}".format(_output_sequense))


class Rotor(Pipeline):
    def __init__(self, _pointer, _items):
        super().__init__()
        self.addOriginItems(_items)
        self.pointer = _pointer
        
        # 進位值，每加密多少次更改一次加密組合，便執行 pointer + 1
        self.carry = 1
        # 紀錄函式被呼叫次數，用於判斷是否需要進位
        self.counter = 0
        
        # 設置 self.addtion
        self.defaultShuffle()
        self.setSwap(self.shuffle_sequence)
        
    def forwardSwap(self, _input):
        self.counter += 1
        
        _index = self.getIndex(_input)
        
        _swap_index = (_index + self.pointer) % self.length
            
        # 使用第 _swap_index 組加密模式
        _output = _index + self.forward[_swap_index]  
#        print("[r-f] from:{}, to:{}".format(_input, self.getChar(_output)))
        
        return self.getChar(_output)
    
    def backwardSwap(self, _input):
        _index = self.getIndex(_input)
        
        # 使用第 _swap_index 組加密模式
        _swap_index = (_index + self.pointer) % self.length
            
        _output = _index + self.backward[_swap_index]
        
#        print("[r-b] from:{}, to:{}".format(_input, self.getChar(_output)))
        
        return self.getChar(_output)
    
    def checkRotate(self):        
        if self.counter % self.carry == 0:
            # 轉動旋轉盤，改變加密組合
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

        
class Enigma:        
    def __init__(self, _items):
        self.items = _items
        self.rotors = []
        self.reflector = Reflector(_items)
        
    def add(self, _rotor):
        assert type(_rotor) is Rotor, "請添加旋轉盤"
        self.rotors.append(_rotor)
        
    def compile_(self):
        _rotor_num = len(self.rotors)
        for _r in range(_rotor_num):
            if _r == 0:
                continue
            else:
                self.rotors[_r].carry = self.rotors[_r - 1].carry * self.rotors[_r].length
                
    def swap(self, _input):
        _output = ""
        _rotor_num = len(self.rotors)
        for _index, _char in enumerate(_input):
            # Forward propagation
            for _r in range(_rotor_num):
                _char = self.rotors[_r].forwardSwap(_char)
                
            # Reflector
            _char = self.reflector.swap(_char)
            
            # Back propagation
            for _r in range(_rotor_num - 1, -1, -1):
                _char = self.rotors[_r].backwardSwap(_char)
                
            # for _r in range(_rotor_num):
            #     self.rotors[_r].printStatus()
                
            # self.reflector.printStatus()
            
            # checkRotate
            for _r in range(_rotor_num):
                self.rotors[_r].checkRotate()
                
            _output += _char
            # print("-"*30)
        
        return _output


def reflactorTest():
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
    
    _rotor = Rotor(0, _items)
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
    _rotor1 = Rotor(0, _items1)
    _rotor2 = Rotor(3, _items2)
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
    _rotor1 = Rotor(0, _items1)
    _rotor2 = Rotor(3, _items2)
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
    _rotor = Rotor(0, _items)
    _enigma.add(_rotor)
    _enigma.compile_()
    
    _encode = ""
    for i in _word:
        _encode += _enigma.swap(i)
        
    print("encode:", _encode)
    
    _enigma = Enigma(_items)
    _rotor = Rotor(0, _items)
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
    _word = "HelloWorld"
    
    _enigma = Enigma(_items)
    _rotor1 = Rotor(4, _items1)
    _rotor2 = Rotor(7, _items2)
    _rotor3 = Rotor(3, _items3)
    _enigma.add(_rotor1)
    _enigma.add(_rotor2)
    _enigma.add(_rotor3)
    _enigma.compile_()
    
    _encode = ""
    for i in _word:
        _encode += _enigma.swap(i)
        
    print("encode:", _encode)
    
    del _enigma
    
    _enigma = Enigma(_items)
    _rotor1 = Rotor(4, _items1)
    _rotor2 = Rotor(7, _items2)
    _rotor3 = Rotor(3, _items3)
    _enigma.add(_rotor1)
    _enigma.add(_rotor2)
    _enigma.add(_rotor3)
    _enigma.compile_()
    
    _decode = ""
    for i in _encode:
        _decode += _enigma.swap(i) 
        
    print("decode:", _decode)

    
if __name__ == "__main__":
#    reflactorTest()
#    rotorTest()
#    rotorTest2()
#    enigmaTest()
    enigmaTest2()
