
from selenium import webdriver
from selenium.webdriver.common.by import By


def admin_login(chromeBrowser):

    chromeBrowser.get('https://admin-dev.goopter.com/')
    
# # chromeBrowser.page_source will get everything ; find_element(By.XPATH,"//*").get_attribute("outerHTML")
    
    # my_page_source=chromeBrowser.page_source
    # actualString = my_page_source.replace('\n', '')
    # print('actual string : ', actualString)
    # expectedFile = open('Goopter Business Portal.html', 'r')
    # expectedString = expectedFile.read().replace('\n', '')
    # expectedFile.close()
    # print('expected string: ', expectedString)
    
    # if actualString.casefold() == expectedString.casefold():
    if 1:
        

        userName_txt = chromeBrowser.find_element(By.NAME, 'username')
        userName_txt.send_keys('cynthiadev3')

        password_txt = chromeBrowser.find_element(By.NAME, 'password')
        password_txt.send_keys('ok20230117')

        login_btn = chromeBrowser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/form/div/div[3]/div/div/div/button')
        login_btn.click()
    else:
        print("page source not consistent")