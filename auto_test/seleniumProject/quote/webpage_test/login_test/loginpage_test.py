import unittest

from auto_test.seleniumProject.quote.base.browseroperation import BrowserOperation
from auto_test.seleniumProject.quote.base.usebrowser import UseBrowser
from auto_test.seleniumProject.quote.webpage_func.user_manager.loginpage import LoginPage


class LoginPage_Test(unittest.TestCase):

    def setUp(self) -> None:
        self.lp = LoginPage()
        self.bo = BrowserOperation(UseBrowser.driver)

    def test_1_login_null(self):
        self.lp.login()
        self.assertEqual(self.bo.get_text('/html/body/table/tbody/tr[1]/td[2]/form/table/tbody/tr[5]/td'),'请勿非法登录！')

    def test_2_login_coorect(self):
        self.lp.login('admin','admin123')
        correct = self.lp.login_correct_text('main','/html/body/table/tbody/tr[1]/td/span')
        self.assertEqual(correct,'欢迎使用报价管理系统')


    def tearDown(self) -> None:
        UseBrowser.quit()

if __name__ == '__main__':
    unittest.main()
