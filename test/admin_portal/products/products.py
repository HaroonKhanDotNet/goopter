
from selenium import webdriver
from selenium.webdriver.common.by import By

# def products_searchbox_type(chromeBrowser):

#     searchbox = chromeBrowser.find_element(By.XPATH, '/html/body/div[1]/div/section/section/main/div[2]/div/div[1]/div[1]/div[1]/span/input')
#     searchbox.send_keys('bubble')

def products_searchbox_type(chromeBrowser):

    searchbox = chromeBrowser.find_element(By.XPATH, '/html/body/div[1]/div/section/section/main/div[2]/div/div[1]/div[1]/div[1]/span/input')
    searchbox.send_keys('bubble')