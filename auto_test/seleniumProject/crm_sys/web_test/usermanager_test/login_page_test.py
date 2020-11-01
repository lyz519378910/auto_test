import time
import unittest
from HTMLTestRunner import HTMLTestRunner
import sys
sys.path.append('D:\\Python')
from auto_test.seleniumProject.crm_sys.config.myself_log import AutoLog
from auto_test.seleniumProject.crm_sys.web_func.usermanager_func.login_page import Login
from auto_test.seleniumProject.crm_sys.config.myself_excel import OperationExcel

class TestLogin(unittest.TestCase):

    def setUp(self) -> None:

        #传入Excel地址，及用例参数sheet名称
        self.op = OperationExcel('D:\\Python\\auto_test\\seleniumProject\\crm_sys\\config\\case.xlsx','用例参数')
        #传入url，get_cell(1, 1)为Excel中的位置
        self.login = Login(self.op.get_cell(1, 1))

    def test_login_correct(self):
        u"""登录正确"""
        #传入登录参数，get_cell(1, 2)为Excel中的位置
        self.login.login(self.op.get_cell(1, 2),self.op.get_cell(1, 3))
        self.login.login_correct(self.assertEqual,self.op.get_cell(1, 4),self.login.logg.set_log('------登陆成功------', 'info'))

    def test_login_user_paswd_error(self):
        u"""用户或密码错误"""
        self.login.login(self.op.get_cell(2, 2),self.op.get_cell(2, 3))
        #调用Login类中，实例化logg中AutoLog类的的函数
        self.login.logg.set_log('------获取弹出框------', 'info')
        alert_text = self.login.alert_text()
        self.assertEqual(self.op.get_cell(2, 4),alert_text)
        #弹出框确认
        self.login.alert_accept()

    def test_login_user_paswd_null(self):
        u"""用户密码为空"""
        self.login.login(self.op.get_cell(3, 2),self.op.get_cell(3, 3))
        self.login.logg.set_log('------获取弹出框------', 'info')
        alert_text = self.login.alert_text()
        self.assertEqual(self.op.get_cell(3, 4),alert_text)
        self.login.alert_accept()

    def test_login_paswd_null(self):
        u"""密码为空"""
        self.login.login(self.op.get_cell(4, 2),self.op.get_cell(4, 3))
        self.login.logg.set_log('------获取弹出框------', 'info')
        alert_text = self.login.alert_text()
        self.assertEqual(self.op.get_cell(4, 4),alert_text)
        self.login.alert_accept()

    def test_login_username_null(self):
        u"""用户为空"""
        self.login.login(self.op.get_cell(5, 2),self.op.get_cell(5, 3))
        self.login.logg.set_log('------获取弹出框------', 'info')
        alert_text = self.login.alert_text()
        self.assertEqual(self.op.get_cell(5, 4),alert_text)
        self.login.alert_accept()

    # def test_login_correct(self):
    #     pass

    def tearDown(self) -> None:
        self.login.driver_quit()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    login_case = unittest.TestLoader().loadTestsFromTestCase(TestLogin)

    suite.addTest(login_case)
    date_now = time.strftime('%Y-%m-%d', time.localtime())  # 设置时间
    report_path = 'D:\\Python\\auto_test\\seleniumProject\\crm_sys\\report'  # 报告位置
    report_name = report_path + "/" + 'report_crm_' + date_now + '.html'       # 报告名称，将时间加入文件
    with open(report_name, 'wb+') as file:
        runner = HTMLTestRunner(stream=file, verbosity=1, title='auto_test', description='ui_auto_test')
        runner.run(suite)