"""
    関数の引数の基礎
"""

"""
位置引数のタプル化
"""
def say_something(word, *args):
    print("word = ", word)
    for arg in args:
        print(arg)

say_something('Hi!', 'Mike', 'Nanncy')
# t = ('Mike', 'Nanncy')
# say_something('Hi!', 'Mike', *t)


"""
キーワード引数の辞書化
"""
def menu(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

d = {
    'entree':'beef',
    'drink':'coffee',
    'dessert':'ice'
}
menu(**d)


"""
位置引数とキーワード引数を同時に使う

　位置引数：タプル
　KW引数：辞書
　　KW引数は、something = value となっているもの
"""
def menu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

menu('banana','apple','orange',**d)
