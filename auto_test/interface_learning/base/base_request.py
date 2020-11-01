import json

import requests


class RequestOperation:

    def request_result(self,method,url,data):
        '''执行方法，传递method，url，data参数'''
        if method == 'get':
            '''发送get请求'''
            res = requests.get(url=url, json=data).text
            print(json.dumps(res, indent=2, ensure_ascii=False))
        elif method == 'post':
            '''发送post请求'''
            res = requests.post(url=url, json=data).text
            print(json.dumps(res, indent=2, ensure_ascii=False))
        try:
            res = json.loads(res)
        except:
            print("这个结果是text")
        return res

    def judge_element(self,result,result_value,expect_value,code_status):
        if result.json()[result_value] == expect_value and result.status_code == code_status:
            print('success')
        else:
            print('failed')

    def show_request(self,json_res):
        print(json.dumps(json_res, indent=2, ensure_ascii=False))
