"""
    ラムダ
"""
l = ['Mon','tue','wed','thu','Fri','sat','SUN']

def change_words(words, func):
    for word in words:
        print(func(word))

# 実行
change_words(l, lambda word:word.capitalize())
change_words(l, lambda word:word.lower())