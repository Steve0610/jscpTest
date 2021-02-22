import time

import ddt
import unittest2

from jscpExam.func.dataReader import dataReader
from jscpExam.testcase.BaseTestCase import BaseTestCase

@ddt.ddt
class verificationTest(BaseTestCase):
    table = dataReader('jscp_testdata.csv')

    @ddt.data(*table)
    def test_exam_permission(self, row):
        self.driver.get('https://www.bnuexam.cn/sxjmcardquery?type=CardNo')
        self.driver.find_element_by_class_name('name').send_keys(row[0])
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[1]/input').send_keys(row[1])
        self.driver.find_element_by_class_name('search').click()
        time.sleep(3)
        self.room = self.driver.find_element_by_css_selector('.left-card > p:nth-child(7)').text
        self.seat = self.driver.find_element_by_css_selector('.left-card > p:nth-child(8)').text
        print(self.room, self.seat)
        self.driver.back()
        print(row)
# if __name__ == '__main__':
#     unittest2.main()


