
from selenium import webdriver
from selenium.webdriver.common.by import By

def products_main(chromeBrowser):

    chromeBrowser.get('https://admin-dev.goopter.com/products')
    #products_link = chromeBrowser.find_element(By.XPATH, '//*[@id="root"]/div/section/section/aside[2]/div/div/div[2]/ul/li[6]/span[2]/a')
    #products_link.click()

def products_searchbox_type(chromeBrowser):

    searchbox = chromeBrowser.find_element(By.XPATH, '/html/body/div[1]/div/section/section/main/div[2]/div/div[1]/div[1]/div[1]/span/input')
    searchbox.send_keys('bubble')