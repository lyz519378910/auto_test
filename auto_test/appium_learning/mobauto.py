import time
import re

from appium import webdriver
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction


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
    # 功能一：点击坐标按钮(tap)
    driver.tap([(450,900)])
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    print('width:{} height:{}'.format(width,height))
    time.sleep(5)
    # 功能二：滑动(TouchAction)
    action = TouchAction(driver)
    action.press(x=600,y=600).wait(1000).move_to(x=100,y=600).release().perform()
    time.sleep(5)
    action.press(x=600,y=600).wait(1000).move_to(x=100,y=600).release().perform()
    time.sleep(5)
    # 点击坐标按钮
    driver.tap([(400,850)])
    time.sleep(5)
    driver.tap([(550,650)])
    time.sleep(2)
    # 滑动
    action.press(x=360, y=1000).wait(1000).move_to(x=360, y=200).release().perform()
    time.sleep(5)
    action.press(x=360, y=200).wait(1000).move_to(x=360, y=1000).release().perform()
    time.sleep(5)

    driver.tap([(100, 800)])
    time.sleep(5)
    driver.tap([(100, 400)])
    time.sleep(5)
    driver.tap([(350, 350)])
    time.sleep(5)

    # 功能三：多点触控(MultiAction)
    action1 = TouchAction(driver)
    action2 = TouchAction(driver)
    action1.press(x=200,y=200).wait(2000).move_to(x=500,y=200).release()
    action2.press(x=200, y=200).wait(2000).move_to(x=200, y=500).release()
    multi = MultiAction(driver)
    multi.add(action1,action2)
    multi.perform()


    # 功能四：返回（4）
    driver.press_keycode(4)

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