import time
import pytest


from auto_test.seleniumProject.crm.crm_base.usebrowser import UseBrowser
from auto_test.seleniumProject.crm.crm_web_func.crm_web_customer_func.crm_web_customer_care_func.crm_web_customer_care_add_func import CustomerCareAdd


class Test_CustomerCareAdd:

    def setup(self):
        self.ca = CustomerCareAdd()

    def test_customer_care_add_success(self):
        u"""关怀正确"""
        self.ca.customer_care_add(self.ca.lp.ub.eo.get_cell(20, 2), self.ca.lp.ub.eo.get_cell(20, 3))
        self.ca.lp.lg.set_log('------获取弹出框------', 'info')
        alert_text = self.ca.lp.bo.alert_text()
        assert self.ca.lp.ub.eo.get_cell(20,4), alert_text
        self.ca.lp.bo.alert_accept()

    def teardown(self):
        UseBrowser.quit()

if __name__ == '__main__':
    pytest.main(['-v', '-s','--reruns','1','--html=../../crm_report/report.html'])
