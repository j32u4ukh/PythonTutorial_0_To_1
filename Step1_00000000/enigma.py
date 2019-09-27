# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 22:33:12 2019

@author: j32u4ukh
"""
class Rotor:
    # pointer=None 表示此為反射板
    def __init__(self, _items, _pointer=None, _carry=None):
        self.items = _items
        self.length = len(_items)
        self.pointer = _pointer
        self.carry = _carry
        self.counter = 0
        
        if self.pointer is not None:
            self.shift()
        
    def shift(self):
        return self.items[self.pointer:] + self.items[:self.pointer]

    # 交換功能        
    def swap(self, _input):
        # 每被呼叫一次就加一
        self.counter += 1
        
        # 確保輸入為 index
        if (type(_input) is str) or (type(_input) is chr):
            _index = self.getIndex(_input)
        else:
            _index = _input

        # 若為奇數
        if _index & 1 == 1:
            _char = self.items[_index - 1]
        # 若為偶數
        else:
            _char = self.items[_index + 1]
        
        self.checkRotate()
        
        return _char
        
    def checkRotate(self):
        if self.pointer is not None:
            if self.counter % self.carry == 0:
                self.pointer += 1
                self.pointer %= self.length
                # 旋轉
                self.items = self.shift()
    
    # 取得字元的 index        
    def getIndex(self, _char):
        for i in range(self.length):
            if self.items[i] == _char:
                return i
            
            
class Enigma:
    def __init__(self):
        self.rotors = []
        
    def add(self, _rotor):
        self.rotors.append(_rotor)
    

def rotorTest():
    items = ['H', 'e', 'l', 'o', 'W', 'r', 'd', 's']
    word = "Hello"
    rotor = Rotor(items, 0, 1)
    
    encode = ""
    for i in word:
        encode += rotor.swap(i)
        
    print("encode:", encode)
    
    rotor = Rotor(items, 0, 1)
    decode = ""
    for i in encode:
        decode += rotor.swap(i)
        
    print("decode:", decode)


def reflactorTest():
    items = ['H', 'e', 'l', 'o', 'W', 'r', 'd', 's']
    word = "Hello"
    rotor = Rotor(items)
    
    encode = ""
    for i in word:
        encode += rotor.swap(i)
        
    print("encode:", encode)
    
    rotor = Rotor(items)
    decode = ""
    for i in encode:
        decode += rotor.swap(i)
        
    print("decode:", decode)


if __name__ == "__main__":
#    rotorTest()
    reflactorTest()
