import time
import unittest

from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select

from myself_fuction.myself_log import AutoLog
from myself_fuction.myself_seleniu import Seleniu_package
alog = AutoLog()

class Add_Case(unittest.TestCase):

    driver = None


    def driver_find_name(self, drv, name_param, value):
        try:
            drv.find_element_by_name(name_param).clear()
            drv.find_element_by_name(name_param).send_keys(value)
            alog.set_log('input:' + value, 'info')
        except Exception as e:
            alog.set_log(e.with_traceback, 'error')


    def setUp(self) -> None:
        spackage = Seleniu_package()
        self.driver = spackage.webdriver_Chrome('http://localhost:8080/crm')
        time.sleep(1)
        self.driver_find_name(self.driver, 'userNum', 'admin')
        self.driver_find_name(self.driver, 'userPw', '123456')
        self.driver.find_element_by_id('in1').click()
        # for v in cls.driver.window_handles:
        #     cls.driver.switch_to.window(v)
        #     cls.assertEqual('客户关系管理系统', cls.driver.title)
        self.driver.switch_to.frame('topFrame')
        actions = ActionChains(self.driver)
        element = self.driver.find_element_by_xpath(
            '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td[5]/table/tbody/tr/td/div/a')
        actions.click(element).perform()  # perform()  执行的意思
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame('mainFrame')
        self.driver.find_element_by_xpath(
            '/html/body/form/table/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[4]/input').click()

    def test_add_case1(self):  # case1
        self.driver_find_name(self.driver, 'customerName', 'admin')
        self.driver_find_name(self.driver, 'customerEmail', '123@qq.com')
        self.driver.execute_script("document.getElementById('customerBirthday').readOnly=false")
        self.driver.execute_script("document.getElementById('customerBirthday').value = '2020-10-31'")
        self.driver_find_name(self.driver, 'customerAddMan', 'admin')
        actions = ActionChains(self.driver)
        element = self.driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[4]/td[2]/input[2]')
        actions.click(element).perform()

        element = self.driver.find_element_by_name('customerSource')
        select_element = Select(element)            #选择方式选择
        select_element.select_by_value('3')
        self.driver.find_element_by_name('submit').click()
        alert = Alert(self.driver)
        self.assertEqual('客户添加成功',alert.text) # 获取警告框的text消息
        alert.accept()

    def test_add_case2(self):  # case2
        self.driver_find_name(self.driver, 'customerName', '')
        self.driver_find_name(self.driver, 'customerEmail', '1231@qq.com')
        self.driver.execute_script("document.getElementById('customerBirthday').readonly=false")
        self.driver.execute_script("document.getElementById('customerBirthday').value = '2020-10-30'")
        self.driver_find_name(self.driver, 'customerAddMan', 'admin1')
        self.driver.find_element_by_name('submit').click()
        alert = Alert(self.driver)
        self.assertEqual('- 客户姓名不能为空!\n', alert.text)  # 获取警告框的text消息
        alert.accept()

    def test_add_case3(self):  # case3
        self.driver_find_name(self.driver, 'customerName', 'lyz')
        self.driver_find_name(self.driver, 'customerEmail', 'com')
        self.driver.execute_script("document.getElementById('customerBirthday').readOnly=false")
        self.driver.execute_script("document.getElementById('customerBirthday').value = '2020-10-30'")
        self.driver_find_name(self.driver, 'customerAddMan', 'admin1')
        self.driver.find_element_by_name('submit').click()
        alert = Alert(self.driver)
        self.assertEqual('- Email格式不对!\n', alert.text)  # 获取警告框的text消息
        alert.accept()

    def test_add_case4(self):  # case4
        self.driver_find_name(self.driver, 'customerName', 'lyz')
        self.driver_find_name(self.driver, 'customerEmail', '123@qq.com')
        self.driver.execute_script("document.getElementById('customerBirthday').readOnly=false")
        self.driver.execute_script("document.getElementById('customerBirthday').value = '2020-10-30'")
        self.driver_find_name(self.driver, 'customerAddMan', '')
        self.driver.find_element_by_name('submit').click()
        alert = Alert(self.driver)
        self.assertEqual('- 创建人不能为空!\n', alert.text)  # 获取警告框的text消息
        alert.accept()


    def tearDown(self) -> None:
        self.driver.quit()
        print('test add over')