import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert

from auto_test.seleniumProject.crm_sys.config.myself_log import AutoLog


class Add:

    def __init__(self,url):
        self.logg = AutoLog()
        self.driver = webdriver.Chrome('C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')
        self.driver.set_window_position(200, 100)
        self.driver.set_window_size(1280, 720)
        # self.driver.implicitly_wait(20)
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

    def alert_accept(self):
        Alert(self.driver).accept()

    def login_correct(self):
        time.sleep(1)
        self.driver.switch_to.frame('topFrame')
        actions = ActionChains(self.driver)
        element = self.driver.find_element_by_xpath(
            '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td[5]/table/tbody/tr/td/div/a')

        actions.click(element).perform()  # perform()  执行的意思
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame('mainFrame')
        self.driver.find_element_by_xpath('/html/body/form/table/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[4]/input').click()

        # element1 = self.driver.find_element_by_link_text('添加')
        # actions.click(element1).perform()



    def add(self,user,mal,brth,adds):
        self.logg.set_log('------添加功能开始------','info')

        username = self.driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[2]/td[2]/input')
        username.send_keys(user)
        self.logg.set_log('------输入客户姓名------','info')

        mail = self.driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[4]/td[4]/input')
        mail.send_keys(mal)
        self.logg.set_log('------客户邮箱------', 'info')

        # js = "$('input[id = customerBirthday]').removeAttr('readonly')"
        # self.driver.execute_script(js)
        # self.driver.find_element_by_id('customerBirthday').send_keys(brth)

        self.driver.find_element_by_id('customerBirthday').click()
        self.driver.execute_script("document.getElementById('customerBirthday').readOnly=false")
        self.driver.find_element_by_id('customerBirthday').clear()
        self.driver.find_element_by_id('customerBirthday').send_keys(brth)
        # self.driver.execute_script("document.getElementById('customerBirthday').value = " + brth + " ")
        self.logg.set_log('------客户生日------', 'info')

        addres = self.driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[8]/td[2]/input')
        addres.send_keys(adds)
        self.logg.set_log('------客户添加人------', 'info')

        self.driver.find_element_by_name('submit').click()
        self.logg.set_log('------客户添加------', 'info')





