import unittest2

from jscpExam.lib.HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':

    suite = unittest2.defaultTestLoader.discover('./testcase', '*Test.py')

    path = 'report/TestReport.html'
    with open(path, 'wb') as file:
        HTMLTestRunner(stream=file, verbosity=1, title="自动化测试报告", description="测试环境：Chrome").run(suite)
    print('测试报告生产')
