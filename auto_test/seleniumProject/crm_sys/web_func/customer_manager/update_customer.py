import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select

from auto_test.seleniumProject.crm_sys.config.myself_log import AutoLog

#1、复制时注意修改类名
from auto_test.seleniumProject.crm_sys.config.myself_yaml import YamlOperation


class Update:

    def __init__(self,url):
        # 实例化日志
        self.logg = AutoLog()
        #实例化 YamlOperation类，添加yaml文件
        self.yam = YamlOperation('D:\\Python\\auto_test\\seleniumProject\\crm_sys\\config\\test.yaml')
        self.driver = webdriver.Chrome('C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')
        self.driver.set_window_position(200, 100)
        self.driver.set_window_size(1280, 720)
        # self.driver.implicitly_wait(5)
        self.driver.get(url)

    # 2、复制时注意修改方法名
    def login(self,user,pas):
        self.logg.set_log('------登录功能开始------','info')

        username = self.driver.find_element_by_xpath(self.yam.get_locator('LoginPage','username'))
        username.send_keys(user)
        self.logg.set_log('------输入用户名------','info')
        password = self.driver.find_element_by_xpath(self.yam.get_locator('LoginPage','password'))
        password.send_keys(pas)
        self.logg.set_log('------输入密码------', 'info')
        self.driver.find_element_by_xpath('//*[@id="in1"]').click()
        self.logg.set_log('------登录------', 'info')

    def driver_quit(self):
        self.driver.quit()

    def alert_text(self):
        alert = Alert(self.driver)
        message=alert.text           #获取警告框的text消息
        return message

    def alert_accept(self):
        Alert(self.driver).accept()

    def login_correct(self):
        time.sleep(1)
        self.driver.switch_to.frame('topFrame')
        actions = ActionChains(self.driver)
        element = self.driver.find_element_by_xpath(self.yam.get_locator('LoginPage','customer'))

        actions.click(element).perform()  # perform()  执行的意思
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame('mainFrame')
        self.driver.find_element_by_xpath(self.yam.get_locator('LoginPage','customer_add')).click()

        # element1 = self.driver.find_element_by_link_text('添加')
        # actions.click(element1).perform()

    # 3、复制时注意修改方法名
    def update(self,user,mal,sour,adds):
        self.logg.set_log('------修改功能开始------','info')

        element = self.driver.find_element_by_name('customerForUser')
        select_element = Select(element)  # 选择方式选择
        select_element.select_by_visible_text(user)
        self.logg.set_log('------负责员工------','info')

        mail = self.driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[7]/td[2]/input')
        mail.send_keys(mal)
        self.logg.set_log('------客户邮箱------', 'info')

        element = self.driver.find_element_by_name('customerSource')
        select_element = Select(element)  # 选择方式选择
        select_element.select_by_value(sour)
        self.logg.set_log('------客户来源------', 'info')

        addres = self.driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[8]/td[2]/input')
        addres.send_keys(adds)
        self.logg.set_log('------客户添加人------', 'info')

        self.driver.find_element_by_name('submit').click()
        self.logg.set_log('------客户修改------', 'info')





