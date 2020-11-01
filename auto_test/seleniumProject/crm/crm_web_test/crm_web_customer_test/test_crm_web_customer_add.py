import pytest


from auto_test.seleniumProject.crm.crm_base.usebrowser import UseBrowser
from auto_test.seleniumProject.crm.crm_web_func.crm_web_customer_func.crm_web_customer_add_func import CustomerAdd


class Test_CustomerAdd:

    def setup(self):
        self.ca = CustomerAdd()

    def test_1_add_coorect(self):
        u"""添加客户正确"""
        # 传入登录参数，get_cell(1, 2)为Excel中的位置
        self.ca.customer_add(self.ca.lp.ub.eo.get_cell(8, 2), self.ca.lp.ub.eo.get_cell(8, 3),
                             self.ca.lp.ub.eo.get_cell(8, 4), self.ca.lp.ub.eo.get_cell(8, 5))
        self.ca.lp.lg.set_log('------获取弹出框------', 'info')
        alert_text = self.ca.lp.bo.alert_text()
        #第一次页面判断添加成功
        assert self.ca.lp.ub.eo.get_cell(8,6), alert_text
        self.ca.lp.bo.alert_accept()
        #第二次数据库判断添加成功
        assert '节日',self.ca.lp.ub.co.judge_customer_care_add_correct()
        self.ca.lp.lg.set_log('------添加成功------', 'info')

    def teardown(self):
        UseBrowser.quit()

if __name__ == '__main__':
    pytest.main(['-v', '-s','--reruns','1','--html=../../../crm_report/report.html'])
