import unittest2
from selenium import webdriver
from selenium.webdriver import ActionChains


class BaseTestCase(unittest2.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get('https://www.bnuexam.cn/')
        cls.driver.find_element_by_xpath('//*[@id="app"]/header/div/div/span[1]/span[1]').click()
        cls.driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/div[4]/span[1]').click()
        cls.driver.find_element_by_css_selector('.login_input.login_username').send_keys('13520397009')
        cls.driver.find_element_by_css_selector('.login_input.login_password').send_keys('123456a')
        cls.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[4]/button').click()
        # ActionChains(cls.driver).move_to_element(cls.driver.find_element_by_link_text('数学建模')).perform()
        # cls.driver.find_element_by_xpath('//*[@id="app"]/header/div/nav/a[5]/div[2]/span[4]').click()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
