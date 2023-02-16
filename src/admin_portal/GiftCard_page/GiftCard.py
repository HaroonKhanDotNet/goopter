from selenium import webdriver
from selenium.webdriver.common.by import By




def GiftCard_main(chromeBrowser):
     chromeBrowser.get('https://admin-dev.goopter.com/giftCards')


def giftcard_link(chromeBrowser):     
     giftcard_link = chromeBrowser.find_element(By.XPATH,"//li[8]")
     giftcard_link().click

#//body[1]/div[1]/div[1]/section[1]/section[1]/main[1]/div[2]/div[1]/div[3]/div[7]/div[1]/label[1]/span[1]
#//label[@class='ant-radio-button-wrapper ant-dropdown-trigger ant-dropdown-open']
#//div[3]//div[7]
def three_dots_link(chromerBrowser):   
       three_dots =  chromerBrowser.find_element(By.CLASS_NAME,"clickable-row")
       three_dots().click


#//div[3]//div[6]//div[1]//button[1]
#/html[1]/body[1]/div[1]/div[1]/section[1]/section[1]/main[1]/div[2]/div[1]/div[3]/div[6]/div[1]/button[1]/div[1]
def switch_link(chromeBrower):
     switch_link =  chromeBrower.find_element(By.XPATH,"//div[3]//div[6]//div[1]//button[1]")
     switch_link().click

     