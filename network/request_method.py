import requests

payload = {'key1':'value1', 'key2':'value2'}

# 各メソッド
r_get = requests.get('http://httpbin.org/get', params=payload)
r_post = requests.post('http://httpbin.org/post', data=payload)
r_put = requests.put('http://httpbin.org/put', data=payload)
r_delete = requests.delete('http://httpbin.org/delete', params=payload)

# print(r.status_code)
# print(r.text)
print(r_get.json())
print(r_post.json())
print(r_put.json())
print(r_delete.json())