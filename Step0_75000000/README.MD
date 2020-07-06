"""
教學大綱；シラバス；syllabus：
1. import
2. from
3. 多個 import；複数の import; multiple imports
4. pip

---

這個世界上有許多工程師樂於分享他們所寫的程式，使用別人事先寫好的程式，可以讓我們省去很多麻煩。

この世の沢山エンジニアは彼らが書いたのプログラムを皆に共有する。これを使って、もっと簡単に自分のプログラムを完成する。

Many engineers in this world are happy to share the programs they write. Using programs written by others in advance can save us a lot of trouble.

---

他們會根據程式的功能與內容，利用資料夾把程式碼做分類，並把所有程式碼打包起來供其他人使用，我們使用的這個又叫做'套件'。

彼らはプログラムの機能と内容にフォルダーで<ruby>分類<rt>ぶんるい</rt></ruby>して皆に使われる、最も上のフォルダーが”パッケージ”と呼ばれる。

They will use the folder to classify the code according to the function and content of the program, and package all the code for other people to use. So the one we use is also called 'package'.

---

當我們要使用'套件'，首先要下載，然後是 import 。

パッケージを使いたいなら、それをダウンロードして、 import を使って。

When we want to use the 'package', we first need to download it, then import.

---

這裡先說明 "import" ，比如：數學計算使很常會使用到的功能，因此有個"套件"名稱叫做 math ，使用方式如下。

先ずは import を説明しよう、例えば：数学の計算が沢山使われるので、math というのパッケージがあります。使い方は下のようにしてください。

Here we first explain "import", for example: functions which are commonly used in mathematical calculations will be combined into a package called "math", which is used as follows.

```python
import math

print(math.log10(100))  # 2.0
```

第一行告訴程式我要引入 math 這個'套件'。

第一行はプログラムに” math というパッケージをインポートしてください”に教えて。

The first line tells the program that I want to import the "package" called math.

---

math 後一點接著 log10 表示我要使用 math 當中的 log10 這個函式。

math の後ろの点は log10 を続いて、 math の関数 log10 を使うことです。

The point attachs to math follows with "log10" that means I want to use the function log10 in the "math".

---

log10 是以 10 為底的 log ，log2 是以 2 為底的 log ，是指數的反函數，log2(8) = 3 表示 8 是 2 的 3 次方，以此類推。

log10 は「底(てい)を 10 とするの対数」、log2 は「底を 2 とするの対数」、<ruby>指数<rt>しすう</rt></ruby>の<ruby>逆関数<rt>ぎゃくかんすう</rt></ruby>。log2(8) = 3 は「8 が 2 の 3 乗」の意味です。

log10 is a log with a base of 10, log2 is a log with a base of 2. It is the inverse function of the exponent. log2(8) = 3 means that two cubed is eight and so on.

---

下面示範另一種引入方式，利用 from 這個字，告訴程式這個 log2 是'套件' math 下面的 log2 ，所以可以不用像前面一個例子，前面還要寫 math，而是可以直接用。

他のインポートするの例は下があります。 from でプログラムに”この log2 は math からの log2 ”に教えるので、前の例と違う、 log2 を<ruby>直接<rt>ちょくせつ</rt>使用<rt>しよう</rt></ruby>が大丈夫です。

Let's demonstrate another way to import, using the word "from", to tell the program that log2 is the log2 belongs the'package' math, so you can directly to use without math. You don't have to do as the previous example.

```python
from math import log2

print(log2(8))  # 3.0
```

當我們從同一個套件 import 了多個函式進來時，可以有以下幾種方式，以 log2 和 log10 為例：

私たちは同じパッケージから複数の関数をインポートしているとき、複数の方法があります。log2 と log10 を例として説明します。

When we import multiple functions from the same package, there are several ways below to take log2 and log10 as examples:

---

1. import 共同套件，使用時前面都加上套件名稱，優點是可以清楚知道這個函式來自哪個套件，但缺點就是程式碼會變得比較長。

1. <ruby>共通<rt>きょうつう</rt></ruby>するパッケージをインポートして、使うとき、関数の前にこのパッケージの名前を続いて。<ruby>長所<rt>ちょうしょ</rt></ruby>はこの関数がどのパッケージからことをはっきり分かる、<ruby>短所<rt>たんしょ</rt></ruby>はコードの長さが長くなる。

1. Import the joint package, add the package name before use, the advantage is that you can clearly know which package this function comes from, but the disadvantage is that the code will become longer.

```python
import math
# math.log2(...)
# math.log10(...)
```

2. 一個函式一行引用，優點是不需要引用某個函式時，可以快速移除，但缺點是重複的內容太多，不是個好的做法。

2. <ruby>一行<rt>いちぎょう</rt></ruby>に一つ関数をインポートして、長所は関数が要らないとき、すぐに<ruby>削除<rt>さくじょ</rt></ruby>できます。短所は<ruby>重複<rt>ちょうふく</rt></ruby>コンテンツが多くすぎて、いい方法じゃないと思います。

2. Each line import a function, the advantage is that when a function is not needed, it can be quickly removed, but the disadvantage is that there is too much duplicate content, which is not a good way.

```python
from math import log2

from math import log10
```

3. 用逗號分隔同個套件下的不同函式，優點是省去了前一種方法重複的內容，缺點是當引用的數量一多，這行引用也會變得過長。

3. <ruby>読点<rt>とうてん</rt></ruby>で同じパッケージの関数に分かれる。長所はコンテンツが重複しない、でも短所はインポートされるの数量が多くになると、コードの長さも長くなる。

3. Separate different functions under the same package with a comma. The advantage is to save the repeated content likes the previous method. The disadvantage is that when the number of references is more, this line of references will become too long.

```python
from math import log2, log10
```

4. 用逗號分隔同個套件下的不同函式，搭配括號來換行，優點是排除了前一種方法的缺點。

4. <ruby>丸括弧<rt>まるかっこ</rt></ruby>で関数を<ruby>取<rt>と</rt></ruby>り<ruby>囲<rt>かこ</rt></ruby><rt>んで、これなら前の方法の欠点がいなくなる。

4. Separate different functions under the same package with commas, and use parentheses to wrap, the advantage is to eliminate the disadvantages of the former method.

```python
from math import (
          log2, 
          log10
          )
```

最一開始提到，要使用'套件'前需要進行安裝，但這個安裝並不是在這裡執行，而是在 cmd 當中，因此把它的說明放到了最後。

最初の時言った、パッケージを使いたいなら、<ruby>設置<rt>せっち</rt></ruby>しなければならない。だが、ここでインストールではない、 cmd に実行するです。だから、最後のところに説明をします。

It was mentioned at the beginning that you need to install before using the 'package', but the installation is not performed here, but in cmd, so its description is put to the end.

---

cmd 可以直接在電腦中開啟搜尋，並輸入 cmd 後便可開啟。

コンピューターで<ruby>検索<rt>けんさく</rt>機能<rt>きのう</rt></ruby>開けて、cmd を入れって、cmd が開けられる。

To open cmd, we can use the search function of computer and enter the cmd.

---

一般會建議初學者透過 Anaconda 來安裝 Python。

<ruby>一般的<rt>いっぱんてき</rt></ruby>に言えば、<ruby>初心者<rt>しょしんしゃ</rt></ruby>に” Anaconda で設置して方がいい”を<ruby>提案<rt>ていあん</rt></ruby>する。

It is generally recommended that beginners install Python through Anaconda.

---

因此要安裝套件時，需要先進入所謂的'虛擬環境'，然後輸入 pip install XXX 來進行安裝。

だから、設置しているとき、先ずは"<ruby>仮想<rt>かそう</rt>環境<rt>かんきょう</rt></ruby>"に<ruby>入<rt>はい</rt></ruby>って、pip install XXX を<ruby>入<rt>い</rt></ruby>れて設置する。

Therefore, to install the package, you need to enter the so-called 'virtual environment', and then enter "pip install XXX" to do the installation.

---

而 Python 本身也有附帶一些'套件'，可以讓你省去安裝這個步驟，'套件' math 就是其中一個例子。

Python は少しパッケージを<ruby>添付<rt>てんぷ</rt></ruby>して、設置が要らない。例えば： math というのパッケージ。

Python attaches some package itself that can save you the process to install packages. The package math is one example.

---

我知道上面的說明對'初學者'可能有看沒有懂。

上の説明は初心者にまだ難しい。

I know that the above instructions are difficult to beginners.

---

在這個檔案在的資料夾當中，還有一個叫做 pip_learning.md 的檔案，裡面有圖片說明應該會比較清楚。

このファイルが入っているフォルダー内は pip_learning.md というのファイルがあります、写真を連れて、理解やすいと思います。

In the folder where this file is located, there is also a file called pip_learning.md, which contains pictures that should illustrate more clearly.

---

當整份教程完成後，我也會將一些過程中使用到但沒有說明的部分一併補上的。

全てのチュートリアルは完成したあと、使ったけど説明されない部分を<ruby>追記<rt>ついき</rt></ruby>します。

When the entire tutorial is completed, I will also add some parts that are used in the process but are not explained.
