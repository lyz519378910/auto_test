from auto_test.seleniumProject.crm.crm_util.crm_db.crm_mysql import DbOperation
import re

class CustomerOperation:

    def __init__(self):
        self.do = DbOperation('localhost','quote')

    def delete_customer(self):
        self.do.delete_data("delete from customer_info where customer_name = 'admin' ")

    def delete_customer_care(self):
        self.do.delete_data("delete from customer_care where care_theme = '节日'")

    def judge_customer_care_add_correct(self):
        self.do.operation_data("select * from customer_care where care_theme = '节日'",0,'care_theme')





if __name__ == '__main__':
    co = CustomerOperation()
    co.judge_customer_care_add_correct()
