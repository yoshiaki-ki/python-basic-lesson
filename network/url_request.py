import urllib.request
import json

payload = {'key1':'value1', 'key2':'value2'}

# GET
# url = 'http://httpbin.org/get' + '?' + urllib.parse.urlencode(payload) #dictをurlパラメタの形式に変更
# with urllib.request.urlopen(url) as f:
#     print(f.read().decode('utf-8'))

# POST
payload = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(
    'http://httpbin.org/post',data=payload, method='POST'
)
with urllib.request.urlopen(req) as f:
    print(f.read().decode('utf-8'))