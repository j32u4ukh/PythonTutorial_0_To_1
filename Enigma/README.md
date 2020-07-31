# Enigma

## Enigma 基本介紹；Enigmaの基本的な紹介；Basic introduction of Enigma

Enigma 是二戰時期納粹德國使用的一系列的加解密機器(有多種型號)。

Enigma は第二次世界大戦中にナチスドイツが使った一連の<ruby>暗号化<rt>あんごうか</rt></ruby>と<ruby>解読<rt>かいどく</ruby>する機械です（沢山種類があります）。

Enigma is a series of encryption and decryption machines (various models) used by Nazi Germany during World War II.

---

明文正序經過多個旋轉盤，抵達反射板，再反序經過原本的旋轉盤後輸出，完成加密。

クリアテキストはポジティブシーケンスな<ruby>複数<rt>ふくすう</rt></ruby>のスクランブラーから<ruby>反射板<rt>はんしゃばん）</ruby>まで、それで、<ruby>逆順<rt>ぎゃくじゅん</rt></ruby>な複数のスクランブラーで暗号化する。

The plaintext passes through multiple rotors in the positive order, reaches the reflector, and then passes through the original rotors in reverse order, and then output the completed encryption.

---

反射板的設計使得加密、解密在旋轉盤數值相同時，加密後的密文依序輸入後，可獲得加密前的明文。

反射板のデザインに暗号化と解読とき、もうしスクランブラーの数量と状態が同じなら、暗号化したの暗号文順番に輸入して、暗号化する前のクリアテキストをもらう。

The design of the reflector makes it possible to obtain the plaintext before encryption after the encrypted ciphertext is input sequentially when the encryption and decryption values are the same on the rotor.

---

也就是說，旋轉盤數值相同時，輸入 9527 得到 2468，輸入 2468 得到 9527。

つまり、スクランブラーの数量と状態が同じ場合、 9527 を輸入して 2468 をもらう、 2468 を輸入して 9527 をもらう。

In other words, when the values of the rotors are the same, enter 9527 to get 2468, and enter 2468 to get 9527.

---

此性質也導致了"加密後的字母必定不是原本的字母"這項缺點，成為破解 Enigma 的一道入口。

この性質も"暗号化した後の文字が必ず本来の文字じゃない"な欠点に<ruby>繋がる<rt>つながる</rt></ruby>、Enigma を解読されるの入口。

This property also leads to the shortcoming of "encrypted letters must not be the original letters", which has become an entrance to crack Enigma.

---

每加密"一個字母"，最右邊的旋轉盤便會旋轉一次，旋轉盤數值隨之變換，造成"每一個字母"的加密組合都不同。

毎一文字を暗号化して、最も右側のスクランブラーは一回を回して、数値を変えて、毎回の要素変換ルールが違います。

Each time a letter is encrypted, the rightmost rotor will rotate once, and the value of the rotor will change accordingly, resulting in a different encryption combination for each letter.

---

也就是當輸入 314159 可能得到 271828，明文中的兩個 1 分別被加密為 7 和 8，密文當中的兩個 2 分別來自於 3 和 5。

つまり、 314159 を輸入して 271828 もらうことを例して、クリアテキスト中の二つ 1 は暗号化して、 7 と 8 になって。暗号文の中の二つ 2 は 3 と 5 から変換しました。

That is, when you enter 314159, you may get 271828. The two 1s in the plaintext are encrypted as 7 and 8, respectively, and the two 2s in the ciphertext are from 3 and 5 respectively.

---

右邊的旋轉盤每旋轉一圈，會帶動左方的旋轉盤旋轉一次，以此類推。

右側のスクランブラーは一ラウンドを回して、左側のスクランブラーに一回を回して、こういう風に推定する。

Every time the rotor on the right rotates a round, the rotor on the left will rotate once, and so on.

---

後來又出現了"接線板"，將從反射板進入旋轉盤的密文再次加密。但"接線板"只有兩兩交換數組字母，而非全部進行加密。

”プラグボード”の<ruby>登場<rt>とうじょう</rt></ruby>は反射板からの暗号文がスクランブラーを入って前に暗号化する。だが、プラグボードは数組数字をペアワイズ交換。

Later, the plug-board appeared, and re-encrypt the cipher text which comes from the reflector and is going to enter the rotor. But the plug-board only exchanges few group of letters in pairs, not all of them are encrypted.

---

本次專案沒有實作"接線板"，有興趣的人可以自行嘗試看看。

今回のプロジェクトはプラグボードを実装しない、興味あったら、自分でやってみよう。

This project did not implement the plug-board, those who are interested can try it by yourself.

---

本專案的目的不在於介紹 Enigma，因此介紹到此為止，內容若有錯誤，還請見諒。

このプロジェクトの目的は Enigma を紹介するじゃないので、紹介はここまでだ。もし<ruby>内容<rt>ないよう</rt></ruby>はエラーがありますなら、ごめんなさい。

The purpose of this project is not to introduce Enigma, so the introduction ends here. If there are errors in the content, please forgive me.

## Enigma 特徵；Enigmaの<ruby>特徴<rt>とくちょう</rt></ruby>；Feature of Enigma

中文版
1. 每加密一次，最右邊的旋轉盤便會旋轉一次。
2. 右邊的旋轉盤每旋轉一圈，會帶動左方的旋轉盤旋轉一次，旋轉盤數值隨之變換，以此類推。
3. 加密後的密文，必和加密前的明文不同。
4. 旋轉盤可調整數值，以切換不同加密組合。

<ruby>日本語版<rt>にほんごはん</rt></ruby>
1. 毎一文字を暗号化して、最も右側のスクランブラーは一回を回す。
2. 右側のスクランブラーは一ラウンドを回して、左側のスクランブラーに一回を回して、こういう風に推定する。
3. 暗号化した後の文字が必ず本来の文字じゃない。
4. スクランブラーの状態や数値は<ruby>調整<rt>ちょうせい</rt></ruby>できる、違う要素変換ルールたちの間にスイッチする。

English version
1. Every time you encode the text, the first rotor from right will whirl one time.
2. When the rotor at right hand whirl one round, it will drive the rotor at left hand whirl one time.
3. Encoded character must different from the original character.
4. A rotor can change the number of stage to switch between different set of encoding。
