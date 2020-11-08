import json
import re

import requests
import sys
import os

from deepdiff import DeepDiff
from openpyxl.styles import Font, colors
from requests import utils

base_path = os.getcwd()
sys.path.append(base_path)

from auto_test.interfaceProject.a_quote.quote4_util.quote_excel import ExcelOperation




class RequestOperation:

    def __init__(self):
        self.eo = ExcelOperation('D:\\Git\\auto_test\\auto_test\\interfaceProject\\a_quote\\quote3_config\\quote.xlsx','用例参数')

    #获取Excel中的值
    def get_excel_value(self,value):
        # 获取列数
        cols = self.eo.get_col()
        data = {}
        # 从下表为8开始找
        for v in range(8, cols):
            if value[v] == '':
                break
            else:
                value1 = re.search('(.+):', value[v]).group().replace(':', '')
                value2 = re.search(':(.+)', value[v]).group().replace(':', '')
                data.setdefault(value1, value2)
        return data
        # 调用请求结果函数
        # res = self.request_result(value[3], value[4], data)

    #判断请求值，一个是增删改查，一个是登录
    def judge_request_value(self,value,login_value):
        data = self.get_excel_value(login_value)
        #返回cookies，定义为heade
        heade = self.get_cookies(login_value[3], login_value[4], data)
        # 判断删除，因为删除用的是get，无body
        if value[1] == '删':
            res = self.request_result(value[3], value[4],None,heade)
            self.judge_element(res, value[6], value[7])
        else:
            if value[1] == '查':
                res = self.request_result(value[3], value[4], data, heade)
                self.judge_search_element(res, value[6], value[7])
            else:
                res = self.request_result(value[3], value[4], data, heade)
                self.judge_element(res, value[6], value[7])

    '''执行方法，传递method，url，data参数'''
    def request_result(self,method,url,data=None,heade=None):
        try:
            #检查url完整性
            if 'http://' not in url:
                url = 'http://' + url
            if method == 'get':
                '''发送get请求'''
                res = requests.get(url=url, json=data, header=heade)
                print(json.dumps(res.json(), indent=2, ensure_ascii=False))
            elif method == 'post':
                '''发送post请求'''
                res = requests.post(url=url, json=data, header=heade)
                print(json.dumps(res.json(), indent=2, ensure_ascii=False))
            res = json.loads(res)
        except:
            pass
        finally:
            return res

    #获取cookies
    def get_cookies(self,method,url,data):
        # 检查url完整性
        if 'http://' not in url:
            url = 'http://' + url
        if method == 'get':
            '''发送get请求'''
            res = requests.get(url=url, json=data)
            print(json.dumps(res.json(), indent=2, ensure_ascii=False))
        elif method == 'post':
            '''发送post请求'''
            res = requests.post(url=url, json=data)
            print(json.dumps(res.json(), indent=2, ensure_ascii=False))
        try:
            res = json.loads(res)
        except:
            pass
        finally:
            return requests.utils.dict_from_cookiejar(res.cookies)

    #请求数据
    def request_value(self,interface_name):
        # 获取行数
        rows = self.eo.get_row()
        #直接提取登陆成功的行，为获取cookie做准备
        login_value = self.eo.get_row_data(1)
        for i in range(1, rows):
            #获取一行的值
            value = self.eo.get_row_data(i)
            # 判断是否执行此条case
            if value[1] == interface_name and value[2] == 'yes':
                self.judge_request_value(value,login_value)



    #判断返回值是否是自己需要的
    def judge_element(self,result,code_status,expect_value):
        if result.json()['message'] == expect_value and result.status_code == int(code_status):
            print('success\n')
        else:
            print('failed\n')


    #查找要特殊点，因为涉及到遍历
    def judge_search_element(self,result,code_status,expect_value):
        for i in range(len(result.json())):
            if result.json()[i]['message'] == expect_value and result.status_code == int(code_status):
                print('success\n')
                break
        else:
            print('failed\n')

    #判断两个字典是否相同
    def compare_dict(self,dict1_param, dict2_param):
        cmp_dict = DeepDiff(dict1_param, dict2_param, ignore_order=True).to_dict()
        if cmp_dict.get('dictionary_item_added'):
            print("not equal")
        else:
            print('equal')



# if __name__ == '__main__':
#     data = {
#         "username": 'username',
#         "password": 'password',
#         "grade": 'grade'
#     }
#
#     res = RequestOperation()
#     res1 = res.request_result('post','http://localhost:8080/InterfaceProject/adduser',data)
#     res.judge(res1)
