"""
    Class 3
"""
"""
    クラスメソッド、スタティックメソッド
"""

class Person:
    kind = 'human'

    def __init__(self):
        self.x = 100

    @classmethod # オブジェクトになっていない、クラスの状態でも呼び出せるメソッド
    def what_is_your_kind(cls):
        return cls.kind

    @staticmethod  # クラスに関係なく実行できる。クラス外においても問題ないが、何を表しているかわからなくなるためこのような書き方をする
    def about(year):
        print('about human {}'.format(year))

a = Person() # オブジェクトが生成される
print(a.what_is_your_kind())

b = Person  # オブジェクトを生成しない。この時点ではクラス
print(b.what_is_your_kind())
print(b.kind)

Person.about(2000)


"""
    特殊メソッド
"""
class Word:
    def __init__(self,text):
        self.text = text

    def __str__(self):
        return "WORD!!!!!"

    def __len__(self):
        return len(self.text)

    def __add__(self, word): # wordは別のオブジェクト。クラスを足し合わせる際の特殊メソッド
        return self.text.lower() + word.text.lower()

w = Word('test')
w2 = Word('########')
print(w)
print(len(w))
print(w + w2)