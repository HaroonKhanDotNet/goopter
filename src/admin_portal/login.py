from selenium import webdriver
from selenium.webdriver.common.by import By


def admin_login(chromeBrowser):

    chromeBrowser.get('https://admin-dev.goopter.com/')

    userName_txt = chromeBrowser.find_element(By.NAME, 'username')
    userName_txt.send_keys('taleydev')

    password_txt = chromeBrowser.find_element(By.NAME, 'password')
    password_txt.send_keys('20230117')

    login_btn = chromeBrowser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/form/div/div[3]/div/div/div/button')
    login_btn.click() 