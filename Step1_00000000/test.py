# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 21:57:00 2019

@author: j32u4ukh
"""
import numpy as np

def numberASCII():
    # 48 ~ 57
    for i in range(10):
        string = '{}'.format(i)
        print(string, ord(string))
        

def alphabetASCII():
    print('A', ord('A'))  # 65
    print('Z', ord('Z'))  # 90
    print('a', ord('a'))  # 97
    print('z', ord('z'))  # 122    
    print()
    
    for i in range(65, 91):
        char = chr(i)
        print(i, char)    
    print()
    
    for i in range(97, 123):
        char = chr(i)
        print(i, char)

      
def sixQuotationMarksTest():
    print("""a {} 
    b {} 
    c {}""".format(1,
    2, 
    3))
    

def chineseTest():
    # print(ord('ˊ'))  # 714
    # print(ord('ˇ'))  # 711
    # print(ord('ˋ'))  # 715
    # print(ord('˙'))  # 729
    # print(ord('ㄅ'))  # 12549
    # print(ord('ㄦ'))  # 12582
    # print(ord('ㄧ'))  # 12583
    # print(ord('ㄨ'))  # 12584
    # print(ord('ㄩ'))  # 12585
    
    for i in range(12549, 12582 + 1):
        print(i, chr(i))
        
    
def japaneseTest():
    japanese = ['あ', 'い', 'う', 'え', 'お',
                'か', 'き', 'く', 'け', 'こ',
                'さ', 'し', 'す', 'せ', 'そ',
                'ら', 'り', 'る', 'れ', 'ろ',]
    
    for j in japanese:
        print(j, ord(j))
        
    print(chr(12354 + 3))
    
    
def shuffleTest(_array):
    _length = len(_array)
    _shuffle_array = [0 for i in range(_length)]
    _is_odd = False
    
    if _length & 1 == 1:
        _is_odd = True
        _length -= 1
        
    for i in range(0, _length, 2):
        try:
            _shuffle_array[i] = _array[i + 1]
            _shuffle_array[i + 1] = _array[i]
        except IndexError:
            print("length:{}, require index:{}".format(len(_array), i + 1))
            
    if _is_odd:
        _shuffle_array[_length] = _array[_length]
            
    return _shuffle_array
    

if __name__ == "__main__":
    # numberASCII()        
    # alphabetASCII()
    # sixQuotationMarksTest()
    # chineseTest()
    # japaneseTest()
    array = [1, 2, 3, 4, 5, 6]
    shuffle_array = shuffleTest(array)
    print(array)
    print(shuffle_array)
        
        
