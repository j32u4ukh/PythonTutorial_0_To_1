# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 21:57:00 2019

@author: j32u4ukh
"""

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

numberASCII()        
# alphabetASCII()
#sixQuotationMarksTest()
