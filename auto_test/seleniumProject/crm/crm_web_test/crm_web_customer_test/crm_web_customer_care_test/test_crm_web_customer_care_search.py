import time
import pytest


from auto_test.seleniumProject.crm.crm_base.usebrowser import UseBrowser
from auto_test.seleniumProject.crm.crm_web_func.crm_web_customer_func.crm_web_customer_care_func.crm_web_customer_care_search_func import CustomerCareSearch



class Test_CustomerCareSearch:

    def setup(self):
        self.ca = CustomerCareSearch()
        # self.tcca = Test_CustomerCareAdd()

    def test_customer_care_search_success(self):
        u"""查询正确"""
        self.ca.customer_care_search(self.ca.lp.ub.eo.get_cell(23, 2))
        self.ca.lp.lg.set_log('------获取查询信息------', 'info')
        self.ca.judge_search_correct(self.ca.lp.ub.eo.get_cell(23,4))
        self.ca.lp.lg.set_log('------查询成功------', 'info')
        # self.ca.lp.bo.alert_accept()

    def teardown(self):
        UseBrowser.quit()

if __name__ == '__main__':
    pytest.main(['-v', '-s','--reruns','1','--html=../../../crm_report/report.html'])
