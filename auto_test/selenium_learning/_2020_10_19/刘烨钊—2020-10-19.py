from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re

class Jd:

    def username_format_error(self):
        rese = driver.find_element_by_id('userName')
        rese.send_keys('_o7Y<')
        gar = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/i').value_of_css_property('background')
        print(re.search('error.png',gar).group())
        path = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/span').text
        if path == '格式错误，仅支持汉字、字母、数字、“-”“_”的组合':
            print('pass')
        else:
            print('failed')
        # print(rese.get_attribute('placeholder'))

    def username_null_error(self):
        rese = driver.find_element_by_id('userName')
        rese.send_keys(Keys.ENTER)
        gar = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/i').value_of_css_property(
            'background')
        print(re.search('error.png', gar).group())
        path = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/span').text
        if path == '用户名不能为空':
            print('pass')
        else:
            print('failed')

    def username_click_tip(self):
        rese = driver.find_element_by_id('userName')
        rese.click()
        gar = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/i').value_of_css_property('background')
        print(re.search('default.png', gar).group())
        path = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/span').text
        if path == '支持汉字、字母、数字、“-”“_”的组合，4-20个字符':
            print('pass')
        else:
            print('failed')

    def username_placeholder(self):
        placeholder = driver.find_element_by_id('userName').get_attribute('placeholder')
        # rese.click()
        # gar = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/i').value_of_css_property('background')
        # print(re.search('default.png', gar).group())
        # path = driver.find_element_by_xpath('//*[@id="userName"]').text
        if placeholder == '您的账户名和登录名':
            print('pass')
        else:
            print('failed')

    def username_correct(self):
        rese = driver.find_element_by_id('userName')
        rese.send_keys('疯狂力量药水')
        gar = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/i').value_of_css_property('background')
        print('pass',re.search('right.png', gar).group())

    def password_null_error(self):
        rese = driver.find_element_by_id('pwd')
        rese.send_keys(Keys.ENTER)
        gar = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/i').value_of_css_property('background')
        print(re.search('error.png', gar))
        path = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/span').text
        if path == '密码不能为空':
            print('pass')
        else:
            print('failed')

    def password_format_error(self):
        rese = driver.find_element_by_id('pwd')
        rese.send_keys('12')
        gar = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/i').value_of_css_property('background')
        print(re.search('error.png',gar).group())
        path = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/span').text
        if path == '密码长度应在6-20个字符之间':
            print('pass')
        else:
            print('failed')

    def password_format_tip(self):
        rese = driver.find_element_by_id('pwd')
        rese.send_keys('1234567')
        gar = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/i').value_of_css_property('background')
        print('pass',re.search('ruo.png',gar))

    def password_placeholder(self):
        placeholder = driver.find_element_by_id('pwd').get_attribute('placeholder')
        if placeholder == '建议至少两种字符组合':
            print('pass')
        else:
            print('failed')

    def password_correct(self):
        rese = driver.find_element_by_id('pwd')
        rese.send_keys('疯狂力量药水')
        gar = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/i').value_of_css_property('background')
        print('pass',re.search('right.png', gar).group())

    def password_confirm_format_error(self):
        rese = driver.find_element_by_id('pwd')
        rese.send_keys('疯狂力量药水')
        rese2 = driver.find_element_by_id('pwd2')
        rese2.send_keys('12')
        gar = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div[2]/i').value_of_css_property('background')
        print(re.search('error.png',gar).group())
        path = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div[2]/span').text
        if path == '两次密码不一致':
            print('pass')
        else:
            print('failed')

    def password_confirm_format_correct(self):
        rese = driver.find_element_by_id('pwd')
        rese.send_keys('疯狂力量药水')
        rese2 = driver.find_element_by_id('pwd2')
        rese2.send_keys('疯狂力量药水')
        gar = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div[1]/i').value_of_css_property('background')
        print('pass',re.search('right.png',gar))

    def password_confirm_placeholder(self):
        placeholder = driver.find_element_by_id('pwd2').get_attribute('placeholder')
        if placeholder == '请再次输入密码':
            print('pass')
        else:
            print('failed')

    def protocol_error(self):
        bt = driver.find_element_by_id('btn')
        bt.click()
        # rese = driver.find_element_by_id('ck')
        # rese.click()
        gar = driver.find_element_by_xpath('/html/body/div[2]/div/div[6]/div[2]/i').value_of_css_property('background')
        print(re.search('error.png',gar).group())
        path = driver.find_element_by_xpath('/html/body/div[2]/div/div[6]/div[2]/span').text
        if path == '请同意协议':
            print('pass')
        else:
            print('failed')

    def protocol_correct(self):
        rese = driver.find_element_by_id('ck')
        rese.click()
        gar = driver.find_element_by_xpath('/html/body/div[2]/div/div[6]/div[2]/i').value_of_css_property('background')
        print('pass',re.search('right.png',gar).group())

    def total(self):
        t1 = driver.find_element_by_id('userName')
        t1.send_keys('疯狂力量药水')
        t2 = driver.find_element_by_id('pwd')
        t2.send_keys('疯狂力量药水')
        t3 = driver.find_element_by_id('pwd2')
        t3.send_keys('疯狂力量药水')
        rese = driver.find_element_by_id('ck')
        rese.click()
        bt = driver.find_element_by_id('btn')
        bt.click()
        if driver.switch_to_alert().text == '可以注册':
            print('pass')

if __name__ == '__main__':
    driver = webdriver.Chrome('C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')
    driver.get('file:///C:/Users/LYZ/AppData/Local/Temp/Rar$EXa9052.'
               '3059/7%E6%9C%8820%E5%8F%B7/jd_reg/jd_reg/demo.html##')
    driver.set_window_position(200, 100)
    driver.set_window_size(1280, 720)
    jd = Jd()

    # jd.username_format_error()                      #1、用户名：格式错误   /html/body/div[2]/div/div[6]/div[2]/span
    # jd.username_null_error()                        #2、用户名：空
    # jd.username_click_tip()                         #3、用户名：提示
    # jd.username_placeholder()                       #4、用户名：占位提示
    # jd.username_correct()                           #5、用户名：成功

    # jd.password_null_error()                        #6、密码：空
    # jd.password_format_error()                      #7、密码：格式错误
    # jd.password_format_tip()                        #8、密码强弱提示
    # jd.password_placeholder()                       #9、密码：占位提示
    # jd.password_correct()                           #10、密码：成功
    # jd.password_confirm_format_error()              #11、确认密码：错误
    # jd.password_confirm_format_correct()            #12、确认密码：成功
    # jd.password_confirm_placeholder()               #13、确认密码：占位提示
    # jd.protocol_error()                             #14、协议：错误
    # jd.protocol_correct()                           #15、协议:正确
    jd.total()                                      #16、注册成功