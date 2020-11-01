import unittest

from selenium.webdriver.common.alert import Alert
from myself_fuction.myself_log import AutoLog
from myself_fuction.myself_seleniu import Seleniu_package
alog = AutoLog()

# def user_paswd(drv,user,paswd):                             #定义用户名、密码
#     try:
#         drv.find_element_by_name('userNum').clear()
#         drv.find_element_by_name('userNum').send_keys(user)
#         drv.find_element_by_name('userPw').clear()
#         drv.find_element_by_name('userPw').send_keys(paswd)
#         drv.find_element_by_id('in1').click()
#         alog.set_log('')
#     except Exception as e:
#
#         alog.set_log(user+paswd+'输入错误！','error')


class Login_Case(unittest.TestCase):

    driver = None

    def driver_find_name(self,drv,name_param,value):
        try:
            drv.find_element_by_name(name_param).clear()
            drv.find_element_by_name(name_param).send_keys(value)
            alog.set_log('input:'+value,'info')
        except Exception as e:
            alog.set_log(e.with_traceback,'error')

    def setUp(self) -> None:                          #开始
        spackage = Seleniu_package()
        self.driver = spackage.webdriver_Chrome('http://localhost:8080/crm')

    def test_login_case1(self):                           #case1
        self.driver_find_name(self.driver,'userNum','1')
        self.driver_find_name(self.driver, 'userPw', '1')
        self.driver.find_element_by_id('in1').click()
        self.assertEqual('用户或密码错误！请重新输入！',Alert(self.driver).text)
        Alert(self.driver).accept()
        print('test_login_case1 pass')

    def test_login_case2(self):                            #case2
        self.driver_find_name(self.driver, 'userNum', '')
        self.driver_find_name(self.driver, 'userPw', '')
        self.driver.find_element_by_id('in1').click()
        # if Alert(driver).text == '- 用户名不能为空!                                       - 密码不能为空!':
        Alert(self.driver).accept()
        print('test_login_case2 pass')

    def test_login_case3(self):                             #case3
        self.driver_find_name(self.driver, 'userNum', '1')
        self.driver_find_name(self.driver, 'userPw', '')
        self.driver.find_element_by_id('in1').click()
        self.assertEqual('- 密码不能为空!\n', Alert(self.driver).text)
        Alert(self.driver).accept()
        print('test_login_case3 pass')

    def test_login_case4(self):                             #case4
        self.driver_find_name(self.driver, 'userNu', '')
        self.driver_find_name(self.driver, 'userPw', '1')
        self.driver.find_element_by_id('in1').click()
        self.assertEqual('- 用户名不能为空!\n', Alert(self.driver).text)
        Alert(self.driver).accept()
        print('test_login_case4 pass')

    def test_login_case5(self):                             #case5
        self.driver_find_name(self.driver, 'userNum', 'admin')
        self.driver_find_name(self.driver, 'userPw', '123456')
        self.driver.find_element_by_id('in1').click()
        for v in self.driver.window_handles:
            self.driver.switch_to.window(v)
            self.assertEqual('客户关系管理系统', self.driver.title)
            print('test_login_case5 pass')
            break

    def tearDown(self) -> None:
        self.driver.quit()
        print('test over')



