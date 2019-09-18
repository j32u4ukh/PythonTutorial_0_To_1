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
        self.index_to_char = {}
        self.char_to_index = {}
        
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
            
    def addOriginItem(self, _item):
        """將 _item 的值放入 self.origin_sequence"""
        assert type(_item) is chr, "_item 的類型必須是 chr"
        self.origin_sequence.append(_item)
        
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
        self.reflector_sequence = self.origin_sequence.copy()
        
    def setReflector(self):
        _temp_sequence = self.origin_sequence.copy()
        random.shuffle(_temp_sequence)
        print(_temp_sequence)
        

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
    reflector = Reflector()
    print("origin")
    print(reflector.origin_sequence)
    print("reflector")
    reflector.setReflector()