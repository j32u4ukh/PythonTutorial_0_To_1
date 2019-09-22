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
        
    def setSwap(self, _temp_array):
        _length = len(_temp_array)
        for i in range(_length):
            _curr_char = _temp_array[i]
            _curr_index = self.getIndex(_curr_char)
            
            _next = i + 1 
            
            if _next == _length:
                _next = 0
                
            _next_char = _temp_array[_next]
            _next_index = self.getIndex(_next_char)
            
            # set forward 後減前
            _index_gap = _next_index - _curr_index
            
            if _index_gap < 0:
                _index_gap += _length
                
            self.forward.append(_index_gap)
            
            # set backward 前減後
            _index_gap = _curr_index - _next_index
            
            if _index_gap < 0:
                _index_gap += _length
                
            self.backward.append(_index_gap)
        
    def getIndex(self, _char):
        for _index, _item in enumerate(self.origin_sequence):
            if _item == _char:
                return _index
        
        """查詢的字元不在 self.origin_sequence 當中"""
        return -1

class Reflector(Pipeline):
    def __init__(self, _items=None):
        super().__init__()
        self.addOriginItems(_items)
        
        # 設置 forward backward
        self.temp_sequence = self.origin_sequence.copy()
        random.shuffle(self.temp_sequence)
        self.setSwap(self.temp_sequence)
        
    def swap(self, _input):
        if type(_input) is str:
            _input = self.getIndex(_input)
            
        _output = _input + self.forward[_input]
        _output = _output % self.length
        
#        print("[reflector]index:{}, addtion_index:{}, output:{}".format(_input, 
#              _output, self.origin_sequence[_output]))
        
        return self.origin_sequence[_output]


class Rotor(Pipeline):
    def __init__(self, _carry, _items=None):
        super().__init__()
        self.addOriginItems(_items)
        # 進位值，每加密多少次更改一次加密組合，即 pointer + 1
        self.carry = _carry
        
        # 設置 self.addtion
        self.temp_sequence = self.origin_sequence.copy()
        random.shuffle(self.temp_sequence)
        self.setSwap(self.temp_sequence)
        
    def swap(self, _input, _direction):
        if type(_input) is str:
            _input = self.getIndex(_input)
        
        _swap_index = _input + self.pointer
        _swap_index = _swap_index % self.length
#        print("[rotor]index:{}, pointer:{}, swap_index:{}".format(_input, 
#              self.pointer, _swap_index))
            
        _output = _input + _direction[_swap_index]
        _output = _output % self.length
        
#        print("[rotor]out_index:{}, output:{}".format(_output,
#              self.origin_sequence[_output]))
        return self.origin_sequence[_output]
        
    def forwardSwap(self, _input):
        return self.swap(_input, self.forward)
    
    def backwardSwap(self, _input):
        return self.swap(_input, self.backward)
    
    def checkRotate(self, _pre_rotor):        
        if _pre_rotor > 0 and _pre_rotor % self.carry == 0:
            # 轉動旋轉盤，改變加密組合
            self.pointer += 1
            self.pointer = self.pointer % self.length


class Enigma:
    def __init__(self, _items):
        self.items = _items
        self.rotors = []
        self.reflector = Reflector(items)
        
    def add(self, _rotor):
        assert type(_rotor) is Rotor, "請添加旋轉盤"
        self.rotors.append(_rotor)
        
    def compile_(self):
        _rotor_num = len(self.rotors)
        for _r in range(_rotor_num):
            if _r == 0:
                continue
            else:
                self.rotors[_r].carry *= self.rotors[_r - 1].carry            
        
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
#            print("-"*30)
        
        return _output

if __name__ == "__main__":   
    string = "Hello World"
    code = "Hello"
    items = list(set(list(string)))
    
#    reflector = Reflector(items)
#    print("origin:", reflector.origin_sequence)
#    print("reflector:", reflector.temp_sequence)
#    print("forward:", reflector.forward)
#    print("backward:", reflector.backward)
#    for i in code:
#        print(i, reflector.swap(i))
        
    enigma = Enigma(items)
    rotor = Rotor(1, items)
    enigma.add(rotor)
    enigma.compile_()
    
    print("origin:   ", rotor.origin_sequence)
    print("forward:  ", rotor.forward)
    print("backward: ", rotor.backward)
    reflector = enigma.reflector
    print("reflector:", reflector.forward)
#    print("="*30)
#    for i, s in enumerate(string):
#        print(i, s, rotor.transform(s))
#        rotor.checkRotate(i + 1)
    
    encode = enigma.swap(code)
    print(code)
    print(encode)
    
    