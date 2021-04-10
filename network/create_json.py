import json

j = {
    "employee":
        [
            {"id":111, "name":"Mike"},
            {"id":222, "name":"Nancy"},
        ]
}

print(j)
print("#########")
print(json.dumps(j))  #　jsonは必ずダブルクオート（”）で値を囲むこと

# jsonファイルへの書き込み
with open('test.json', 'w') as f:
    json.dump(j,f)

# jsonファイルの読み込み
with open('test.json', 'r') as f:
    print(json.load(f))