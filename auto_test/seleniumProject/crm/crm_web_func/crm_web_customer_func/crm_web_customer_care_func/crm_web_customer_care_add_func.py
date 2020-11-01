import time

from auto_test.seleniumProject.crm.crm_web_func.crm_web_user_func.crm_web_login_func import LoginPage


class CustomerCareAdd:

    def __init__(self):
        self.lp = LoginPage()
        self.lp.login(self.lp.ub.eo.get_cell(1, 2), self.lp.ub.eo.get_cell(1, 3))
        time.sleep(1)
        self.lp.bo.switch_frame('/html/frameset/frameset/frame[1]')
        self.lp.bo.click_element(self.lp.ub.yo.get_locator('CustomerCare', 'cc_click'))
        self.lp.bo.switch_frame('mainFrame')
        self.lp.bo.click_element(self.lp.ub.yo.get_locator('CustomerCare', 'cc_add'))

    def customer_care_add(self,careTheme,careNexttime):
        self.lp.ub.co.delete_customer_care()
        self.lp.bo.send_key(self.lp.ub.yo.get_locator('CustomerCare', 'cc_subject'), careTheme)  # yaml文件
        self.lp.lg.set_log('------关怀主题------', 'info')
        self.lp.bo.driver.execute_script("window.document.getElementById("+"'"+self.lp.ub.yo.get_locator('CustomerCare','cc_care_time')+"'"+").readOnly=false")
        self.lp.bo.driver.execute_script("window.document.getElementById("+"'"+self.lp.ub.yo.get_locator('CustomerCare','cc_care_time')+"'"+").value="+"'"+careNexttime+"'")
        self.lp.lg.set_log('------下次关怀时间------', 'info')
        self.lp.bo.click_element(self.lp.ub.yo.get_locator('CustomerCare', 'cc_submit'))
        self.lp.lg.set_log('------添加------', 'info')