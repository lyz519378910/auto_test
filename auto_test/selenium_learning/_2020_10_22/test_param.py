import time
import unittest
from HTMLTestRunner import HTMLTestRunner

import sys
sys.path.append('/')

from ddt import ddt, data, unpack, file_data


@ddt  #数据驱动
class MyTestCase(unittest.TestCase):
    pass
    #例1
    # @data(['1','1'],['a','1'])     #装测试数据
    # @unpack
    # def test_1_case(self,v):
    #     username = v[0]
    #     password = v[1]
    #     print(username,password)

    #例2
    # @data(['1','1'],['a','1'])     #装测试数据
    # @unpack                        #解包
    # def test_1_case(self,username,password):
    #     print('username:{},password:{}'.format(username,password))

    #例3                              #读取json文件
    @file_data('login_data.json')
    def test_1_case(self,**data):
        print(data['username'],data['password'],data['flag'])

    #例4                              #读取yaml文件
    # @file_data('login_data.yaml')
    # def test_1_case(self, **udata):
    #     print(udata['username'], udata['password'])
    #     # print(udata)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    test_case = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    # lst = [login_case,]                       #放在列表
    # suite.addTests(lst)                       #addTests  多类添加
    suite.addTest(test_case)

    date_now = time.strftime('%Y-%m-%d', time.localtime())              #设置时间
    report_path = 'D:\\Python\\report_python'                           #报告位置
    report_name = report_path + "/" + 'report_' + date_now + '.html'    #报告名称，将时间加入文件
    with open(report_name,'wb+') as file:
        runner = HTMLTestRunner(stream=file, verbosity=1, title='auto_test',description='ui_auto_test')
        runner.run(suite)

