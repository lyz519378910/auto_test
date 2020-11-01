#coding=utf-8
import requests
import json
from requests import cookies


#上传文件
url = 'https://www.imooc.com/user/postpic'

#下载
download_uel = 'href="//www.imooc.com/mobile/appdown"'
file = {
    "fileField":("test.jpg",open("D:/图片/test.jpg","rb"),"image/jpg"),
    "type":"1"
}

cookie = {
    "apsid":"A0NGQ4Njc1ZjZlM2NkMmUwNzQ1NDc1NDhjMzU4NTkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOTQwNzQzMwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1MTkzNzg5MTBAcXEuY29tAAAAAAAAAAAAAAAAAAAAAGZjN2FkNTY5OGI0MzE3YWFjMTdkZDA0ZTA2ODhhNjEycBmVX3AZlV8%3DMT"
}

#上传
res = requests.post(url,files=file,cookies = cookie).json()

#下载
res_down = requests.get(download_uel)
with open("mukewang.apk","wb") as f:
    f.write(res_down.content)


# print(res)
print(res_down)

# #Content-Disposition: form-data; name="fileField"; filename="983b2a34349b033b7d64284a14ce36d3d439bd47.jpg"
# Content-Type: image/jpeg	<file>
# Content-Disposition: form-data; name="type"	1

