"""
    例外処理
"""

l = [1,2,3]
i = 5
try:
    l[1] # 成功する
except IndexError as e:
    print("ERROR:{}".format(e))
else:
    print('DONE')
finally:
    print('clean up')