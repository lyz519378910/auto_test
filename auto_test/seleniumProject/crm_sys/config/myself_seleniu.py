from selenium import webdriver

class Seleniu_package:

    #chrome网页驱动位置
    def webdriver_Chrome(self,http):
        driver = webdriver.Chrome('C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')
        driver.get(http)
        driver.set_window_position(200, 100)
        driver.set_window_size(1280, 720)
        return driver

    #切换窗体(驱动名称,目标页面名称)
    def chang_window(self,driver_param,aim_param):
        for v in driver_param.window_handles:
            driver_param.switch_to.window(v)
            if driver_param.title == aim_param:
                print('pass')
                break
