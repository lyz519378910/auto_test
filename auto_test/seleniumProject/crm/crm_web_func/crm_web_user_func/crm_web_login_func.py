from auto_test.seleniumProject.crm.crm_util.crm_log import AutoLog
from auto_test.seleniumProject.crm.crm_base.browseroperation import BrowserOperation
from auto_test.seleniumProject.crm.crm_base.usebrowser import UseBrowser


class LoginPage:

    def __init__(self):
        self.ub = UseBrowser()                              #实例化操作网页
        self.lg = AutoLog()                                 #实例化日志
        self.bo = BrowserOperation(UseBrowser.driver)       #实例化网页操作
        self.bo.open_url(self.ub.eo.get_cell(1, 1))         #打开Excel下标中的网页

        #url在Excel中的位置
        # self.lg.set_log('------登陆页面------', 'info')

    #登录函数
    def login(self,user='',paswd=''):
        self.bo.send_key(self.ub.yo.get_locator('LoginPage','username') ,user)         #yaml文件
        self.lg.set_log('------账号------', 'info')
        self.bo.send_key(self.ub.yo.get_locator('LoginPage','password'),paswd)
        self.lg.set_log('------密码------', 'info')
        self.bo.click_element(self.ub.yo.get_locator('LoginPage','click'))
        self.lg.set_log('------登录------', 'info')

    #登录成功返回信息函数
    def login_correct_text(self,frame_id,frame_path):
        self.bo.switch_frame(frame_id)
        return self.bo.get_text(frame_path)






# if __name__ == '__main__':
#     lp = LoginPage()
#     lp.login()
#     time.sleep(2)
#     UseBrowser.quit()
