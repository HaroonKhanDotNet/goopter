from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains





# def GiftCard_main(chromeBrowser):
#      chromeBrowser.get('https://admin-dev.goopter.com/giftCards')


def giftcard_link(chromeBrowser):     
     giftcard_link = chromeBrowser.find_element(By.XPATH, "//li[9]").click()
   

   
     
def filter_link(chromerBrowser):   
        filter_link =  chromerBrowser.find_element(By.XPATH,"//button[@class='ant-btn ant-btn-default ant-btn-lg filter-button']//*[name()='svg']")
        filter_link().click



def three_dots_link(chromerBrowser):   
       three_dots = chromerBrowser.find_element(By.XPATH,"//div[3]//div[7]//div[1]//label[1]")
       ActionChains(chromerBrowser).move_to_element(three_dots).perform()


def Edit(chromeBrowser):
      Edit_dots= chromeBrowser.find_element(By.XPATH,"//span[normalize-space()='Edit']").click()

def Edit_title(chromeBrowser):

      EditTtile = chromeBrowser.find_element(By.XPATH, "//input[@id='name_en']")
      EditTtile.send_keys("\b new card 2023")
  
    
      #ActionChains(chromeBrowser).move_to_element(Edit_dots).perform()


#//div[3]//div[6]//div[1]//button[1]
#/html[1]/body[1]/div[1]/div[1]/section[1]/section[1]/main[1]/div[2]/div[1]/div[3]/div[6]/div[1]/button[1]/div[1]
def switch_link(chromeBrower):
     switch_link =  chromeBrower.find_element(By.XPATH,"//div[3]//div[6]//div[1]//button[1]")
     switch_link().click



     