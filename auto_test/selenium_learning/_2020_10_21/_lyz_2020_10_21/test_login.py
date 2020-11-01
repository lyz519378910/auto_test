import time
import unittest
from HTMLTestRunner import HTMLTestRunner

from seleniumProject._2020_10_21._lyz_2020_10_21.add_case import Add_Case
from seleniumProject._2020_10_21._lyz_2020_10_21.update_case import Update_Case
from seleniumProject._2020_10_21._lyz_2020_10_21.login_case import Login_Case

class MyTestCase(unittest.TestCase):
    pass

if __name__ == '__main__':
    suite = unittest.TestSuite()
    add_case = unittest.TestLoader().loadTestsFromTestCase(Add_Case)
    up_case = unittest.TestLoader().loadTestsFromTestCase(Update_Case)
    login_case = unittest.TestLoader().loadTestsFromTestCase(Login_Case)

    lst = [login_case,add_case,up_case]                       #放在列表
    suite.addTests(lst)                       #addTests  多类添加
    # suite.addTest(add_case)
    # suite.addTest(up_case)

    date_now = time.strftime('%Y-%m-%d', time.localtime())  # 设置时间
    report_path = 'D:\\Python\\report_python'  # 报告位置
    report_name = report_path + "/" + 'report_' + date_now + '.html'  # 报告名称，将时间加入文件
    with open(report_name, 'wb+') as file:
        runner = HTMLTestRunner(stream=file, verbosity=1, title='auto_test', description='ui_auto_test')
        runner.run(suite)
