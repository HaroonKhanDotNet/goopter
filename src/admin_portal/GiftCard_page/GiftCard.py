from selenium import webdriver
from selenium.webdriver.common.by import By




def GiftCard_main(chromeBrowser):
     chromeBrowser.get('https://admin-dev.goopter.com/giftCards')


def giftcard_link(chromeBrowser):     
     giftcard_link = chromeBrowser.find_element(By.XPATH,"//li[8]")
     giftcard_link().click

    
    # //div[@class='icon-button-text d-inline']
     
def filter_link(chromerBrowser):   
        filter_link =  chromerBrowser.find_element(By.XPATH,"//button[@class='ant-btn ant-btn-default ant-btn-lg filter-button']")
        filter_link().click


#//body[1]/div[1]/div[1]/section[1]/section[1]/main[1]/div[2]/div[1]/div[3]/div[7]/div[1]/label[1]/span[1]
#//label[@class='ant-radio-button-wrapper ant-dropdown-trigger ant-dropdown-open']
#//div[3]//div[7]
#//body/div[@id='root']/div/section[@class='ant-layout']/section[@class='ant-layout ant-layout-has-sider']/main[@class='ant-layout-content']/div[@class='wrapper-child']/div[@class='gift-card-table']/div[7]/div[1]
#
def three_dots_link(chromerBrowser):   
       three_dots =  chromerBrowser.find_element(By.XPATH,"")
       three_dots().click


#//div[3]//div[6]//div[1]//button[1]
#/html[1]/body[1]/div[1]/div[1]/section[1]/section[1]/main[1]/div[2]/div[1]/div[3]/div[6]/div[1]/button[1]/div[1]
def switch_link(chromeBrower):
     switch_link =  chromeBrower.find_element(By.XPATH,"//div[3]//div[6]//div[1]//button[1]")
     switch_link().click



     