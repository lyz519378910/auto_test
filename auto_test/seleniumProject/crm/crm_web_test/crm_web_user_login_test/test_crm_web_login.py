import pytest

from auto_test.seleniumProject.crm.crm_base.browseroperation import BrowserOperation
from auto_test.seleniumProject.crm.crm_base.usebrowser import UseBrowser
from auto_test.seleniumProject.crm.crm_web_func.crm_web_user_func.crm_web_login_func import LoginPage


class Test_LoginPage:

    def setup(self):
        self.lp = LoginPage()
        self.bo = BrowserOperation(UseBrowser.driver)

    def test_1_login_null(self):
        u"""密码为空"""
        self.lp.login(self.lp.ub.eo.get_cell(4, 2), self.lp.ub.eo.get_cell(4, 3))
        self.lp.lg.set_log('------获取弹出框------', 'info')
        alert_text = self.lp.bo.alert_text()
        assert self.lp.ub.eo.get_cell(4, 4),alert_text
        self.lp.bo.alert_accept()

    # def test_2_login_coorect(self):
    #     u"""登录正确"""
    #     #传入登录参数，get_cell(1, 2)为Excel中的位置
    #     self.lp.login(self.lp.ub.eo.get_cell(1, 2),self.lp.ub.eo.get_cell(1, 3))
    #     self.lp.bo.login_correct(assert,self.lp.ub.eo.get_cell(1, 4),self.lp.lg.set_log('------登陆成功------', 'info'))

    def test_3_login_user_paswd_error(self):
        u"""用户或密码错误"""
        self.lp.login(self.lp.ub.eo.get_cell(2, 2),self.lp.ub.eo.get_cell(2, 3))
        #调用Login类中，实例化logg中AutoLog类的的函数
        self.lp.lg.set_log('------获取弹出框------', 'info')
        alert_text = self.lp.bo.alert_text()
        assert self.lp.ub.eo.get_cell(2, 4),alert_text
        #弹出框确认
        self.lp.bo.alert_accept()

    def teardown(self):
        UseBrowser.quit()

if __name__ == '__main__':
    pytest.main(['-v', '-s','--reruns','1','--html=../seleniumProject/crm/crm_report/report.html'])
