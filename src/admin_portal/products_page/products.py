from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.color import Color
from datetime import date, timedelta, datetime
from selenium.common.exceptions import NoSuchElementException
from random_word import RandomWords
import time
import selenium.webdriver.support.wait



def products_main(chromeBrowser):

    chromeBrowser.get('https://admin-dev.goopter.com/products')
    #products_link = chromeBrowser.find_element(By.XPATH, '//*[@id="root"]/div/section/section/aside[2]/div/div/div[2]/ul/li[6]/span[2]/a')
    #products_link.click()

def products_searchbox_type(chromeBrowser):
    sleep(2)
    #chromeBrowser.implicitly_wait(10)
    searchbox = chromeBrowser.find_element(By.XPATH, '/html/body/div[1]/div/section/section/main/div[2]/div/div[1]/div[1]/div[1]/span/input')
    searchbox.send_keys('bubble')