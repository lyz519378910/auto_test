from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
import time
import re

class Quote:

    def username_click_tip(self):
        driver.find_element_by_id('UserName').send_keys('123')
        driver.find_element_by_id('Password').send_keys('123')
        # gra = driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td[2]/form/table/tbody/tr[5]/td/img').\
        #     value_of_css_property('background')
        # print(gra)
        # print(re.search('default.png', gra))
        path = driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td[2]/form/table/tbody/tr[5]/td').text
        if path == '请勿非法登录！':
            print('pass')
        else:
            print('failed')

    def username_correct(self):
        driver.find_element_by_id('UserName').send_keys('admin')
        driver.find_element_by_id('Password').send_keys('admin123')
        driver.find_element_by_name('submit').click()
        driver.switch_to.frame('main')
        text = driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/span')
        if text == '欢迎使用报价管理系统':
            print('pass')
        else:
            print('failed')
        # path = driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/span').text
        # if path == '欢迎使用报价管理系统':
        #     print('pass')
        # else:
        #     print('failed')

    def customer_add(self):
        driver.find_element_by_id('UserName').send_keys('admin')
        driver.find_element_by_id('Password').send_keys('admin123')
        driver.find_element_by_name('submit').click()
        for v in driver.window_handles:
            driver.switch_to.window(v)
            if driver.title == '报价管理系统':
                driver.switch_to.frame('Links')           #进框
                actions = ActionChains(driver)
                element = driver.find_element_by_class_name('noLine')
                element1 = driver.find_element_by_class_name('imgnob')

                actions.click(element).perform()           #perform()  执行的意思
                actions.click(element1).perform()          #perform()  执行的意思
                driver.switch_to.default_content()         #出框
                driver.switch_to.frame('main')             #进框
                driver.find_element_by_xpath('/html/body/center/table[2]/tbody/tr[2]/td[2]/a').click()

                #添加

                for v in driver.window_handles:
                    driver.switch_to.window(v)
                    if driver.title == '新增客户信息':
                        driver.find_element_by_name('customerNO').clear()
                        driver.find_element_by_name('customerNO').send_keys('s001')
                        driver.find_element_by_name('customerName').clear()
                        driver.find_element_by_name('customerName').send_keys('lyz')
                        driver.find_element_by_name('phone').clear()
                        driver.find_element_by_name('phone').send_keys('185')
                        driver.find_element_by_name('address').clear()
                        driver.find_element_by_name('address').send_keys('cd')
                        driver.execute_script("document.getElementsByName('relationman').readOnly=false")
                        driver.execute_script("document.getElementsByName('relationman').values='lyz'")
                        driver.find_element_by_name('relationman').clear()
                        driver.find_element_by_name('relationman').send_keys('lyz')
                        driver.find_element_by_name('otherInfo').clear()
                        driver.find_element_by_name('otherInfo').send_keys('lyz')
                        cn6 = driver.find_element_by_name('saveButton')
                        cn6.click()
                        break

    def customer_update(self):
        driver.find_element_by_id('UserName').send_keys('admin')
        driver.find_element_by_id('Password').send_keys('admin123')
        driver.find_element_by_name('submit').click()
        for v in driver.window_handles:
            driver.switch_to.window(v)
            if driver.title == '报价管理系统':
                driver.switch_to.frame('Links')     # 进框
                actions = ActionChains(driver)
                element = driver.find_element_by_class_name('noLine')
                element1 = driver.find_element_by_class_name('imgnob')

                actions.click(element).perform()    # perform()  执行的意思
                actions.click(element1).perform()   # perform()  执行的意思
                driver.switch_to.default_content()  # 出框
                driver.switch_to.frame('main')      # 进框
                driver.find_element_by_xpath('/html/body/center/form/table[1]/tbody/tr[3]/td[7]/a[2]').click()

                # 修改

                for v in driver.window_handles:
                    driver.switch_to.window(v)
                    if driver.title == '更新客户信息':
                        driver.find_element_by_name('address').clear()
                        driver.find_element_by_name('address').send_keys('cd')
                        cn6 = driver.find_element_by_name('saveButton')
                        cn6.click()

                        for v in driver.window_handles:
                            driver.switch_to.window(v)
                            if driver.title == '更新记录成功':
                                print('pass')
                                break
                        break

    #    imgnob
    def customer_search(self):
        driver.find_element_by_id('UserName').send_keys('admin')
        driver.find_element_by_id('Password').send_keys('admin123')
        driver.find_element_by_name('submit').click()
        for v in driver.window_handles:
            driver.switch_to.window(v)
            if driver.title == '报价管理系统':
                driver.switch_to.frame('Links')        # 进框
                actions = ActionChains(driver)
                element = driver.find_element_by_class_name('noLine')

                actions.click(element).perform()       # perform()  执行的意思
                # actions.click(element1).perform()    # perform()  执行的意思
                driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/img').click()
                driver.switch_to.default_content()     # 出框
                driver.switch_to.frame('main')         # 进框
                # driver.find_element_by_xpath('/html/body/center/form/table[1]/tbody/tr[3]/td[7]/a[2]').click()

                # 修改

                driver.find_element_by_name('customerNO').clear()
                driver.find_element_by_name('customerNO').send_keys('0201305')
                cn6 = driver.find_element_by_name('saveButton')
                cn6.click()
                if driver.find_element_by_xpath('/html/body/center/form/table[1]/tbody/tr[2]/td[1]').text == '0201305':
                    print('pass')


if __name__ == '__main__':
    driver = webdriver.Chrome('C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')
    driver.get('http://localhost:8080/JavaPrj_6')
    driver.implicitly_wait(10)
    driver.set_window_position(200, 100)
    driver.set_window_size(1280, 720)
    quote = Quote()

    # quote.username_click_tip()                        #登录失败
    quote.username_correct()                          #登陆成功
    # quote.customer_add()                              #客户添加
    # quote.customer_update()                           #客户更新
    # quote.customer_search()                           #客户查询