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

if __name__ == "__main__":
    # numberASCII()        
    # alphabetASCII()
    # sixQuotationMarksTest()
    # chineseTest()
    # japaneseTest()
    def getPointer(_array, _char):
        for i, c in enumerate(_array):
            if c == _char:
                return i
            
    origin = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    shuffle = ['1', '2', '8', '9', '4', '0', '5', '3', '6', '7']
    pointer = []
    length = len(shuffle)
    for index in range(length):
        curr = shuffle[index]
        curr_pointer = getPointer(origin, curr)
        
        next_index = index + 1 
        
        if next_index == length:
            next_index = 0
            
        next_char = shuffle[next_index]
        next_pointer = getPointer(origin, next_char)
        
        pointer_plus = next_pointer - curr_pointer
        
        if pointer_plus < 0:
            pointer_plus += length
            
        pointer.append(pointer_plus)
        
    print(pointer)
        
        
