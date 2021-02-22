import time

import ddt
import unittest2
from selenium.webdriver import ActionChains
from jscpExam.func.dataReader import dataReader
from jscpExam.testcase.BaseTestCase import BaseTestCase


@ddt.ddt
class examTest(BaseTestCase):

    table = dataReader('jscp_testdata.csv')

    @ddt.data(*table)
    def test_exam(self, row):
        # 登录
        # 数据驱动测试
        self.driver.get('https://www.bnuexam.cn/sxjmcardquery?type=Award')
        self.driver.find_element_by_class_name('name').send_keys(row[0])
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[1]/input').send_keys(row[1])
        self.driver.find_element_by_class_name('search').click()
        time.sleep(3)
        self.score = self.driver.find_element_by_xpath('//*[@id="app"]/section/div/p[7]').text
        self.award = self.driver.find_element_by_xpath('//*[@id="app"]/section/div/p[8]').text
        print(self.score, self.award)
        self.driver.back()
        # print(*self.table)
        print(row)

if __name__ == '__main__':
    unittest2.main()
