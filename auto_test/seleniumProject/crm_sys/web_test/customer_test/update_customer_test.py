import time
import unittest
from HTMLTestRunner import HTMLTestRunner
import sys
sys.path.append('D:\\Python')
from auto_test.seleniumProject.crm_sys.config.myself_log import AutoLog

#1、复制时注意修改包
from auto_test.seleniumProject.crm_sys.web_func.customer_manager.update_customer import Update

from auto_test.seleniumProject.crm_sys.config.myself_excel import OperationExcel

class TestAdd(unittest.TestCase):

    def setUp(self) -> None:

        self.logger = AutoLog()
        self.op = OperationExcel('D:\\Python\\auto_test\\seleniumProject\\crm_sys\\config\\case.xlsx','用例参数')

        # 2、复制时注意修改名称
        self.add = Update(self.op.get_cell(1, 1))
        self.add.login(self.op.get_cell(1, 2), self.op.get_cell(1, 3))
        self.logger.set_log('------登陆成功------', 'info')
        self.add.login_correct()


    def test_update_correct(self):

        # 3、复制时注意修改方法
        self.add.update(self.op.get_cell(14, 2),self.op.get_cell(14, 3),self.op.get_cell(14, 4),self.op.get_cell(14, 5))
        self.logger.set_log('------获取弹出框------', 'info')
        alert_text = self.add.alert_text()
        self.assertEqual(self.op.get_cell(14, 6), alert_text)
        self.add.alert_accept()

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