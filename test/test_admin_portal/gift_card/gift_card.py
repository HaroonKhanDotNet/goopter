from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

def gift_card(chromeBrowser):
    chromeBrowser.get('https://admin-dev.goopter.com/giftCards')
      
    action = ActionChains(chromeBrowser)
    sleep(1)
    
    cards = chromeBrowser.find_element(By.XPATH,"//div[3]//div[7]//div[1]//label[1]")
    
    action.move_to_element(cards).perform()
    
    sleep(10)