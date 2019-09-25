# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 21:31:23 2019

@author: j32u4ukh
"""
import random

class Pipeline:
    def __init__(self):
        """初始字元順序"""
        self.origin_sequence = []
        self.shuffle_sequence = []
        self.length = 0
        self.forward = []
        self.backward = []
        self.pointer = 0
        
    def defaultSequence(self):
        for i in range(10):
            _char = '{}'.format(i)
            self.origin_sequence.append(_char)
            
        for i in range(65, 91):
            _char = chr(i)
            self.origin_sequence.append(_char)
            
        for i in range(97, 123):
            _char = chr(i)
            self.origin_sequence.append(_char)
        
    def addOriginItems(self, _items=None):
        """若 _items 不為None，將 _items 陣列中所有值依序放入 self.origin_sequence"""
        if _items is None:
            self.defaultSequence()            
        else:
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

class Reflector(Pipeline):
    def __init__(self, _items=None):
        super().__init__()
        self.addOriginItems(_items)
        
        # 設置 forward backward
        self.defaultShuffle()
        self.setSwap(self.shuffle_sequence)
        
    def swap(self, _input):
        if type(_input) is str:
            _input = self.getIndex(_input)
            
        _output = _input + self.forward[_input]
        
        print("[reflector]from:{}, to:{}".format(_input, _output))
        
        return self.getChar(_output)


class Rotor(Pipeline):
    def __init__(self, _pointer, _items=None):
        super().__init__()
        self.addOriginItems(_items)
        self.pointer = _pointer
        
        # 進位值，每加密多少次更改一次加密組合，即 pointer + 1
        self.carry = 1
        
        # 設置 self.addtion
        self.defaultShuffle()
        self.setSwap(self.shuffle_sequence)
        
    def swap(self, _input, _direction):
        if type(_input) is str:
            _input = self.getIndex(_input)
        
        _swap_index = _input + self.pointer
        if self.length <= _swap_index:
            _swap_index %= self.length
            
        _output = _swap_index + _direction[_swap_index]
        print("[rotor]from:{}, pointer:{}, swap_index:{}, to:{}".format(_input, 
              self.pointer, _swap_index, _output))
        
#        print("[rotor]out_index:{}, output:{}".format(_output,
#              self.origin_sequence[_output]))
        return self.getChar(_output)
        
    def forwardSwap(self, _input):
        if type(_input) is str:
            _input = self.getIndex(_input)
        
        _swap_index = _input + self.pointer
        if self.length <= _swap_index:
            _swap_index %= self.length
            
        _output = _swap_index + self.forward[_swap_index]
        print("[forward]from:{}, pointer:{}, swap_index:{}, to:{}".format(_input, 
              self.pointer, _swap_index, _output))
        
        return self.getChar(_output)
    
    def backwardSwap(self, _input):
        if type(_input) is str:
            _input = self.getIndex(_input)
            
        _output = _input + self.backward[_input]
        print("[backward]from:{}, to:{}".format(_input, _output))
        
#        print("[rotor]out_index:{}, output:{}".format(_output,
#              self.origin_sequence[_output]))
        return self.getChar(_output)
    
    def checkRotate(self, _pre_rotor):        
        if _pre_rotor > 0 and _pre_rotor % self.carry == 0:
            # 轉動旋轉盤，改變加密組合
            self.pointer += 1
            self.pointer = self.pointer % self.length
            
    def setCarry(self, _carry):
        self.carry = _carry


class Enigma:
    def __init__(self, _items):
        self.items = _items
        self.rotors = []
        self.reflector = Reflector(self.items)
        
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
            
            # checkRotate
            for _r in range(_rotor_num):
                self.rotors[_r].checkRotate(_index + 1)
                
            _output += _char
            print("-"*30)
        
        return _output
    
    
def reflectorTest():
    # _string = "HelloWorld"    
    # _items = list(set(list(_string)))
    _items = ['r', 'd', 'e', 'H', 'W', 'o', 'l']
    _code = "Hello"    
    _reflector = Reflector(_items)
    print("origin:    ", _reflector.origin_sequence)
    print("reflector: ", _reflector.shuffle_sequence)
    print("forward:   ", _reflector.forward)
    print("backward:  ", _reflector.backward)
    for i in _code:
        print(i, _reflector.swap(i))
        

def rotorTest():
    # _string = "HelloWorld"    
    # _items = list(set(list(_string)))
    _items = ['r', 'd', 'e', 'H', 'W', 'o', 'l']
    _code = "Hello"
    
    _rotor = Rotor(0, _items)
    print("origin:  ", _rotor.origin_sequence)
    print("shuffle: ", _rotor.shuffle_sequence)
    print("forward: ", _rotor.forward)
    print("backward:", _rotor.backward)
    print("="*30)
    
    _encode = ""
    for i in _code:
        _encode += _rotor.forwardSwap(i)
        
    print("encode:{}".format(_encode))
    
    _decode = ""
    for i in _encode:
        _decode += _rotor.backwardSwap(i)
        
    print("decode:{}".format(_decode))
    
    
def enigmaTest():
    _items = ['r', 'd', 'e', 'H', 'W', 'o', 'l']
    _code = "ell"
    
    _enigma = Enigma(_items)
    _rotor = Rotor(0, _items)
    _enigma.add(_rotor)
    _enigma.compile_()
    print("origin:   ", _rotor.origin_sequence)
    print("forward:  ", _rotor.forward)
    print("reflector:", _enigma.reflector.forward)
    print("backward: ", _rotor.backward)
    
    encode = _enigma.swap(_code)
    print(encode)
    

def enigmaTest2():
    _items = ['r', 'd', 'e', 'H', 'W', 'o', 'l']
    _code = "ell"
    
    _enigma = Enigma(_items)
    _rotor = Rotor(0, _items)
    _enigma.add(_rotor)
    _enigma.compile_()
    print("origin:   ", _rotor.origin_sequence)
    print("forward:  ", _rotor.forward)
    print("reflector:", _enigma.reflector.forward)
    print("backward: ", _rotor.backward)
    
    _encode = _enigma.swap(_code)
    print("encode:", _encode)
        
    _enigma.rotors[0].pointer = 0
    _decode = _enigma.swap(_encode)
    print("decode:", _decode)
    

if __name__ == "__main__":
#    reflectorTest()
#    rotorTest()
#    enigmaTest()
    enigmaTest2()
