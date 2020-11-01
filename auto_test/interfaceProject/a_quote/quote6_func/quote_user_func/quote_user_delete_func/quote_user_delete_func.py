import sys
import os

base_path = os.getcwd()
sys.path.append(base_path)

from quote5_base.request_operation import RequestOperation


class Quote_Delete:

    def __init__(self):
        self.ro = RequestOperation()

    def quote_delete(self, method):
        self.ro.request_value(method)


# if __name__ == '__main__':
#     login = Quote_Delete()
#     login.quote_delete('删')