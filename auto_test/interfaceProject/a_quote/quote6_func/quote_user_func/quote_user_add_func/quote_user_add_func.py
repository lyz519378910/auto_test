import sys
import os

base_path = os.getcwd()
sys.path.append(base_path)

from quote5_base.request_operation import RequestOperation


class Quote_Add:

    def __init__(self):
        self.ro = RequestOperation()

    def quote_add(self,method):
        self.ro.request_value(method)


# if __name__ == '__main__':
#     login = Quote_Add()
#     login.quote_add('增')
