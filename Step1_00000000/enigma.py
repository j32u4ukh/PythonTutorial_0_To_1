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
        assert (type(_item) is chr) or  (type(_item) is str), "_item 的類型必須是 chr 或 str"
        self.origin_sequence.append(_item)
        
    def getIndexAddition(self, _temp_array):
        _addition = []
        _length = len(_temp_array)
        for i in range(_length):
            _curr = _temp_array[i]
            _curr_index = self.getIndex(_curr)
            
            _next = i + 1 
            
            if _next == _length:
                _next = 0
                
            _next_char = _temp_array[_next]
            _next_index = self.getIndex(_next_char)
            
            _index_gap = _next_index - _curr_index
            
            if _index_gap < 0:
                _index_gap += _length
                
            _addition.append(_index_gap)
            
        return _addition        
        
    def getIndex(self, _char):
        for _index, _item in enumerate(self.origin_sequence):
            if _item == _char:
                return _index
        
        """查詢的字元不在 self.origin_sequence 當中"""
        return -1
    
    def getChar(self, _index):
        _char = ''
        
        try:
            _char = self.origin_sequence[_index]
        except IndexError:
            print("""length of origin_sequence is {}, your index is {}""".format(len(self.origin_sequence), _index))

        return _char

class Reflector(Pipeline):
    def __init__(self, _items=None):
        super().__init__()
        self.addOriginItems(_items)
        self.addtion = None
        self.setReflector()
        self.pointer = 0
        
    def setReflector(self):
        _temp_sequence = self.origin_sequence.copy()
        random.shuffle(_temp_sequence)
        self.addtion = self.getIndexAddition(_temp_sequence)
        
    def transform(self, _input):
        if type(_input) is str:
            _input = self.getIndex(_input)
        
        _output = _input + self.addtion[self.pointer]
        _output = _output % self.length
        
        return self.origin_sequence[_output]

class Rotor(Pipeline):
    def __init__(self, _carry):
        super().__init__()
        self.carry = _carry


class Enigma:
    def __init__(self, _items):
        self.items = _items
        
    def test(self):
        print("Hello Enigma!")


if __name__ == "__main__":   
    string = "Hello World"
    items = list(set(list(string)))
    
    reflector = Reflector(items)
    print("origin")
    print(reflector.origin_sequence)
    print("reflector")
    print(reflector.addtion)
    for i in string:
        print(i, reflector.transform(i))