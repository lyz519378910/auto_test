import unittest
from base.base_request import BaseRequest
url1 = "http://www.imooc.com"

data = {
    "username":"1111",
    "password":"2222"
}
request = BaseRequest()

class TestCase1(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        pass

    def setUp(self) -> None:
        pass

    # def test_1(self):
    #     # res = requests.get(url=url1,params=data).json()
    #     data1 = {
    #         "user":"11111"
    #     }
    #     self.assertDictEqual(data1,data)

    # def test_2(self):
    #     data1 = {
    #         "username": "1111",
    #         "password": "2222"
    #     }
    #     self.assertDictEqual(data1,data,msg="不等")

    # def test_3(self):
    #     flag = True
    #     self.assertFalse(flag)

    def test_4(self):
        res = request.run_main('get',url1,data)
        print(res)

    # def test_5(self):
    #     flag = "111"
    #     flag1 = "222"
    #     self.assertEqual(flag,flag1,msg="两个str不等")

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
