import json
import re

import requests
import sys
import os

from deepdiff import DeepDiff
from openpyxl.styles import Font, colors

base_path = os.getcwd()
sys.path.append(base_path)

from auto_test.interfaceProject.a_quote.quote4_util.quote_excel import ExcelOperation




class RequestOperation:

    def __init__(self):
        self.eo = ExcelOperation('D:\\Git\\auto_test\\auto_test\\interfaceProject\\a_quote\\quote3_config\\quote.xlsx','用例参数')

    def request_value(self,interface_name):
        # 获取行数
        rows = self.eo.get_row()
        for i in range(1, rows):
            value = self.eo.get_row_data(i)
            # 判断是否执行此条case
            if value[1] == interface_name and value[2] == 'yes':
                self.judge_request_value(value)

    def judge_request_value(self,value):
        # 判断删除，因为删除用的是get，无body
        if value[1] == '删':
            res = self.request_result(value[3], value[4])
            self.judge_element(res, value[6], value[7])
        else:
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
            # 调用请求结果函数
            res = self.request_result(value[3], value[4], data)
            if value[1] == '查':
                self.judge_search_element(res, value[6], value[7])
            else:
                self.judge_element(res, value[6], value[7])

    '''执行方法，传递method，url，data参数'''
    def request_result(self,method,url,data=None):
        try:
            #检查url完整性
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

            res = json.loads(res)
        except:
            pass
        finally:
            return res

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
