"""
教學大綱；シラバス；syllabus：
1. class：(Object-oriented, OO)
2. Pipeline

class 又稱為'類別'，是物件導向語言的特色，就像現實中的物品一樣，會有各式各樣的屬性
以及功能。
クラスは「カテゴリ」とも呼ばれて、オブジェクト指向(しこう)言語の特徴、現実(しこう)の
ものと同じ、色々な属性(ぞくせい)と機能(きのう)があります。

＝＝＝＝＝
以智慧型手機為例，手機會有長、寬以及手機號碼等'屬性'，並擁有打電話、拍照、上網等'功能'。
スマホを例として、携帯(けいたい)は長さとか、広さとか、電話番号なんどの属性があって、
電話するとか、写真を撮るとか、インターネットをするなんどの機能があります。

＝＝＝＝＝
若以人為例，人有身高、體重、性別等'屬性'，並擁有走路、吃飯、睡覺等'功能'。
人を例として、人は身長(しんちょう)とか、体重(たいじゅう)とか、性別なんどの属性が
あって、歩くとか、食べるとか、眠るなんどの機能があります。

＝＝＝＝＝
class 當中伴隨著的變數就是上面說的'屬性'，而 class 擁有的函式就是'功能'。
class に付属(ふぞく)しているの変数は属性、関数は機能だ。

＝＝＝＝＝
'非物件導向語言'雖然一樣有變數和函式，但這些變數與函式並不附屬於誰，而是分別各自
獨立的，希望以下示範能讓各位理解上面的說明。
非オブジェクト指向言語も変数と関数がありますが、この変数と関数は誰にも付属(ふぞく)
してはない、別々に独立(どくりつ)なものだ。下の例は皆に上の説明を分かれば良かった。

＝＝＝＝＝
物件的格式是以 class 開頭，後面可以自己替這個物件取名，每個字的開頭用大寫英文字母。
最後是冒號，冒號以下便是對這個物件的設定。
オブジェクトは class に始めて、名前をとる、ひとつずつ単語が大文字始めて、最後はコロン
、それの下からはオブジェクトの設定することだ。
"""
import math
# from random import shuffle
from random import randint


class SmartPhone:
    """
    物件需要'建立'之後才能使用，下面會示範如何建立，而這個 __init__ 便是在說明
    '建立'的時候需要提供哪些參數，以及要執行哪些事情。
    オブジェクトは構築したあと使われできる、これからどうやって構築するこよを
    デモンストレーションしています。この __init__ は構築するときなにか必要な
    パラメータと実行することを説明します。

    ＝＝＝＝＝
    __init__ 前後分別兩個 _ 構成，是預設的函數名稱，並非是可以隨自己取的名稱。括弧內
    便是'建立'的時候需要提供哪些參數。而 __init__ 包含的三行程式碼則是'建立'時會
    執行的事情。
    __init__ の前と後ろはそれぞれ二つ _ に構成(こうせい)して、デフォルト関数の名前
    、自分で勝手(かって)に命名してはいけない。丸括弧の中には提供(ていきょう)するが
    必要なパラメータ。下の三行は構築するとき実行するなこと。

    ＝＝＝＝＝
    self 是一個代表這個物件的變數，這個變數是可以自己取的，但建議沿用大家的慣例。
    self はある変数でこのオブジェクトに代表する。この変数の名前は自分で命名しては
    できるけど、皆の習慣(しゅうかん)を続け方がいいと思う。
    """

    def __init__(self, _width, _height, _phone_number):
        """
        self.width 是個變數，就是表示這個物件的 width，而 _width 則是物件外面
        提供的變數，只存在於這個 __init__ 當中，若想在物件的其他地方使用，就需要將
        變數內容儲存在物件本身的變數(屬性)當中。
        self.width はある変数でこのオブジェクトの広さに代表する。一方、 _width は
        外から提供するの変数、この __init__ 中だけで読まわれできる。オブジェクトの
        他の部分も読みたいなら、オブジェクトの属性に保存しなければならない。
        """
        self.width = _width
        self.height = _height
        self.phone_number = _phone_number

    """
    智慧型手機這個物件，擁有打電話功能，要使用這個功能時，需要提供對方的電話號碼，
    才知道要打給誰。
    スマホというオブジェクトは電話するの機能があります、使うとき相手の電話番号が必要
    だ、それで誰に電話することが分かりますか。

    ＝＝＝＝＝
    函式的第一個變數通常會放 self ，如此一來便能在函式當中使用這個物件的變數(屬性)，
    或物件的函式(功能)。
    関数に最初の変数は普通に self を入れって、そして、関数の中でオブジェクトの属性
    と機能が使われている。

    ＝＝＝＝＝
    若不需要使用這個物件的變數或函式，則會有其他寫法，以後遇到再說明即可。
    もしオブジェクトの属性と機能は必要がないなら、別の書き方があります、その時で
    説明すればいい。
    """

    def call(self, _number_to_call):
        """
        在物件內部要使用物件的變數或函式時，前面會帶有 self 這個字，表示它是物件
        本身的變數，就像下方寫法一樣。
        変数の前に self がありますなら、’この変数はオブジェクトの属性’を表示する。
        """
        print("{} call to {}.".format(self.phone_number, _number_to_call))

    def getPhoneNumber(self):
        return self.phone_number


"""
前面定義完 SmartPhone ，這裡已屬於物件的外面，因此要使用物件的變數或函式時，需要先
建立物件，再利用代表物件的變數後面接'.'再接屬性或功能的名稱。
前に SmartPhone を定義(ていぎ)しました、ここはもうオブジェクトの外だから、
オブジェクトの属性または機能を使いたいなら、先ずはオブジェクトを構築して、代表するの
変数の後ろで小数点を付けて(つけて)、さらに属性または機能の呼び名を付ける。

＝＝＝＝＝
建立物件時，等號左邊利用變數來代表這個物件，等號右邊則是物件名稱，括弧中則輸入所需參數。
オブジェクトを構築するとき、等号(とうごう)の左側は変数でこのオブジェクトを代表する、
右側はオブジェクトの名前と必要なパラメータ。
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
以下再以圖形物件作為示範，幫助各位理解使用物件導向的好處。
下は形(かたち)オブジェクトを例として、皆にオブジェクト指向(しこう)を使うの
長所(ちょうしょ)を理解するのに役立(やくだ)ちました。
"""


class Rectangle:
    def __init__(self, _width, _height):
        self.width = _width
        self.height = _height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * (self.width + self.height)


class Circle:
    def __init__(self, _radius):
        self.radius = _radius
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

"""
最後以 Enigma 中使用到的物件為例，以下會做一些簡化與修改，和最終版本不會完全相同。
最後は Enigma 中に使われてオブジェクトを例として説明します。でもこれは簡単なバージョン、
最後のバージョンと完全同じじゃない。

＝＝＝＝＝
Pipeline 物件將接收一個陣列，並轉換成兩個'元素相同'但'順序不同'的陣列。
オブジェクト Pipeline は一つ配列をもらって、二つ「順番は違うでも要素は同じ」の配列になります。

＝＝＝＝＝
一個按照順序排列，一個保留原本輸入時的順序。
一つは順番に並んで、もう一つの順番は輸入したと同じ。

＝＝＝＝＝
同時提供兩個函式，分別利用索引值與陣列內容去反查。
そして、二つ関数を提供して、それぞれはインデックスと配列の内容で相手をお互いを探している。
"""


class Pipeline:
    """  __init__
    建立 Pipeline 物件的同時會執行 __init__ 內定義的程式碼。

    オブジェクト　Pipeline　を建立（こんりゅう）する時、__init__で
    定義（ていぎ）したのコードも実行（じっこう）する。
    """

    def __init__(self, _items):
        """
        參數 _items 提供 self.origin_sequence '順序不同'但'元素相同'的陣列，
        例如：[1, 2, 3], [1, 3, 2], [3, 1, 2]。

        パラメータ　_items　は　self.origin_sequence　に「順番（じゅんばん）は
        違うでも要素（ようそ）は同じ」の配列（はいれつ）を提供（ていきょう）する。
        例えば：[1, 2, 3], [1, 3, 2], [3, 1, 2]。
        """
        self.origin_sequence = _items.copy()

        """
        將 self.origin_sequence 排序，獲得相同順序的元素陣列。
        例如：[1, 3, 2], [3, 1, 2] → [1, 2, 3], [1, 2, 3]。

        同じ順番の要素配列のために、self.origin_sequence を並べ替えする。
        例えば：[1, 3, 2], [3, 1, 2] → [1, 2, 3], [1, 2, 3]。
        """
        self.origin_sequence.sort()

        """
        self.shuffle_sequence 保留原本輸入時的順序，用於建立元素轉換規則，
        例如：1 → 2；5 → 3；2 → 7。

        輸入（ゆにゅう）したの順番を保存するの　self.shuffle_sequence で「要素変換
        （へんかん）ルール」を建立する。
        """
        self.shuffle_sequence = _items.copy()

        """
        self.length 儲存陣列長度。

        self.length　は配列の長さを保存する。
        """
        self.length = len(_items)

    """
    返回 _char 在 self.origin_sequence 中的索引值，若不在當中則返回 -1。
    
    self.origin_sequence での _char のインデックスを戻って、もし中にいないなら -1 を戻って。
    """

    def getIndex(self, _char):
        try:
            """
            返回 _char 在 self.origin_sequence 中的索引值，若不在當中則產生 ValueError。
            
            self.origin_sequence での _char のインデックスを戻って、もし中にいないなら
            ValueError を発生する。
            """
            return self.origin_sequence.index(_char)
        except ValueError:
            """
            _char 不在 self.origin_sequence 當中，則返回 -1。尚未處理返回 -1時的情形。
            
            _char は self.origin_sequence の中にいないの場合は -1 を戻って。
            """
            return -1

    """
    根據索引值取得字元，處理超出範圍的索引值，使其產生以下效果：
    索引值最後一位 +1 後回到第一位，同樣的，第一位 -1 後回到最後一位。
    
    インデックスで紐をもらって、そして、インデックスの範囲を超えて(こえて)場合に対処(たいしょ)して、下の効果に生成(せいせい)する：
    最後のインデックスたす 1 なら 0 になって、そして、最初のインデックスひく 1 なら最後のインデックスになります。
    """

    def getChar(self, _index):
        """
        索引值小於 0 時，索引值加陣列長度。

        インデックスは小なり（しょうなり） 0 なら、配列の長さを足して。
        """
        if _index < 0:
            _index += self.length

        """
        索引值大於陣列長度時，索引值取'除以陣列長度'後的餘數。
        
        インデックスは大なり（だいなり）配列の長さなら、インデックスは’配列の長さに割られる’あと残り数字。
        """
        if self.length <= _index:
            _index %= self.length

        """
        返回調整後的索引值指向的陣列中的字元。
        
        調整（ちょうせい）したのインデックスでもらったの紐を戻って。
        """
        return self.origin_sequence[_index]


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
