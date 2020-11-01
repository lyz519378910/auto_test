import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert

from auto_test.seleniumProject.crm_sys.config.myself_log import AutoLog


class Login:

    def __init__(self,url):
        # 实例化日志
        self.logg = AutoLog()
        #实例化驱动
        self.driver = webdriver.Chrome('C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        #获取url
        self.driver.get(url)


    def login(self,user,pas):
        self.logg.set_log('------登录功能开始------','info')
        username = self.driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/input')
        username.send_keys(user)
        self.logg.set_log('------输入用户名------','info')
        password = self.driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/div/input')
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

    def alert_accept(self):          #确认警告
        Alert(self.driver).accept()

    #正确登录
    def login_correct(self,assertEqual,excel_param,flag):
        for v in self.driver.window_handles:
            self.driver.switch_to.window(v)
            assertEqual(excel_param, self.driver.title)
            flag
            break






