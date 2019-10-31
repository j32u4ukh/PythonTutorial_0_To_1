# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:48:00 2019

@author: j32u4ukh

教學大綱：
1. inherit
2. super()
3. Reflector

物件導向語言還有一個特色，那就是物件的繼承。子物件會繼承父物件的屬性與方法(功能)，例如：
父物件是電話，子物件是市內電話、普通手機、智慧型手機，三樣子物件都繼承了電話具備電話
號碼的屬性，以及可以打電話這項功能。

之前在教物件的時候有說物件的形式是"class 物件名稱:"，但這其實是簡化了一些東西，完整的
版本應該是"class 物件名稱(object):"，又因為所有物件都繼承自 object 這個物件，所以也
可以簡化成"class 物件名稱():"，這段使用的三種形式都是可以的。

以智慧型手機為例，就會是"class 智慧型手機(電話):"，以下示範繼承的效果，可以與之前在教
物件時的程式碼做比較。
"""
from random import shuffle

class Phone:
     def __init__(self, _phone_number):
          self.phone_number = _phone_number
          
     def call(self, _number_to_call):
          print("{} call to {}".format(self.phone_number, _number_to_call))
          
     def getPhoneNumber(self):
          return self.phone_number
          

class SmartPhone(Phone):
     def __init__(self, _width, _height, _phone_number):
          self.width = _width
          self.height = _height
          self.phone_number = _phone_number
          

"""
可以看到， SmartPhone 當中並沒有對 call 和 getPhoneNumber 作定義，但依然可以使用，
這就是繼承了 Phone 之後的效果，可以有效減少重複的程式碼。
"""
smart_phone1 = SmartPhone(8, 17, "0809449")
smart_phone2 = SmartPhone(9.8, 19, "110")

print("smart_phone1.width:", smart_phone1.width)
print("smart_phone1.height:", smart_phone1.height)
print("smart_phone1.phone_number:", smart_phone1.phone_number)

print("smart_phone2.width:", smart_phone2.width)
print("smart_phone2.height:", smart_phone2.height)
print("smart_phone2.phone_number:", smart_phone2.phone_number)

smart_phone1.call("110")
smart_phone1.call(smart_phone2.getPhoneNumber())
"""
仔細看兩個物件的 __init__ 會發現， self.phone_number 的部分重複操作了，而重複的部分
完全和 Phone 的 __init__ 相同。我們可以利用 super() 去執行父物件當中的函式，當子物件
有和父物件相同名稱的函式時，透過 super() 可以明確地使用父物件中的函式。

下面以普通手機為例，因為上面已經定義過智慧型手機了。
"""
class MobilePhone(Phone):
     def __init__(self, _width, _height, _phone_number):
          self.width = _width
          self.height = _height
          """
          透過 super() 去使用父物件 Phone 當中的 __init__ ，這行相當於做了 
          self.phone_number = _phone_number ，如果 Phone 的 __init__ 當中定義
          了更多內容，那省下來不用重複寫的內容也就會越多。
          """
          super().__init__(_phone_number)
     
     """
     MobilePhone 的 call 這項函式當中，透過 super() 去使用父物件 Phone 當中的
     call ，並在這之後在執行自己本身的程式碼，這對撰寫程式提供了許多彈性。
     """
     def call(self, _number_to_call):          
          super().call(_number_to_call)
          print("通話結束")
          

mobile_phone1 = MobilePhone(7.4, 13, "9527")
mobile_phone2 = MobilePhone(3.14, 14, "110")

print("mobile_phone1.width:", mobile_phone1.width)
print("mobile_phone1.height:", mobile_phone1.height)
print("mobile_phone1.phone_number:", mobile_phone1.phone_number)

print("mobile_phone2.width:", mobile_phone2.width)
print("mobile_phone2.height:", mobile_phone2.height)
print("mobile_phone2.phone_number:", mobile_phone2.phone_number)

mobile_phone1.call("110")
mobile_phone1.call(mobile_phone2.getPhoneNumber())
"""
下面我將以 Enigma 中使用到的物件為例，讓各位看看實際使用到繼承的情況，因此需要對物件
的內涵稍作說明，細節請參考 PythonTutorial_0_To_1/Enigma/。

以下將實作 Reflector 繼承 Pipeline ， Reflector 是 Enigma 加密過程中的一環，會將 
Enigma 所包含的元素兩兩交換。
"""
class Pipeline:
    def __init__(self, _items): 
        self.origin_sequence = _items.copy()
        self.origin_sequence.sort()
        
        self.shuffle_sequence = _items.copy()
        shuffle(self.shuffle_sequence)        
        
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
   

class Reflector(Pipeline):
    def __init__(self, _items):
        """
        Reflector 繼承 Pipeline，Pipeline 做得到的 Reflector 一樣可以。
        super().__init__(_items) 執行了 Pipeline 當中的 __init__()，
        並給予參數 _items。
        """
        super().__init__(_items)
    
    """
    Reflector 的設計為兩兩互換，這裡讓第 0 和第 1 互換，第 2 和第 3 互換，以此類推。
    """
    def swap(self, _input):
        _index = self.getIndex(_input)
        
        """_index & 1
        採用二進制規則來判斷奇偶，結果為 0 是偶數，結果為 1 是奇數，例如：
        
        _index = 4(十進制) = 00000100
                 1(十進制) = 00000001
        _index & 1        =  00000000 = 0
        
        _index = 5(十進制) = 00000101
                 1(十進制) = 00000001
        _index & 1        =  00000001 = 1
        """
        if (_index & 1) == 1:
            """
            奇數：和前一個元素互換。
            """
            _char = self.getChar(_index - 1)
        else:
            """
            偶數：和後一個元素互換。
            """
            _char = self.getChar(_index + 1)
            
        return _char
   

def reflectorTest():
     """
     這是個測試 Reflector 的函式， items 提供了所有的元素，注意元素的個數需要是偶數，
     因為 Reflector 是兩兩互換的。
     """
     items = ['H', 'e', 'l', 'o', 'W', 'r', 'd', 's']
     reflactor = Reflector(items)
     word = "Hello"
     
     """
     透過 reflactor 的 swap 當中的每個元素做加密，並加入 encode 當中。
     """
     encode = ""
     for i in word:
          encode += reflactor.swap(i)
     
     print("encode:", encode)
     
     """
     由於  Reflector 是兩兩互換的，因此將 encode 再次透過 swap 轉換，便會變回原本
     輸入的內容了。
     """
     decode = ""
     for i in encode:
          decode += reflactor.swap(i)
     
     print("decode:", decode)
    
    
reflectorTest()
