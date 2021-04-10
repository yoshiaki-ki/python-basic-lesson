"""
    ジェネレイター
"""
def greeting():
    yield 'Goog morning'
    yield 'Good afternoon'
    yield 'Good night'


g = greeting()

print(next(g))
print(next(g))
print(next(g))