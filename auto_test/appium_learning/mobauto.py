import time
import re

from appium import webdriver


def login():
    name = driver.find_element_by_xpath("//android.widget.EditText[@index='2']")
    name.click()
    name.send_keys('sa')
    paswd = driver.find_element_by_id('com.example.CangKuGuanLiXiTong12345:id/PasswordET')
    paswd.click()
    paswd.send_keys('sa')
    driver.find_element_by_xpath("//android.widget.Button[@text='登  录']").click()
    exitt = driver.find_element_by_id('android:id/button1').text
    if exitt == '以后再说':
        driver.find_element_by_id('android:id/button1').click()
        print('pass')

def register():
    reg = driver.find_element_by_id("com.example.CangKuGuanLiXiTong12345:id/Button01")
    reg.click()
    time.sleep(2)
    reg = driver.find_element_by_id("com.example.CangKuGuanLiXiTong12345:id/NameET")
    reg.click()
    reg.send_keys('lyz')
    time.sleep(2)
    reg = driver.find_element_by_id("com.example.CangKuGuanLiXiTong12345:id/PasswordET")
    reg.click()
    reg.send_keys('lyz123')
    time.sleep(2)
    reg = driver.find_element_by_id("com.example.CangKuGuanLiXiTong12345:id/ConfirmPasswordET")
    reg.click()
    reg.send_keys('lyz123')
    time.sleep(2)
    reg = driver.find_element_by_id("com.example.CangKuGuanLiXiTong12345:id/button1")
    reg.click()

def xmyx():
    # 点击坐标按钮
    driver.tap([(700,1300)])
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    print('width:{} height:{}'.format(width,height))
    time.sleep(2)
    # 滑动
    driver.swipe(start_x=678,start_y=500,end_x=123,end_y=500)
    time.sleep(2)
    driver.swipe(start_x=678, start_y=500, end_x=123, end_y=500)
    time.sleep(2)
    # 点击坐标按钮
    driver.tap([(400,850)])
    # driver.find_element_by_xpath("//android.widget.TextView[@text='我是男生']").click()
    # time.sleep(2)
    # driver.swipe(start_x=360, start_y=1000, end_x=360, end_y=200)
    # time.sleep(2)
    # driver.swipe(start_x=360, start_y=200, end_x=360, end_y=1000)
    # time.sleep(2)
    # driver.tap(([400, 850]))

if __name__ == '__main__':


    cap = {}

    cap['platformName'] = 'Android'

    # 自己的adb devices
    cap['deviceName'] = '127.0.0.1:21503'
    # app位置

    cap['app'] = 'D:\\Git\\auto_test\\Appium_Test\\xmyx.apk'

    # cap['appPackage'] = 'com.example.CangKuGuanLiXiTong12345'  # 获取包名
    # cap['appActivity'] = 'com.example.CangKuGuanLiXiTong12345.MainActivity'  # 获取activity启动

    # #非首次操作
    # cap['noReset'] = 'true'

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=cap)
    print(6666)
    xmyx()
    # login()
    # register()