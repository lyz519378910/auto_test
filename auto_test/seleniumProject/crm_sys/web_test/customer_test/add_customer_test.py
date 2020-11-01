import time
import unittest
from HTMLTestRunner import HTMLTestRunner
import sys
sys.path.append('D:\\Python')
from auto_test.seleniumProject.crm_sys.config.myself_log import AutoLog
from auto_test.seleniumProject.crm_sys.web_func.customer_manager.add_customer import Add
from auto_test.seleniumProject.crm_sys.config.myself_excel import OperationExcel

class TestAdd(unittest.TestCase):

    def setUp(self) -> None:

        self.logger = AutoLog()
        self.op = OperationExcel('D:\\Python\\auto_test\\seleniumProject\\crm_sys\\config\\case.xlsx','用例参数')
        self.add = Add(self.op.get_cell(1, 1))
        self.add.login(self.op.get_cell(1, 2), self.op.get_cell(1, 3))
        self.logger.set_log('------登陆成功------', 'info')
        self.add.login_correct()


    def test_add_correct(self):

        self.add.add(self.op.get_cell(8, 2),self.op.get_cell(8, 3),self.op.get_cell(8, 4),self.op.get_cell(8, 5))
        self.logger.set_log('------获取弹出框------', 'info')
        alert_text = self.add.alert_text()
        self.assertEqual(self.op.get_cell(8, 6),alert_text)
        self.add.alert_accept()
    #
    def test_add_user_null(self):
        self.add.add(self.op.get_cell(9, 2),self.op.get_cell(9, 3),self.op.get_cell(9, 4),self.op.get_cell(9, 5))
        self.logger.set_log('------获取弹出框------', 'info')
        alert_text = self.add.alert_text()
        self.assertEqual(self.op.get_cell(9, 6),alert_text)
        self.add.alert_accept()

    def test_add_email_error(self):
        self.add.add(self.op.get_cell(10, 2), self.op.get_cell(10, 3), self.op.get_cell(10, 4), self.op.get_cell(10, 5))
        self.logger.set_log('------获取弹出框------', 'info')
        alert_text = self.add.alert_text()
        self.assertEqual(self.op.get_cell(10, 6), alert_text)
        self.add.alert_accept()

    def test_add_creat_person_null(self):
        self.add.add(self.op.get_cell(11, 2), self.op.get_cell(11, 3), self.op.get_cell(11, 4), self.op.get_cell(11, 5))
        self.logger.set_log('------获取弹出框------', 'info')
        alert_text = self.add.alert_text()
        self.assertEqual(self.op.get_cell(11, 6), alert_text)
        self.add.alert_accept()
    #


    # def test_add_correct(self):
    #     pass

    def tearDown(self) -> None:
        self.add.driver_quit()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    add_case = unittest.TestLoader().loadTestsFromTestCase(TestAdd)

    suite.addTest(add_case)
    date_now = time.strftime('%Y-%m-%d', time.localtime())  # 设置时间
    report_path = 'D:\\Python\\auto_test\\seleniumProject\\crm_sys\\report'  # 报告位置
    report_name = report_path + "/" + 'report_crm_' + date_now + '.html'       # 报告名称，将时间加入文件
    with open(report_name, 'wb+') as file:
        runner = HTMLTestRunner(stream=file, verbosity=1, title='auto_test', description='ui_auto_test')
        runner.run(suite)