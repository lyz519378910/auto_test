#浏览器封装
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys

from auto_test.seleniumProject.crm.crm_util.crm_db.crm_customer_db.crm_customer_db import CustomerOperation
from auto_test.seleniumProject.crm.crm_util.crm_excel import ExcelOperation
from auto_test.seleniumProject.crm.crm_util.crm_yaml import YamlOperation

sys.path.append('D:\\Python\\auto_test')

class UseBrowser:

    driver = None

    def __init__(self):
        # chrome_options = Options()
        # chrome_options.add_argument('--headless')   #无头启动
        # ##实例化 驱动
        # self.driver = webdriver.Chrome('D:\\Python\\auto_test\\seleniumProject\\crm\\chromedriver.exe',chrome_options=chrome_options)
        self.driver = webdriver.Chrome('D:\\Python\\auto_test\\seleniumProject\\crm\\chromedriver.exe')
        #实例化 yaml文件
        self.yo = YamlOperation('D:\\Python\\auto_test\\seleniumProject\\crm\\crm_config\\test.yaml')
        #实例化 xlsx文件
        self.eo = ExcelOperation('D:\\Python\\auto_test\\seleniumProject\\crm\\crm_config\\case.xlsx', '用例参数')
        #实例化 mysql
        self.co = CustomerOperation()

        self.driver.set_window_position(200, 100)
        self.driver.set_window_size(1280, 720)
        # self.driver.implicitly_wait(5)
        UseBrowser.driver = self.driver


    #退出页面
    @classmethod
    def quit(cls):
        UseBrowser.driver.quit()

