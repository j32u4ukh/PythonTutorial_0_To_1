教學大綱；シラバス；syllabus：
1. array
2. append()
3. sort()
4. copy()
5. 索引值；インデックス; index
6. id()

---

這裡要介紹的是"陣列 array"，包含建立、添加、排序與複製。

ここは<ruby>配列<rt>はいれつ</rt></ruby> array を紹介する。<ruby>確立<rt>かくりつ</rt></ruby>、<ruby>追加<rt>ついか</rt></ruby>、<ruby>並<rt>なら</rt></ruby>べ<ruby>替<rt>か</rt></ruby>えとコピーが<ruby>含<rt>ふく</rt></ruby>まれている。

Here is going to introduce "array", includes establishing, adding, sorting and copying.

* <ruby>含<rt>ふく</rt></ruby>まれている：自動詞

---

"陣列 array"是由一連串的元素組成，元素可以都相同(都是整數)，也可以不相同，整數和字串交雜，甚至放另一個陣列進去也可以。

配列は色々な要素からなっている、これらの要素は同じでも大丈夫だが、違っても大丈夫だ。

整数と文字列は<ruby>混<rt>ま</rt></ruby>ざっている。しかも、他の配列を入れても大丈夫だ。

Array is composed by a series of elements which can all same(all is integer) or not all same. Randomly place integers and strings, or another array in the array is valid.

*　配列に格納されている要素の一つ一つの型が異なっているても大丈夫だ。

*　からなる：由...組成
*　は：強調後面；　が:強調前面

---

陣列的元素由中括弧所包住，逗號分隔每一個元素，以下示範建立。

配列の要素は<ruby>角括弧<rt>かくがっこ</rt></ruby>で<ruby>取<rt>と</rt></ruby>り<ruby>囲<rt>かこ</rt></ruby>まれていて、<ruby>読点<rt>とうてん</rt></ruby>で要素に分かれている。下記は例だ。

Elements of array are enclosed by brackets, and are separated by a comma. The following example is establishing a array.

* 下記：文章用，"下方"範例等；下：純粹的下面，某某東西的下面的

```python
array1 = [1, 2, 3]
array2 = [1, "one", 2, "二", 3, [1, 2, 3]]
print(array1)
print(array2)
```

建立了"陣列 array"之後，還可以透過 append() 添加新的元素進去。

配列は確立したあと、append() で新しい要素を追加できる。

After establishing a array, we can use append function to add a new element into the array. 

```python
array1 = [1, 2, 3]
print(array1)
array1.append(4)
print(array1)
```

有了 append() 添加元素，一開始建立"陣列 array"的時候也可以是空的，事後再將元素加進去。

append() があれば、配列を確立するのとき、何もありませんでも大丈夫だ。その後要素に追加すれば大丈夫だ。

With append function, we can establish an empty array, add elements after establishing.

```python
array3 = list()
array3.append(3)
array3.append(1)
array3.append(2)
print(array3)
```

array1 和 array3 的元素都是 1, 2, 3 只是順序不一樣，若我們想讓它由小排到大，可以利用 sort()，請看以下示範。

array1 と array3 の要素は 1, 2, 3 だが、シーケンスが違うだ。小さい物から大きい物に並べ替えしたがるなら、sort() を使ってみましょう。

Elements of array1 and array3 are 1, 2, 3, but the order is different. If we want to sort it from small to big, we can use sort function. Please see the following demonstration.

```python
array1 = [1, 2, 3]
array3 = [3, 1, 2]
array3.sort()
print(array1)
print(array3)
```

可以看到在 array3.sort() 之後，array3 的順序也變成由小排到大。如果我只想排序之後做一些操作，並不想該改到原本的陣列的話，就要透過 copy()。

array3.sort() したあと、array3 の順番は小さい物から大きい物までになる。並べ替えだけしたがるなら、copy() を使って元の配列が変えられない。

We can see that after using array3.sort(), the order of array3 become from small to big. If we want to do something after sorting, but do not want to change the origin array, we need to use copy function. 

```python
array4 = [3, 1, 2]
array5 = array4.copy()
array5.sort()
print(array4)
print(array5)
```

如果你覺得一樣是給陣列 [3, 1, 2] 的值，為何不直接 array5 = array4 就好了呢？

array4 と array5 も [3, 1, 2] をあげられるが、どうして直接的に array5 = array4 であればいい？

You may think that array4 and array5 are both equal to [3, 1, 2], why don't we directly assign array4 to array5?

---

這裡順便介紹一下，如何讀取、修改陣列中的特定值。

<ruby>因<rt>ちな</rt></ruby>みに、ここに配列の数値を取得と修正を紹介する。

By the way, following part is going to introduce how to read and modify specific values in the array.

---

可利用 陣列[索引值] 讀取或修改，索引值從 0 開始計算，長度為 3 的陣列，索引值依序為 0, 1, 2。

配列[インデックス]　のような<ruby>形<rt>かたち</rt></ruby>で取得するとか、<ruby>修正<rt>しゅうせい</rt></ruby>するとか。インデックスはゼロからカウントする。配列の長さは三たら、インデックスが　0, 1, 2。

Using the pattern likes "array[index]" to read or modify. Index is starting to count from 0, indexes of an array which length is 3 are 0, 1, 2 in order.

```python
array4 = [3, 1, 2]
array5 = array4.copy()
array5.sort()

# 讀取
print(array4[0])
print(array4[1])
print(array4[2])

# 修改
array4[0] = 4
array4[1] = 5
array4[2] = 6
print(array4)
```

現在可以正式開始示範，為何不直接 array5 = array4 就好了呢？

これから皆さんに見せて、どうして直接的に array5 = array4 しないの？

Now, we can formally start the demonstration, why not just using "array5 = array4"?

---

讓我們在 array5 = array4 之後，修改 array5 裡面的值，看看分別對 array4 和 array5 有何影響？

array5 = array4 の後、array5 中の数値を変更されて、array4 と array5 に影響はなんだろう？

Let's changing values of array5 after using "array5 = array4", and see what happened to array4 and array5.

```python
array4 = [3, 1, 2]
array5 = array4
array5[1] = 7
print(array4)
print(array5)
```

改了 array5 裡面的值， array4 的值也跟著一起改變了。這是因為 array5 = array4 的本質上，是讓 array5 去連結到和 array4 所對應的"記憶體位置"，也就是他們是同一個陣列。

array5 中の数値を変更された後、array5 中の数値も変更された。実際に array5 = array4 の意味は array5 にメモリ内の array4 の位置をリンクして、つまり、同じ配列だ。

After changing the value of array5, the value of array4 is also been changed. That is because, in essence of "array5 = array4" is to make array5 to link to the array4's position of memory. It means that they are same array.

---

我們可以利用 id() 去查詢變數的"記憶體位置"，更清楚的了解 "array5 = array4 後的 array4 和 array5 是同一個陣列"這件事。

id() でメモリの位置を<ruby>問<rt>と</rt></ruby>い<ruby>合<rt>あ</rt></ruby>わせできる。きっちり、”array4 と array5 のメモリの位置が同じ”ことを分かる。

We can use id function to query the position of memory of the variable to deeply understand that array5 and array4 are same array after using "array5 = array4".

---

而前面使用的 copy() 則是在不同的"記憶體位置"複製一份相同數值的陣列。

上の copy() を使ったら、違うメモリの位置で同じ数値の配列をコピーする。

Copy function that using above are to copy a same value array at different position of memory.

```python
array4 = [3, 1, 2]
array5 = array4
print(id(array4))
print(id(array5))

array6 = array4.copy()
print(id(array6))

array6[1] = 5
print(array4)
print(array6)
```
