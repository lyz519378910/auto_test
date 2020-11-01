
from auto_test.seleniumProject.quote.base.usebrowser import UseBrowser


class BrowserOperation:

    def __init__(self,driver):
        self.driver = driver

    def open_url(self,url):
        try:
            self.driver.get(url)
        except Exception as e:
            print(e,'url address error!')

    def send_key(self,xpath_param,content):
        try:
            self.driver.find_element_by_xpath(xpath_param).send_keys(content)
        except Exception as e:
            print(e,'element not find!')

    def click_element(self,xpath_param):
        try:
            self.driver.find_element_by_xpath(xpath_param).click()
        except Exception as e:
            print(e,'element not find!')

    def get_text(self,xpath_param):
        try:
            text = self.driver.find_element_by_xpath(xpath_param).text
        except Exception as e:
            print(e, 'element not find!')
        return text

    def change_frame(self,frame_param):
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame(frame_param)

    def change_window(self,window_name):
        for window_hd in self.driver.window_handles:
            self.driver.switch_to.window(window_hd)
            if self.driver.title == window_name:
                print('pass')
                break

# if __name__ == '__main__':
#     ub = UseBrowser()
#     bo = BrowserOperation(UseBrowser.driver)
#     bo.open_url('http://localhost:8080/JavaPrj_6/')
#     bo.send_key('//*[@id="UserName"]','admin')
#     bo.send_key('//*[@id="Password"]','admin')
#     bo.click_element('/html/body/table/tbody/tr[1]/td[2]/form/table/tbody/tr[6]/td/input[1]')
#     UseBrowser.quit()