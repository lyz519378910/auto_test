import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select

from auto_test.seleniumProject.quote.base.usebrowser import UseBrowser


class BrowserOperation:

    def __init__(self,driver):
        self.driver = driver


    #打开url
    def open_url(self,url):
        try:
            self.driver.get(url)
        except Exception as e:
            print(e,'url address error!')

    #传数据
    def send_key(self,xpath_param,content):
        try:
            self.driver.find_element_by_xpath(xpath_param).send_keys(content)
        except Exception as e:
            print(e,'element not find!')


    #遍历查询数据正确
    def judge_search(self,xpath_param):
        try:
            return self.driver.find_element_by_xpath(xpath_param).text
        except Exception as e:
            print(e,'element not find!')

    #按钮 点击
    def click_element(self,xpath_param):
        try:
            actions = ActionChains(self.driver)
            #以后可以改变，如换成id,name等
            element = self.driver.find_element_by_xpath(xpath_param)
            actions.click(element).perform()  # perform()  执行的意思
        except Exception as e:
            print(e,'element not find!')

    #获取某个字段文本
    def get_text(self,xpath_param):
        try:
            text = self.driver.find_element_by_xpath(xpath_param).text
        except Exception as e:
            print(e, 'element not find!')
        return text

    #进入框
    def switch_frame(self,frame_id):
        if '/' not in frame_id:
            print(frame_id)
            self.driver.switch_to.parent_frame()
            self.driver.switch_to.frame(frame_id)
        else:
            print(frame_id)
            self.driver.switch_to.parent_frame()
            self.driver.switch_to.frame(self.driver.find_element_by_xpath(frame_id))

    #进入新窗体（拿取新窗体的title）
    def change_window(self,window_name):
        for window_hd in self.driver.window_handles:
            self.driver.switch_to.window(window_hd)
            if self.driver.title == window_name:
                break
            else:
                print(self.driver.title + '!=' + window_name)

    #获取警告框的text消息
    def alert_text(self):
        alert = Alert(self.driver)
        return alert.text

    # 确认警告
    def alert_accept(self):
        Alert(self.driver).accept()


    def login_correct(self,assertEqual,excel_param,flag):
        for v in self.driver.window_handles:
            self.driver.switch_to.window(v)
            assertEqual(excel_param, self.driver.title)
            flag
            break

    #下拉列表选择
    def select_down_menu(self,param,site_num):
        select_element = self.driver.find_element_by_name(param)
        sel = Select(select_element)
        sel.select_by_index(site_num)


# if __name__ == '__main__':
#     ub = UseBrowser()
#     bo = BrowserOperation(UseBrowser.driver)
#     bo.open_url('http://localhost:8080/JavaPrj_6/')
#     bo.send_key('//*[@id="UserName"]','admin')
#     bo.send_key('//*[@id="Password"]','admin')
#     bo.click_element('/html/body/table/tbody/tr[1]/td[2]/form/table/tbody/tr[6]/td/input[1]')
#     UseBrowser.quit()