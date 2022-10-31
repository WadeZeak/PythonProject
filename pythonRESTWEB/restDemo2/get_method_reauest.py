import json
import requests

#api路径
url = "http://127.0.0.1:30880/products"

headers = {
    'User-agent': 'none/ofyourbusiness',
    'Spam': 'Eggs',
    'Content-Type': 'application/json'
}


res = requests.get(url, headers=headers) # 发送请求

text = res.text

print(text)