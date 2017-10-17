from selenium import webdriver
import unittest


class ParentTest:
    def __init__(self, wd):  # конструктор передаем адрес wd драйвера
        self.webdriver = webdriver.Chrome(wd)  # инициализируем вебдрайвер по конкретному полученому адресу


class BeforeAfterTest(unittest.TestCase):
    def __init__(self):
        self.chrm = ParentTest("") #self.chrm єто обьект ParentTest в которм есть вебдрайвер

    def setUp(self):
        self.chrm = ParentTest('C:\\Users\\Dmitriy\\PycharmProjects\\TestGov\\drivers\\chromedriver.exe')
        self.chrm.webdriver.maximize_window()
        self.chrm.webdriver.implicitly_wait(30)

    def tearDown(self):
        self.chrm.webdriver.quit()
