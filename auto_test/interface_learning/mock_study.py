import mock
import requests
import unittest

def post_request(url,data):
    res = requests.post(url,data).json()
    return res

def get_request(url,data):
    res = requests.get(url,data).json()
    return res



class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        print('start!')

    def test_1(self):
        url = "http://www.imooc.com/login/register"
        data = {
            "username": "lyz",
        }
        success_test = mock.Mock(return_value=data["username"])
        self.assertEqual("lyz", success_test.return_value)
        # success_test = data["username"]
        # self.assertEqual("lyz",success_test)

    def tearDown(self) -> None:
        print('end')


if __name__ == '__main__':
    unittest.main()
