import hashlib

import requests
import json

# header = {
#     'Host' : 'm.imooc.com',
#     'Connection ' : 'keep-alive',
#     'Pragma ' : 'no-cache',
#     'Cache-Control' : 'no-cache',
#     'Accept' : 'application/json,text/javascript，*/*;q=8.01',
#     'x-Requested-With' :'XMLHttpRequest',
#     'User-Agent' : 'Mozilla/5.0 (iPhone; CPU iPhone os 11_0 like Mac Os x)',
#     'Referer' :' https://m.imooc.com/',
#     'Accept-Language' : 'zh-CN,zh;q=0.9'
# }
#
# res = requests.get("https://m.imooc.com/api/search/searchword",headers=header).json()
#
# print(res)

password = "lyz"
md5 = hashlib.md5()
md5.update(password.encode('utf-8'))
res = md5.hexdigest()
print(res)


data = str({
    'user':'11111'
})
md5.update(data.encode('utf-8'))
res1 = md5.hexdigest()
print(res1)
