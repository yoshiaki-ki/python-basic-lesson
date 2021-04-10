"""
    リスト内包表記
"""
t = (1,2,3,4,5)
t2 = (5,6,7,8,9)

r = [i for i in t if i % 2 == 0]
print(r)

r2 = [i*j for i in t for j in t2]
print(r2)

"""
    辞書内包表記
"""
x = ['mon','tue','wed']
y = ['coffee','orange','water']

d = {x:y for x,y in zip(x,y)}
print(d)