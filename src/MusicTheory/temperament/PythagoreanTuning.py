#https://ja.wikipedia.org/wiki/%E3%83%94%E3%82%BF%E3%82%B4%E3%83%A9%E3%82%B9%E9%9F%B3%E5%BE%8B
#ピタゴラス音律
#減5度と増4度は平均律では同一音だが、ピタゴラス音律では約23.46セント≒1/4半音の差が生じる。この差をピタゴラスコンマと呼ぶ。
#この音程の外れた五度による和音は、顕著なうなりを生じるため、狼の吠声に例えてウルフの五度と呼ばれる。
#結果、ピタゴラス音律では演奏可能な調は制限される。
class PythagoreanTuning:
    def __init__(self):
        self.__DENOMINATOR = 12
        self.__BaseFrequency = 440 #基準となる音をA4(ラ)とし、周波数を440として算出する
        self.__Frequencies = []
        # 減5, 短2, 短6, 短3, 短7, 4, 1, 5, 長2, 長6, 長3, 長7, 増4
        self.__calcFrequencies()
    
    def __calcFrequencies(self):
        self.__Frequencies.clear()
        self.__Frequencies.extend([f for f in self.__calcMinusInOctave()])
        self.__Frequencies.extend([f for f in self.__calcPlusInOctave()])
        self.__Frequencies.sort()
    
    # return: [4, 短7, 短3, 短6, 短2] 減5は増4と同じはずだがピタゴラス音律においては別の音になってしまう（ピタゴラスコンマ）ので省く
    def __calcMinusInOctave(self):
        for x, y in ((1,1), (2,2), (3,2), (4,3), (5,3)):
            yield (((2/3)**x) * (2**y)) * self.__BaseFrequency
    
    # return: [1, 5, 長2, 長6, 長3, 長7, 増4]
    def __calcPlusInOctave(self):
        yield self.__BaseFrequency #1度
        yield 3/2 * self.__BaseFrequency #5度
        for x, y in ((2,1), (3,1), (4,2), (5,2), (6,3)):
            yield (((3/2)**x) * (1/2**y)) * self.__BaseFrequency
    
    @property
    def BaseFrequency(self): return self.__BaseFrequency
    @BaseFrequency.setter
    def BaseFrequency(self, v):
        if 0 < v:
            self.__BaseFrequency = v
            self.__calcFrequencies()
    @property
    def Frequencies(self): return self.__Frequencies


if __name__ == '__main__':
    ji = PythagoreanTuning()
    print(ji.Frequencies)
    print('---------- 1オクターブ下 ----------')
    print([f/2 for f in ji.Frequencies])
    print('---------- 1オクターブ上 ----------')
    print([f*2 for f in ji.Frequencies])

