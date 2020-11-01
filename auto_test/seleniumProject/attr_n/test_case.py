import pytest


class TestCase:

    def test_one_case(self):
        print('a')

    #跳过
    @pytest.mark.skip('see you')
    def test_two_case(self):
        print(2/0)

    def test_three_case(self):
        print('c')

if __name__ == '__main__':
    #生成报告
    # '../'：之前所有test文件都要跑
    # pytest.main(['-v','-s','--html=report.html','../'])
    #'--reruns','1' : 遇错重跑，次数1
    pytest.main(['-v', '-s','--reruns','1','--html=../crm/crm_report/report.html'])
