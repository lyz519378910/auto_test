import time

from auto_test.seleniumProject.crm.crm_web_func.crm_web_user_func.crm_web_login_func import LoginPage


class CustomerAssign:

    def __init__(self):
        self.lp = LoginPage()
        self.lp.login(self.lp.ub.eo.get_cell(1, 2), self.lp.ub.eo.get_cell(1, 3))
        time.sleep(1)
        # ca = self.lp.ub.yo.get_locator('CustomerAssign', 'customerassign')
        # self.lp.bo.switch_frame("'"+ca+"'")  /html/frameset/frameset/frame[1]
        self.lp.bo.switch_frame('/html/frameset/frameset/frame[1]')
        self.lp.bo.click_element(self.lp.ub.yo.get_locator('CustomerAssign', 'ca_click'))
        self.lp.bo.switch_frame('mainFrame')
        self.lp.bo.click_element(self.lp.ub.yo.get_locator('CustomerAssign', 'ca_click_1'))

    def customer_assigon(self):
        #先删除
        self.lp.ub.co.delete_customer()
        #下拉列表选择
        self.lp.bo.select_down_menu('customerForUser',2)
        #点击提交
        self.lp.bo.click_element(self.lp.ub.yo.get_locator('CustomerAssign', 'ca_submit'))
        self.lp.lg.set_log('------添加------', 'info')


        #法二
        # def customer_add(self, **kwargs):
        #     self.lp.bo.change_frame('Links')
        #     self.lp.bo.click_element('/html/body/div/div[1]/div[1]/div[1]/img')
        #     self.lp.bo.change_frame('main')
        #     self.lp.bo.click_element('/html/body/center/table[2]/tbody/tr[2]/td[2]/a')
        #     self.lp.bo.change_window('新增客户信息')
        #     self.lp.bo.send_key('/html/body/center/form/table[1]/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/input',
        #                         kwargs.get('id', ''))
        #     self.lp.bo.send_key('/html/body/center/form/table[1]/tbody/tr[2]/td/table/tbody/tr[1]/td[4]/input',
        #                         kwargs.get('name', ''))
        #     self.lp.bo.send_key('/html/body/center/form/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input',
        #                         kwargs.get('telephone', ''))
        #     self.lp.bo.send_key('/html/body/center/form/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[4]/input',
        #                         kwargs.get('address', ''))
        #     self.lp.bo.send_key('/html/body/center/form/table[1]/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/input',
        #                         kwargs.get('relationman', ''))
        #     self.lp.bo.send_key('/html/body/center/form/table[1]/tbody/tr[2]/td/table/tbody/tr[3]/td[4]/input',
        #                         kwargs.get('other', ''))
        #     self.lp.bo.click_element('/html/body/center/form/table[2]/tbody/tr/td/input[1]')
        #
        # self.bo.click_element(self.ub.yo.get_locator('LoginPage','click'))
        # self.lg.set_log('------登录------', 'info')





# if __name__ == '__main__':
#     lp = LoginPage()
#     lp.login()
#     time.sleep(2)
#     UseBrowser.quit()
