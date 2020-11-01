if __name__ == '__main__':
    suite = unittest.TestSuite()
    test_case = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    # lst = [login_case,]                       #放在列表
    # suite.addTests(lst)                       #addTests  多类添加
    suite.addTest(test_case)

    date_now = time.strftime('%Y-%m-%d', time.localtime())              #设置时间
    report_path = 'D:\\Python\\report_python'                           #报告位置
    report_name = report_path + "/" + 'report_' + date_now + '.html'    #报告名称，将时间加入文件
    with open(report_name,'wb+') as file:
        runner = HTMLTestRunner(stream=file, verbosity=1, title='auto_test',description='ui_auto_test')
        runner.run(suite)