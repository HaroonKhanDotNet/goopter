from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


# class
# __init__
# self

class Page:

    #page constructor
    def __init__(self, title, url, browser):
        self.title = title
        self.url = url
        self.browser = browser
        self.browser.maximize_window()
        self.browser.implicitly_wait(5)

    def getPage(self):
        self.browser.get(self.url)

    def setElem(self, by, xpath, text):

        elem = self.browser.find_element(by, xpath)
        elem.send_keys(text)

    def clickElem(self, by, xpath):
        self.browser.find_element(by, xpath).click()

    #page destructor
    def __del__(self):
        # todo: need to logout first
        self.browser.quit()



goopter_landing_page = Page('Goopter Business Portal', 'https://admin-dev.goopter.com/', Chrome())
goopter_landing_page.getPage()
goopter_landing_page.setElem(By.NAME, 'username', 'haroondev')
goopter_landing_page.setElem(By.NAME, 'password', '20230130')
goopter_landing_page.clickElem(By.XPATH, "//*[@id='root']/div/div/div[1]/form/div/div[3]/div/div/div/button")

input()