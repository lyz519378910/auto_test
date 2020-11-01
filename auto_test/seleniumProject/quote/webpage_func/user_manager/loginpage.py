import time

from auto_test.seleniumProject.quote.base.browseroperation import BrowserOperation
from auto_test.seleniumProject.quote.base.usebrowser import UseBrowser


class LoginPage:

    def __init__(self):
        self.ub = UseBrowser()
        self.bo = BrowserOperation(UseBrowser.driver)
        self.bo.open_url('http://localhost:8080/JavaPrj_6/')

    def login(self,user='',paswd=''):
        self.bo.send_key('//*[@id="UserName"]',user)
        self.bo.send_key('//*[@id="Password"]',paswd)
        self.bo.click_element('/html/body/table/tbody/tr[1]/td[2]/form/table/tbody/tr[6]/td/input[1]')

    def login_correct_text(self,frame_param,frame_path):
        self.bo.change_frame(frame_param)
        return self.bo.get_text(frame_path)



# if __name__ == '__main__':
#     lp = LoginPage()
#     lp.login()
#     time.sleep(2)
#     UseBrowser.quit()
