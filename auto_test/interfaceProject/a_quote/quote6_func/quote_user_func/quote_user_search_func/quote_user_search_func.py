import sys
import os

base_path = os.getcwd()
sys.path.append(base_path)

from auto_test.interfaceProject.a_quote.quote5_base.request_operation import RequestOperation

class Quote_Search:

    def __init__(self):
        self.ro = RequestOperation()

    def quote_search(self, method):
        self.ro.request_value(method)


if __name__ == '__main__':
    login = Quote_Search()
    login.quote_search('查')