import json
import requests

#api路径
url = "http://127.0.0.1:5000/users"

parms = {
    'keyword': 'KFC', #发送给服务器的内容
    'lv': 'high'
}

headers = {
    'User-agent': 'none/ofyourbusiness',
    'Spam': 'Eggs',
    'Content-Type': 'application/json'
}


res = requests.post(url, data=json.dumps(parms), headers=headers) # 发送请求

text = res.text

print(text)
#print(json.loads(text))




