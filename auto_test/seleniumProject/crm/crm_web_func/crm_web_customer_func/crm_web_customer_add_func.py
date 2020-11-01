import time

from auto_test.seleniumProject.crm.crm_web_func.crm_web_user_func.crm_web_login_func import LoginPage


class CustomerAdd:

    def __init__(self):
        #登录
        self.lp = LoginPage()
        self.lp.login(self.lp.ub.eo.get_cell(1, 2), self.lp.ub.eo.get_cell(1, 3))
        time.sleep(1)
        #进入frame、按钮
        self.lp.bo.switch_frame('topFrame')
        self.lp.bo.click_element(self.lp.ub.yo.get_locator('LoginPage', 'mainFrame1'))
        self.lp.bo.switch_frame('mainFrame')
        self.lp.bo.click_element(self.lp.ub.yo.get_locator('LoginPage', 'button1'))

    def customer_add(self,customerName,customerEmail,customerBirthday,customerAddMan):
        self.lp.ub.co.delete_customer()
        self.lp.bo.send_key(self.lp.ub.yo.get_locator('CustomerAdd','customerName'),customerName)      #yaml文件
        self.lp.lg.set_log('------姓名------', 'info')
        self.lp.bo.send_key(self.lp.ub.yo.get_locator('CustomerAdd', 'customerEmail'), customerEmail)
        self.lp.lg.set_log('------邮箱------', 'info')
        self.lp.bo.driver.execute_script("window.document.getElementById("+"'"+self.lp.ub.yo.get_locator('CustomerAdd','customerBirthday1')+"'"+").readOnly=false")
        self.lp.bo.driver.execute_script("window.document.getElementById("+"'"+self.lp.ub.yo.get_locator('CustomerAdd','customerBirthday1')+"'"+").value="+"'"+customerBirthday+"'")

        # self.lp.bo.driver.execute_script("window.document.getElementById('customerBirthday').readOnly = false")
        # self.lp.bo.driver.execute_script("window.document.getElementById('customerBirthday').value = "+" ' "+customerBirthday+" ' ")

        # self.bo.send_key(self.ub.yo.get_locator('CustomerAdd', 'customerBirthday'), customerBirthday)
        self.lp.lg.set_log('------生日------', 'info')
        self.lp.bo.send_key(self.lp.ub.yo.get_locator('CustomerAdd', 'customerAddMan'), customerAddMan)
        self.lp.lg.set_log('------创建人------', 'info')
        self.lp.bo.click_element(self.lp.ub.yo.get_locator('CustomerAdd', 'click'))
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
