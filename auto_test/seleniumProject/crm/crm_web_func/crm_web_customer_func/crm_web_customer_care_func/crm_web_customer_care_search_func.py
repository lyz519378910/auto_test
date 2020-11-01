import time
import re
from auto_test.seleniumProject.crm.crm_web_func.crm_web_user_func.crm_web_login_func import LoginPage


class CustomerCareSearch:

    def __init__(self):
        self.lp = LoginPage()
        self.lp.login(self.lp.ub.eo.get_cell(1, 2), self.lp.ub.eo.get_cell(1, 3))
        time.sleep(1)
        self.lp.bo.switch_frame('/html/frameset/frameset/frame[1]')
        self.lp.bo.click_element(self.lp.ub.yo.get_locator('CustomerCare', 'cc_click'))
        self.lp.bo.switch_frame('mainFrame')

    def customer_care_search(self,customerInput):
        self.lp.bo.send_key(self.lp.ub.yo.get_locator('CustomerCare', 'cc_customerInput'), customerInput)  # yaml文件
        self.lp.lg.set_log('------查询内容------', 'info')
        self.lp.bo.select_down_menu('queryType', 1)
        self.lp.lg.set_log('------查询方式------', 'info')
        self.lp.bo.click_element(self.lp.ub.yo.get_locator('CustomerCare', 'cc_search_click'))
        self.lp.lg.set_log('------查询------', 'info')

    def judge_search_correct(self,compare_param):

        text = self.lp.bo.judge_search(self.lp.ub.yo.get_locator('CustomerCare', 'cc_search_page'))
        res = re.search('\d',text).group()
        for i in range(2,int(res)+2):
            res = self.lp.bo.judge_search("/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr["+str(i)+"]/td[3]/div/span")
            assert compare_param,res


# if __name__ == '__main__':
#     ccs = CustomerCareSearch()
#     ccs.judge_search_correct()