import time
import unittest
from HTMLTestRunner import HTMLTestRunner
import sys
sys.path.append('D:\\Python\\')
from auto_test.seleniumProject.crm.crm_web_test.crm_web_customer_test.crm_web_customer_add_test import CustomerAdd_test
from auto_test.seleniumProject.crm.crm_web_test.crm_web_user_login_test.crm_web_login_test import LoginPage_Test

if __name__ == '__main__':
    suite = unittest.TestSuite()
    CustomerAdd = unittest.TestLoader().loadTestsFromTestCase(CustomerAdd_test)
    LoginPage = unittest.TestLoader().loadTestsFromTestCase(LoginPage_Test)

    test_list = [CustomerAdd,LoginPage]
    suite.addTests(test_list)

    # date_now = time.strftime('%Y-%m-%d', time.localtime())  # 设置时间
    report_path = 'D:\\Python\\auto_test\\seleniumProject\\crm\\crm_report'  # 报告位置
    report_name = report_path + "/" + 'report_crm_new_test.html'       # 报告名称，将时间加入文件
    with open(report_name, 'wb+') as file:
        runner = HTMLTestRunner(stream=file, verbosity=1, title='auto_test', description='ui_auto_test')
        runner.run(suite)