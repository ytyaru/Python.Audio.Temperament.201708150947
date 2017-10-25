# このソフトウェアについて

任意の基音、調(Key)における任意音階(Scale)の構成音を取得できるようにした（音律は12平均律音のみ）。

音律は12平均律固定。まだ純正律が7音しか取得できないから。

今回は12平均律音で全12調におけるメジャースケールの構成音を算出した。

# 対象ファイル名

ファイル名|説明
----------|----
testScale.py|12平均律音で全12調におけるメジャースケールの構成音の音声ファイルを出力する
MusicTheory/temperament/eq12scales/Scale.py|調と音程から構成音を算出する
MusicTheory/temperament/eq12scales/ScaleIntervals.py|各音階の構成音ごとの音程定義（12平均律用）

# 実行

```sh
$ python testScale.py 
BaseKey: A4 440Hz
12平均律
C  D  E  F  G  A  B  
C# D# F  F# G# A# C  
D  E  F# G  A  B  C# 
D# F  G  G# A# C  D  
E  F# G# A  B  C# D# 
F  G  A  A# C  D  E  
F# G# A# B  C# D# F  
G  A  B  C  D  E  F# 
G# A# C  C# D# F  G  
A  B  C# D  E  F# G# 
A# C  D  D# F  G  A  
B  C# D# E  F# G# A# 
```

`res/`配下に音声ファイルが出力される。内容は基音440HzをA4(ラ)として調律した12平均律における全調の構成音。

# 課題

* ソースコードが整理できていない
    * 音楽理論がわからず、どうまとめていいのかもわからない
* 12平均律以外の音律でも構成音を算出したいが……
    * 純正律における中間の5音も算出したい。計算方法がよくわからない
    * ピタゴラス音律はピタゴラスコンマによって減5度と増4度が同一音にならないので、ある組合せでうなりを生じる

# 開発環境

* Linux Mint 17.3 MATE 32bit
* [libav](http://ytyaru.hatenablog.com/entry/2018/08/24/000000)
    * [各コーデック](http://ytyaru.hatenablog.com/entry/2018/08/23/000000)
* [pyenv](https://github.com/pylangstudy/201705/blob/master/27/Python%E5%AD%A6%E7%BF%92%E7%92%B0%E5%A2%83%E3%82%92%E7%94%A8%E6%84%8F%E3%81%99%E3%82%8B.md) 1.0.10
    * Python 3.6.1
        * [pydub](http://ytyaru.hatenablog.com/entry/2018/08/25/000000)
        * [PyAudio](http://ytyaru.hatenablog.com/entry/2018/07/27/000000) 0.2.11
            * [ALSA lib pcm_dmix.c:1022:(snd_pcm_dmix_open) unable to open slave](http://ytyaru.hatenablog.com/entry/2018/07/29/000000)
        * [matplotlib](http://ytyaru.hatenablog.com/entry/2018/07/22/000000)
            * [matplotlibでのグラフ表示を諦めた](http://ytyaru.hatenablog.com/entry/2018/08/05/000000)

# 参考

感謝。

## 440Hz, 432Hz

* http://tabi-labo.com/156689/music-a432

## 和音の生成

* http://ism1000ch.hatenablog.com/entry/2013/11/15/182442
* https://ja.wikipedia.org/wiki/%E4%B8%89%E5%92%8C%E9%9F%B3
* https://ja.wikipedia.org/wiki/%E3%83%91%E3%83%AF%E3%83%BC%E3%82%B3%E3%83%BC%E3%83%89

## 音名

* https://ja.wikipedia.org/wiki/%E9%9F%B3%E5%90%8D%E3%83%BB%E9%9A%8E%E5%90%8D%E8%A1%A8%E8%A8%98

## 音階

* https://ja.wikipedia.org/wiki/%E9%9F%B3%E9%9A%8E

### 五度圏

* http://dn-voice.info/music-theory/godoken/

## 音高の算出

* http://www.asahi-net.or.jp/~HB9T-KTD/music/Japan/Research/DTM/freq_map.html
* http://www.nihongo.com/aaa/chigaku/suugaku/pythagoras.htm

## サイン波のスピーカ再生

* http://www.non-fiction.jp/2015/08/17/sin_wave/
* http://aidiary.hatenablog.com/entry/20110607/1307449007
* http://ism1000ch.hatenablog.com/entry/2013/11/15/182442

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

Library|License|Copyright
-------|-------|---------
[pydub](https://github.com/jiaaro/pydub)|[MIT](https://github.com/jiaaro/pydub/blob/master/LICENSE)|[Copyright (c) 2011 James Robert, http://jiaaro.com](https://github.com/jiaaro/pydub/blob/master/LICENSE)
[pygame](http://www.pygame.org/)|[LGPL](https://www.pygame.org/docs/)|[pygame](http://www.pygame.org/)

