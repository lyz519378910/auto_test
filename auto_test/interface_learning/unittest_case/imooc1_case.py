import unittest
import sys
import os
from interface_learning.base.base_request import BaseRequest
import requests
import mock

import json
def read_json():
    with open("D:\\Python\\auto_test\\interface_learning\\config\\user_data.json") as file:
        data = json.load(file)
    return data

def get_value(key):
    data = read_json()
    return data[key]

host = 'http://www.imooc.com/'
class ImoocCase(unittest.TestCase):
    br = BaseRequest()

    def test_banner(self):
        url = host + 'api3/getbanneradvertver2'
        data = {
            'timestamp': '1561269343481',
            'uid': '7213561',
            'token': '7ad09430cbaf927af642ab843ec374ef',
            'type': '1',
            'marking': 'androidbanner',
            'uuid': '41b650ef846688193728ff7381eb6c1c',
            'secrect': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWUiOiI3MjEzNTYxIiwianRpIjoiM2I2NDg0NjQ2Nzk4NjI3NzU1YjRmZWE0ODliMDNmNmUiLCJkZXZpY2UiOiJtb2JpbGUifQ.EvGIFSHhij4lgEMdCtotFoTMtWSJLwVvridsoaWzdZY'
        }
        mock_method = mock.Mock(return_value=get_value('api3/getbanneradvertver2'))
        ImoocCase.br.run_main = mock_method
        res = ImoocCase.br.run_main('post',url,data)
        self.assertEqual(res['errorCode'],1000)

if __name__ == '__main__':
    unittest.main()
