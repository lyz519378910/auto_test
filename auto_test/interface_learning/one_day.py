import requests
import json

from interface_learning.base.base_request import BaseRequest



# br = BaseRequest()
#
# url = 'http://localhost:8080/InterfaceProject/login'
# data = {
#     "username": "lyz1",
#     "password": "Lyz*123"
# }
# res = br.run_main('post',url,data)
# br.show_request(res)





# res = requests.post(url,json=data)
# json_res = res.json()
# print(json.dumps(json_res,indent=2,ensure_ascii=False))

# url = 'http://localhost:8080/InterfaceProject/adduser'
# data = {
#     "username":"lyz1",
#     "password":"Lyz*123",
#     "grade":"3"
# }
# res = requests.post(url,json=data)
# json_res = res.json()
# print(json.dumps(json_res,indent=2,ensure_ascii=False))



class Login:

    def url_data(self,url,username,password):
        # url = 'http://localhost:8080/InterfaceProject/login'
        data = {
            "username": username,
            "password": password
        }
        return requests.post(url, json=data)


    def interface_login(self,url,username,password,expect_value):
        res = self.url_data(url,username,password)
        print(res.json())
        if res.json()['message']==expect_value and res.status_code==200:
            print('success')
        else:
            print('failed')

if __name__ == '__main__':
    login = Login()
    login.interface_login('http://localhost:8080/InterfaceProject/login','lyz1','Lyz*123','用户名不能为空')
