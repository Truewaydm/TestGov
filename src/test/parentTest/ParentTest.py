import unittest
from selenium import webdriver


class ParentTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:\\Users\\Dmitriy\\PycharmProjects\\TestGov\\drivers\\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.close()

    def checkAC(self, message, actual_result, expected_result):
        assert message, actual_result in expected_result
