教學大綱；シラバス；syllabus：
1. class：(Object-oriented, OO)
2. Pipeline

---

class 又稱為'類別'，是物件導向語言的特色，就像現實中的物品一樣，會有各式各樣的屬性以及功能。

クラスは"カテゴリ"とも呼ばれて、オブジェクト<ruby>指向<rt>しこう</rt></ruby>言語の特徴、現実のものと同じ、色々な<ruby>属性<rt>ぞくせい)と<ruby>機能<rt>きのう</rt></ruby>があります。

Class, also known as'category', is a feature of object-oriented language. Just like real objects, it has various attributes and functions.

---

以智慧型手機為例，手機會有長、寬以及手機號碼等'屬性'，並擁有打電話、拍照、上網等'功能'。

スマホを例として、携帯は長さとか、広さとか、電話番号なんどの属性があって、電話するとか、写真を撮るとか、インターネットをするなんどの機能があります。

Taking a smart phone as an example, the mobile phone will have "attributes" such as length, width, and mobile phone number, and have "functions" for making calls, taking pictures, and surfing the Internet.

---

若以人為例，人有身高、體重、性別等'屬性'，並擁有走路、吃飯、睡覺等'功能'。

人を例として、人は<ruby>身長<rt>しんちょう</rt></ruby>とか、<ruby>体重<rt>たいじゅう</rt></ruby>とか、性別なんどの属性があって、歩くとか、食べるとか、眠るなんどの機能があります。

Taking people as an example, people have 'attributes' such as height, weight, and gender, and have 'functions' such as walking, eating, and sleeping.

---

class 當中伴隨著的變數就是上面說的'屬性'，而 class 擁有的函式就是'功能'。

class に<ruby>付属<rt>ふぞく</rt></ruby>しているの変数は属性、関数は機能だ。

The variable with-in class is the'attribute' mentioned above, and the method that class has is the'function'.

---

'非物件導向語言'雖然一樣有變數和函式，但這些變數與函式並不附屬於誰，而是分別各自獨立的，希望以下示範能讓各位理解上面的說明。

非オブジェクト指向言語も変数と関数がありますが、この変数と関数は誰にも付属してはない、別々に<ruby>独立<rt>どくりつ</rt></ruby>なものだ。下の例は皆に上の説明を分かれば良かった。

Although 'non-object-oriented language' also has variables and methods, they are not belong to anyone, but are independent separately. I hope the following demonstration will make you understand the above description.

---

物件的格式是以 class 開頭，後面可以自己替這個物件取名，每個字的開頭用大寫英文字母。

オブジェクトは class に始めて、名前をとる、ひとつずつ単語が大文字始めて。

The format of the object starts with class, and you can name this object later, with capital English letters at the beginning of each word.

---

最後是冒號，冒號以下便是對這個物件的設定。

最後はコロン、それの下からはオブジェクトの設定することだ。

The last is the colon, and the settings below this colon are for this object.

```python
import math
# from random import shuffle
from random import randint


class SmartPhone:
```

物件需要'建立'之後才能使用，下面會示範如何建立。

オブジェクトは構築したあと使われできる、これからどうやって構築するこよをデモンストレーションしています。

Objects need to be'created' before they can be used. The following will demonstrate how to create them.

### def __init__

這個 __init__ 便是在定義'建立'的時候需要提供哪些參數，以及要執行哪些事情。

この __init__ は構築するときなにか必要なパラメータと実行することを定義します。

This __init__ defines what parameters need to be provided when building the object and what things will perform.

---

__init__ 前後分別兩個 _ 構成，是預設的函數名稱，並非是可以隨自己取的名稱。

__init__ の前と後ろはそれぞれ二つ _ に<ruby>構成<rt>こうせい</rt></ruby>して、デフォルト関数の名前、自分で<ruby>勝手<rt>かって</rt></ruby>に命名してはいけない。

There are two _ before and after __init__, which is the default function name, not a name that can be taken by yourself.

---

括弧內便是'建立'的時候需要提供哪些參數。

丸括弧の中には<ruby>提供<rt>ていきょう</rt></ruby>するが必要なパラメータ。

The brackets are the parameters that need to be provided when 'building'.

---

__init__ 包含的三行程式碼則是'建立'時會執行的事情。

下の三行は構築するとき実行するなこと。

The three-line code included in __init__ is what will be executed during 'building'.

---

self 是一個代表這個物件的變數，這個變數是可以自己取的，但建議沿用大家的慣例。

self はある変数でこのオブジェクトに代表する。この変数の名前は自分で命名してはできるけど、皆の<ruby>習慣<rt>しゅうかん</rt></ruby>を続け方がいいと思う。

"self" is a variable that represents this object. The name of variable can be taken by yourself, but it is recommended to follow convention.

---

self.width 是個變數，就是表示這個物件的 width。

self.width はある変数でこのオブジェクトの広さに代表する。

self.width is a variable, which means the width of this object.

---

而 width 則是物件外面提供的變數，在物件當中只存在於這個 __init__ 當中，無法在物件的其他函式中取得。

一方、width は外から提供して変数、このブジェクトの __init__ 中だけで読まわれできる、このブジェクトの他の関数の中は読まわれできない。

And width is a variable provided outside the object, which only exists in this __init__ in the object, and cannot be obtained in other functions of the object.

---

若想在物件的其他地方使用，就需要將變數內容儲存在物件本身的變數(屬性)當中。

オブジェクトの他の部分も読みたいなら、オブジェクトの属性に保存しなければならない。

If you want to use it elsewhere in the object, you need to store the variable content in the variable (attribute) of the object itself.

```python
    def __init__(self, width, height, _phone_number):
        self.width = width
        self.height = height
        self.phone_number = _phone_number
```

### def call

智慧型手機這個物件，擁有打電話功能，要使用這個功能時，需要提供對方的電話號碼，才知道要打給誰。

スマホというオブジェクトは電話するの機能があります、使うとき相手の電話番号が必要だ、それで誰に電話することが分かりますか。

The object, smart phone, has a call function. To use this function, you need to provide the phone number of the other to know who to call.

---

函式的第一個變數通常會放 self ，如此一來便能在函式當中使用這個物件的變數(屬性)，或物件的函式(功能)。

関数に最初の変数は普通に self を入れって、そして、関数の中でオブジェクトの属性と機能が使われている。

The first variable of a function is usually put in "self", so that you can use the variable (attribute) of the object or the function (function) of the object in the function.

---

若不需要使用這個物件的變數或函式，則會有其他寫法，以後遇到再說明即可。

もしオブジェクトの属性と機能は必要がないなら、別の書き方があります、その時で説明すればいい。

If you don't need to use the variable or function of this object, there will be other ways of writing. We will explain that when we encounter the situation.

---

在物件內部要使用物件的變數或函式時，前面會帶有 self 這個字，表示它是物件本身的變數，就像下方寫法一樣。

変数の前に self がありますなら、’この変数はオブジェクトの属性’を表示する。

當在對象內部使用對象的變量或函數時，單詞self會帶有前綴，以表示它是對象本身的變量，就像下面的寫法一樣。

```python
    def call(self, _number_to_call):
        print("{} call to {}.".format(self.phone_number, _number_to_call))

    def getPhoneNumber(self):
        return self.phone_number
```

前面定義完 SmartPhone ，這裡已屬於物件的外面，因此要使用物件的變數或函式時，需要先建立物件，再利用代表物件的變數後面接'.'再接屬性或功能的名稱。

前に SmartPhone を<ruby>定義<rt>ていぎ</rt></ruby>しました、ここはもうオブジェクトの外だから、オブジェクトの属性または機能を使いたいなら、先ずはオブジェクトを構築して、代表するの変数の後ろで小数点を<ruby>付<rt>つ</rt></ruby>けて、さらに属性または機能の呼び名を付ける。

The SmartPhone is defined above, and here has be belonged to the outside of the object. Therefore, to use the variable or function of the object, you need to create the object first, and then use the variable representing the object followed by '.' and followed by the name of the attribute or function.

---

建立物件時，等號左邊利用變數來代表這個物件，等號右邊則是物件名稱，括弧中則輸入所需參數。

オブジェクトを構築するとき、<ruby>等号<rt>とうごう</rt></ruby>の左側は変数でこのオブジェクトを代表する、右側はオブジェクトの名前と必要なパラメータ。

When creating an object, the left side of the equal sign uses variables to represent the object, the right side of the equal sign is the object name, and the required parameters are entered in parentheses.

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

以下再以圖形物件作為示範，幫助各位理解使用物件導向的好處。

下は<ruby>形<rt>かたち</rt></ruby>オブジェクトを例として、皆にオブジェクト<ruby>指向<rt>しこう</rt></ruby>を使うの<ruby>長所<rt>ちょうしょ</rt></ruby>を理解するのに<ruby>役立<rt>やくだ</rt></ruby>ちました。

The following uses graphic objects as an example to help you understand the benefits of using object-oriented again.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * (self.width + self.height)


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = 2 * self.radius

    def getArea(self):
        return self.radius * self.radius * math.pi

    def getPerimeter(self):
        return self.diameter * math.pi


square = Rectangle(5, 5)
rectangle = Rectangle(5, 8)
circle = Circle(5.3)

print("square area:{}, perimeter:{}".format(
    square.getArea(),
    square.getPerimeter()))

print("rectangle area:{}, perimeter:{}".format(
    rectangle.getArea(),
    rectangle.getPerimeter()))

print("circle area:{}, perimeter:{}".format(
    circle.getArea(),
    circle.getPerimeter()))
```

最後以 Enigma 中使用到的物件為例，以下會做一些簡化與修改，和最終版本不會完全相同。

最後は Enigma 中に使われてオブジェクトを例として説明します。でもこれは簡単なバージョン、最後のバージョンと完全同じじゃない。

Finally, taking the objects used in Enigma as an example, the following will do some simplifications and modifications, which will not be completely the same as the final version.

---

Pipeline 物件將接收一個陣列，並轉換成兩個'元素相同'但'順序不同'的陣列。

オブジェクト Pipeline は一つ配列をもらって、二つ"順番は違うでも要素は同じ"の配列になります。

Object, Pipeline, will receive an array and convert it into two arrays with the same elements but different sequences.

---

一個按照順序排列，一個保留原本輸入時的順序。

一つは順番に並んで、もう一つの順番は輸入したと同じ。

One is in order, and the other keeps the original order.

---

同時提供兩個函式，分別利用索引值與陣列內容去反查。

そして、二つ関数を提供して、それぞれはインデックスと配列の内容で相手をお互いを探している。

At the same time, provide two functions which use index and the content of the array to check back each other.

```python
class Pipeline:
```

### def __init__

建立 Pipeline 物件的同時會執行 __init__ 內定義的程式碼。

オブジェクト　Pipeline　を<ruby>建立<rt>こんりゅう</rt></ruby>する時、__init__で定義したのコードも実行する。

The code defined in __init__ will be executed when the Pipeline object is created.

---

參數 items 提供 self.origin_sequence '順序不同'但'元素相同'的陣列，例如：[1, 2, 3], [1, 3, 2], [3, 1, 2]。

パラメータ　items　は　self.origin_sequence　に「<ruby>順番<rt>じゅんばん</rt></ruby>は違うでも<ruby>要素<rt>ようそ</rt></ruby>は同じ」の配列を<ruby>提供<rt>ていきょう</rt></ruby>する。例えば：[1, 2, 3], [1, 3, 2], [3, 1, 2]。

The parameters "items" provides arrays which have 'different order' but 'same elements' to self.origin_sequence, for example: [1, 2, 3], [1, 3, 2], [3, 1, 2].

---

將 self.origin_sequence 排序，獲得相同順序的元素陣列。例如：[1, 3, 2], [3, 1, 2] → [1, 2, 3], [1, 2, 3]。

同じ順番の要素配列のために、self.origin_sequence を並べ替えする。例えば：[1, 3, 2], [3, 1, 2] → [1, 2, 3], [1, 2, 3]。

Sort self.origin_sequence to obtain arrays of elements in the same order. For example: [1, 3, 2], [3, 1, 2] → [1, 2, 3], [1, 2, 3].

---

self.shuffle_sequence 保留原本輸入時的順序，用於建立元素轉換規則，例如：1 → 2；5 → 3；2 → 7。

<ruby>輸入<rt>ゆにゅう</rt></ruby>したの順番を保存するの　self.shuffle_sequence で「要素<ruby>変換<rt>へんかん</rt></ruby>ルール」を建立する。

self.shuffle_sequence retains the original input sequence and is used to establish element conversion rules, for example: 1 → 2; 5 → 3; 2 → 7.

---

self.length 儲存陣列長度。

self.length　は配列の長さを保存する。

self.length stores the array length.
        
```python
    def __init__(self, items):
        self.origin_sequence = items.copy()
        self.origin_sequence.sort()
        self.shuffle_sequence = items.copy()
        self.length = len(items)
```

### def getIndex

返回 char 在 self.origin_sequence 中的索引值，若不在當中則返回 -1。

self.origin_sequence での char のインデックスを戻って、もし中にいないなら -1 を戻って。

Returns the index value of char in self.origin_sequence, or -1 if it is not contained in array.

```python
    def getIndex(self, char):
        try:
            return self.origin_sequence.index(char)
        except ValueError:
            return -1
```

### def getChar

根據索引值取得字元，處理超出範圍的索引值，使其產生以下效果：索引值最後一位 +1 後回到第一位，同樣的，第一位 -1 後回到最後一位。

インデックスで紐をもらって、そして、インデックスの範囲を<ruby>超<rt>こ</rt></ruby>えて場合に<ruby>対処<rt>たいしょ</rt></ruby>して、下の効果に<ruby>生成<rt>せいせい</rt></ruby>する：最後のインデックスたす 1 なら 0 になって、そして、最初のインデックスひく 1 なら最後のインデックスになります。

Obtain characters based on the index value, and process the index value beyond the range to produce the following effect: index value will turn back to the first one after the last index plus one, and similarly, index value will turn back to the last one after the first index minus one.

---

索引值小於 0 時，索引值加陣列長度。

インデックスは<ruby>小<rt>しょう</rt></ruby>なり 0 なら、配列の長さを足して。

When the index value is less than 0, the index value plus the value of array length.

---

索引值大於陣列長度時，索引值取'除以陣列長度'後的餘數。

インデックスは<ruby>大<rt>だい</rt></ruby>なり配列の長さなら、インデックスは’配列の長さに割られる’あと残り数字。

When the index value is greater than the array length, the index value is taken as the remainder after dividing by the array length.

---

返回調整後的索引值指向的陣列中的字元。

<ruby>調整<rt>ちょうせい</rt></ruby>したのインデックスでもらったの紐を戻って。

Returns the character in the array pointed to by the adjusted index value.

```python
    def getChar(self, index):
        if index < 0:
            index += self.length

        if self.length <= index:
            index %= self.length

        return self.origin_sequence[index]


items = [randint(0, 5) for i in range(3)]
print("origin items:", items)
pipeline1 = Pipeline(items)
pipeline2 = Pipeline(items)

print("pipeline1.origin_sequence:", pipeline1.origin_sequence)
print("pipeline1.shuffle_sequence:", pipeline1.shuffle_sequence)
print("pipeline2.origin_sequence:", pipeline2.origin_sequence)
print("pipeline2.origin_sequence:", pipeline2.shuffle_sequence)

print(pipeline1.getChar(4))
print(pipeline1.getChar(8))
for i in range(5):
    print(i, pipeline1.getIndex(i))
```



