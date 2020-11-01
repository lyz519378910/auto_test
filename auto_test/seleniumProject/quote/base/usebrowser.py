#浏览器封装
import time
from selenium import webdriver
import sys
sys.path.append('D:\\Python\\auto_test')

class UseBrowser:

    driver = None

    def __init__(self):
        self.driver = webdriver.Chrome('D:\\Python\\auto_test\\seleniumProject\\quote\\chromedriver.exe')
        self.driver.set_window_position(200, 100)
        self.driver.set_window_size(1280, 720)
        self.driver.implicitly_wait(5)
        UseBrowser.driver = self.driver



    #退出页面
    @classmethod
    def quit(cls):
        UseBrowser.driver.quit()
