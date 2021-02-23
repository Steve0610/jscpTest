from jscpExam.testcase.BaseTestCase import BaseTestCase


class HomePage(BaseTestCase):
    def test_homepage(self):
        contact_us = self.driver.find_element_by_css_selector('#goTop span').text
        self.assertEqual('京师测评网', self.driver.title)
        self.assertEqual('https://www.bnuexam.cn/', self.driver.current_url)
        self.assertEqual('联系我们', contact_us)
