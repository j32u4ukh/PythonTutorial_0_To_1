教學大綱；シラバス；syllabus：
1. inherit
2. super()
3. Reflector

---

物件導向語言還有一個特色，那就是物件的繼承。

オブジェクト指向言語はもう一つ特徴、それはオブジェクトの<ruby>継承<rt>けいしょう</rt></ruby>。

Another feature of object-oriented language is the inheritance of objects.

---

子物件會繼承父物件的屬性與方法(功能)。

<ruby>子<rt>こ</rt></ruby>オブジェクトは<ruby>親<rt>おや</rt></ruby>オブジェクトの属性と機能を継承する。

Child objects will inherit the properties and methods (functions) of the parent object.

---

例如：父物件是電話，子物件是市內電話、普通手機、智慧型手機，三樣子物件都繼承了電話具備電話號碼的屬性，以及可以打電話這項功能。

例えば、親は電話、子供たちは<ruby>市内<rt>しない</rt></ruby>電話と普通の携帯電話とスマホ、三つ子オブジェクトも電話番号の属性と電話できるの機能を継承しました。

For example, the parent object is a phone, and the child objects are telephones, mobile phones, and smart phones. All three objects inherit the attributes of telephone numbers and the ability to make calls.

---

之前在教物件的時候有說物件的形式是"class 物件名稱:"。

オブジェクトを教えた時オブジェクトの形が　”class オブジェクトの名前:”　を言った。

When teaching objects before, it was said that the form of the object was "class object name:".

---

這其實是簡化了一些東西，完整的版本應該是"class 物件名稱(object):"。

実は一部分の内容を<ruby>省略<rt>しょうりゃく</rt></ruby>した、完全なバージョンは　”class オブジェクトの名前(object):”　。

This actually simplifies some things, the complete version should be "class object name (object):".

---

又因為所有物件都繼承自 object 這個物件，所以也可以簡化成"class 物件名稱():"，這段使用的三種形式都是可以的。

その上、全てのオブジェクトも object を継承して、だから　”class オブジェクトの名前():”　を書いても大丈夫。この三つ形も大丈夫だ。

And because all objects inherit from the "object" object, it can also be simplified to "class object name():". The three forms used in this paragraph are all possible.

---

以智慧型手機為例，就會是"class 智慧型手機(電話):"。

スマホに例をとして、 "class スマホ(電話):" のようなを書かれる。

Take a smart phone as an example, it will be "class SmartPhone(Phone):".

---

以下示範繼承的效果，可以與之前在教物件時的程式碼做比較。

下は継承の効果をデモンストレーションし、この前オブジェクトに教えた時のコードを比較してみよう。

The following demonstrates the effect of inheritance, you can compare this with the previous code when teaching objects.

```python
class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def call(self, _number_to_call):
        print("{} call to {}".format(self.phone_number, _number_to_call))

    def getPhoneNumber(self):
        return self.phone_number


class SmartPhone(Phone):
    def __init__(self, width, height, phone_number):
        # super().__init__(phone_number)
        self.width = width
        self.height = height
        # Phone の __init__ と同じ内容
        self.phone_number = phone_number
```

可以看到，SmartPhone 當中並沒有對 call 和 getPhoneNumber 作定義，但依然可以使用。

上のコードから分かる、 SmartPhone は call と getPhoneNumber に<ruby>定義<rt>ていぎ</rt></ruby>しないが使われできる。

As you can see, call and getPhoneNumber are not defined in SmartPhone, but they can still be used.

---

這就是繼承了 Phone 之後的效果，可以有效減少重複的程式碼。

これは継承したの効果、<ruby>重複<rt>じゅうふく</rt></ruby>なコードを有効な減らして。

This is the effect after inheriting Phone, which can effectively reduce duplicate code.

```python
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
```

仔細看兩個物件的 __init__ 會發現，self.phone_number 的部分重複操作了，而重複的部分完全和 Phone 的 __init__ 相同。

二つオブジェクトの __init__ を見れば self.phone_number の内容重複したことが見つける、重複な内容とPhone の __init__ の内容完全同じことだ。

If you look closely at the __init__ of the two objects, you will find that the part of self.phone_number is repeated, and the repeated part is exactly the same as the __init__ of Phone.

---

我們可以利用 super() 去執行父物件當中的函式。

私たちは super() で親オブジェクトの関数に実行して。

We can use super() to execute the functions in the parent object.

---

當子物件有和父物件相同名稱的函式時，透過 super() 可以明確地使用父物件中的函式。

子オブジェクトと親オブジェクトを同じ名前の関数がありますなら、 super() を利用して、プログラムにはっきり伝えて親オブジェクトの関数を利用する。

When the child object has a function with the same name as the parent object, the function in the parent object can be used explicitly through super().

---

下面以普通手機為例，因為上面已經定義過智慧型手機了。

上の部分はスマホを定義しましたので、下は普通の携帯電話を例として。

Let's take an ordinary mobile phone as an example, because the smart phone has already been defined above.

```python
class MobilePhone(Phone):
```

### def __init__

透過 super() 去使用父物件 Phone 當中的 __init__ ，這行相當於做了 self.phone_number = phone_number。

super() で親オブジェクト Phone の __init__ を利用して、 self.phone_number = phone_number を実行したと同じ効果。

Use the __init__ in the parent object Phone by super function. This line is equivalent to doing self.phone_number = phone_number.

---

如果 Phone 的 __init__ 當中定義了更多內容，那省下來不用重複寫的內容也就會越多。

もし Phone の __init__ にもっと内容を定義したなら、もっと重複な内容を省略してできる。

If more content is defined in the __init__ of the Phone, the more content will be saved without rewriting.

```python
    def __init__(self, width, height, phone_number):
        super().__init__(phone_number)
        self.width = width
        self.height = height
```

### def call

MobilePhone 的 call 這項函式當中，透過 super() 去使用父物件 Phone 當中的 call ，並在這之後在執行自己本身的程式碼，這對撰寫程式提供了許多彈性。

MobilePhone の関数 call の中に super() で親オブジェクト Phone の call を利用して、自分のコードを実行する。このような書き方はコードを書くことがもっと自由になった。

MobilePhone's call function uses super() to use the call in the parent object Phone, and then executes its own code, which provides a lot of flexibility for programming.

```python
    def call(self, _number_to_call):
        super().call(_number_to_call)
        print("通話結束")

```

```python
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
```

下面我將以 Enigma 中使用到的物件為例，讓各位看看實際使用到繼承的情況，因此需要對物件的內涵稍作說明，細節請參考 PythonTutorial_0_To_1/Enigma/。

これから Enigma の中に使ったオブジェクトを例として、皆に実際に継承を使っているの状況を見せて、だから、オブジェクトの内容をを説明することが必要だと思います。

---

以下將實作"反射板"(Reflector)繼承 Pipeline，Reflector 是 Enigma 加密過程中的一環，會將 Enigma 所包含的元素兩兩交換。

<ruby>反射板<rt>はんしゃばん</rt></ruby>が Pipeline を継承することを<ruby>実装<rt>じっそう</rt></ruby>して、Reflector は Enigma 暗号化するの一部分、Enigma 中の要素にペアワイズ<ruby>交換<rt>こうかん</rt></ruby>。

```python
class Pipeline:
    def __init__(self, _items):
        self.origin_sequence = _items.copy()
        self.origin_sequence.sort()

        self.shuffle_sequence = _items.copy()
        self.length = len(_items)

    def getIndex(self, char):
        try:
            return self.origin_sequence.index(char)
        except ValueError:
            return -1

    def getChar(self, index):
        if index < 0:
            index += self.length

        if self.length <= index:
            index %= self.length

        return self.origin_sequence[index]
```

反射板的說明請看 PythonTutorial_0_To_1/Enigma/。

反射板の説明は PythonTutorial_0_To_1/Enigma/ を見てください。

```python
class Reflector(Pipeline):
```

### def __init__

Reflector 繼承 Pipeline，Pipeline 做得到的 Reflector 一樣可以。

Reflector は Pipeline を継承(けいしょう)して、Pipeline ができるなら Reflector もできる。

---

super().__init__(_items) 執行了 Pipeline 當中的 __init__()，並給予參數 _items。

super().__init__(_items) は Pipeline 中の __init__()を実行して、パラメータ _items をあげる。

```python
    def __init__(self, _items):
        super().__init__(_items)
```

### def swap

Reflector 的設計為兩兩互換，這裡讓第 0 和第 1 互換，第 2 和第 3 互換，以此類推。

Reflector の<ruby>設計<rt>せっけい</rt></ruby>はペアワイズ交換する、第 0 目と第 1 目交換して、第 2 目と第 3 目交換して、こういう<ruby>風<rt>ふう</rt></ruby>に<ruby>推定<rt>すいてい</rt></ruby>する。

#### index & 1

採用二進制規則來判斷奇偶，結果為 0 是偶數，結果為 1 是奇數，例如：

バイナリで奇数か偶数かを判断する、もし結果は 0 なら、この数字が偶数を表示して、結果は 1 なら、この数字が奇数を表示する。

index = 4(十進制) = 00000100

        1(十進制) = 00000001
        
index & 1        = 00000000 = 0

index = 5(十進制) = 00000101

        1(十進制) = 00000001
        
index & 1        = 00000001 = 1

---

奇數：和前一個元素互換。

奇数の場合は、前の要素と交換して。

---

偶數：和後一個元素互換。

偶数の場合は、後ろの要素と交換して。

```python
    def swap(self, _input):
        index = self.shuffle_sequence.index(_input)
        if (index & 1) == 1:
            char = self.shuffle_sequence[index - 1]
        else:
            char = self.shuffle_sequence[index + 1]

        return char
```

reflectorTest 是個測試 Reflector 的函式，items 提供了所有的元素，注意元素的個數需要是偶數，因為 Reflector 是兩兩互換的。

これは Reflector をチェックしての関数、 items で全ての要素を提供して。 Reflector はペアワイズ交換するので、要素の数量必ず偶数を注意してください。

---

透過 reflactor 的 swap 對當中的每個元素做加密，並加入 encode 當中。

reflactor の swap で全ての要素に暗号化して、encode の中に入れて。
    
---

由於 Reflector 是兩兩互換的，因此將 encode 再次透過 swap 轉換，便會變回原本輸入的內容了。

Reflector はペアワイズ交換するので、 encode を swap 利用して、元の内容に変えます。
    
```python
def reflectorTest():
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


reflectorTest()
```
