import unittest

from auto_test.seleniumProject.quote.webpage_func.customer_manager.customerpage import CustomerPage


class CustomerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.cp = CustomerPage()

    def test_1_cusomer_add_id(self):
        self.cp.customer_add(id = '1')
        self.assertEqual(self.cp.get_add_sucess_text(),'添加记录成功!')

    # def test_2_cusomer_add_name(self):
    #     pass

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
