from selenium import webdriver


def test_load():
    chromeBrowser = webdriver.Chrome()
    chromeBrowser.get('https://admin-dev.goopter.com/')
    assert chromeBrowser.title == 'Goopter Admin Portal'
 





