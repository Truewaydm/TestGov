from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class LoginTest():
    def LoginTest(self):
        super(webdriver)

#get the path of chromedriver
#create a new Chrome session
#эта надпись нужно для того чтобы указать путь к файлу chromedriver для работы с ним
driver = webdriver.Chrome('C:\\Users\\Dmitriy\\PycharmProjects\\TestGov\\drivers\\chromedriver.exe')

#настроить дефолтное ожидание браузера при выполнении
#браузер будет повторять действия которые мы задаем в течении 10 секунд, если не выполнит выведет ошибку
driver.implicitly_wait(30)

#Менеджеру Driver дали команды открыть браузер в макс размере
driver.maximize_window()

#navigation to the application home page
#Вствляет URL в адресную строку браузера
main_page_url = driver.get("https://test-gov.ald.in.ua/purchases")

#click dropdawn menu
click_menu = driver.find_element_by_xpath(".//*[@id='liLoginNoAuthenticated']/a").click()

#click Login
click_Login = driver.find_element_by_xpath(".//*[@id='butLoginPartial']").click()

#input email/password/submit
#Найди мне елемент по xpath -> указать локатор и вставь мне данные(sendKeys) в поле
input_email = driver.find_element_by_xpath(".//*[@id='Email']").send_keys('qwe@12gmail.com')
input_password = driver.find_element_by_xpath(".//*[@id='Password']").send_keys('123456')
click_submit = driver.find_element_by_xpath(".//*[@id='submitLogin']").click()


#close the browser window
#Дать команду webDriver -> close - закрывает вкладку quit - закрывает браузер
driver.quit()
#driver.close()
