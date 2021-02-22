import ddt

from jscpExam.func.dataReader import dataReader
from jscpExam.testcase.BaseTestCase import BaseTestCase

@ddt.ddt
class verificationTest(BaseTestCase):
    table = dataReader('jscp_testdata.csv')

    @ddt.data(*table)
    def test_exam_permission(self, row):
        self.driver.get('https://www.bnuexam.cn/sxjmcardquery?type=CardNo')



