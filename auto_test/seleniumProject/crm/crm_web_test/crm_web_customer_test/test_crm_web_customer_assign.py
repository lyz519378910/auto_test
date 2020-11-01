import time
import pytest


from auto_test.seleniumProject.crm.crm_base.usebrowser import UseBrowser
from auto_test.seleniumProject.crm.crm_web_func.crm_web_customer_func.crm_web_customer_assign_func import CustomerAssign


class Test_CustomerAssign:

    def setup(self):
        self.ca = CustomerAssign()

    def test_customer_assigon_success(self):
        u"""分配客户正确"""
        self.ca.customer_assigon()
        self.ca.lp.lg.set_log('------获取弹出框------', 'info')
        alert_text = self.ca.lp.bo.alert_text()
        assert self.ca.lp.ub.eo.get_cell(17,2), alert_text
        self.ca.lp.bo.alert_accept()

    def teardown(self):
        UseBrowser.quit()

# if __name__ == '__main__':
#     pytest.main(['-v', '-s','--reruns','1','--html=../crm/crm_report/report.html'])
