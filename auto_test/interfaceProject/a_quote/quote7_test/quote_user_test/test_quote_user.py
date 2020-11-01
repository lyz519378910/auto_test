import pytest

from quote4_util.quote_log import AutoLog
from quote6_func.quote_user_func.quote_user_add_func.quote_user_add_func import Quote_Add
from quote6_func.quote_user_func.quote_user_delete_func.quote_user_delete_func import Quote_Delete
from quote6_func.quote_user_func.quote_user_update_func.quote_user_update_func import Quote_Update
from quote6_func.quote_user_func.quote_user_search_func.quote_user_search_func import Quote_Search


class Test_quote_user:

    def setup(self):
        self.qa = Quote_Add()

        self.qd = Quote_Delete()

        self.qu = Quote_Update()

        self.qs = Quote_Search()

        self.al = AutoLog()

    def test_function(self):
        self.qa.quote_add('增')
        self.al.set_log('增加','info')
        self.qs.quote_search('查')
        self.al.set_log('查找','info')
        self.qu.quote_update('改')
        self.al.set_log('修改', 'info')
        self.qd.quote_delete('删')
        self.al.set_log('删除', 'info')



if __name__ == '__main__':
    pytest.main(['-v', '-s', '--reruns', '1', '--html=../../quote2_report/report.html'])