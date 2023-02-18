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
      # earse only one character
      EditTtile.send_keys('\b')
      EditTtile.send_keys('\b')
      EditTtile.send_keys('\b')
      EditTtile.send_keys('\b')
      EditTtile.send_keys('\b')
      EditTtile.send_keys('\b')
      EditTtile.send_keys('\b')
      EditTtile.send_keys('\b')
      EditTtile.send_keys('\b')
      EditTtile.send_keys('\b')
      EditTtile.send_keys('\b')
      EditTtile.send_keys('\b')
      EditTtile.send_keys('yes new gift card ')

def catogories(chromeBrowser):
     cat = chromeBrowser.find_element(By.XPATH, "//div[@class='ant-select ant-select-lg ant-select-multiple']//div[@class='ant-select-selector']").click()
     deselect =  chromeBrowser.find_element(By.XPATH,"//span[@title='Buffets!']//span[@class='ant-select-selection-item-remove']").click()
     deselect =  chromeBrowser.find_element(By.XPATH,"//span[@title='GiftCard']//span[@class='ant-select-selection-item-remove']").click()
     select = chromeBrowser.find_element(By.XPATH, "//div[contains(text(),'Pizzas')]").click()
    
def price(chromeBrowser):
       price_txt= chromeBrowser.find_element(By.XPATH, "//input[@id='price']")
       price_txt.send_keys('\b')
       price_txt.send_keys('\b')
       price_txt.send_keys('\b')
       price_txt.send_keys('12')
           
def SpecialPrice(chromeBrowser):
       Sprice_txt= chromeBrowser.find_element(By.XPATH, "//input[@id='special_price']")
       Sprice_txt.send_keys('\b')
       Sprice_txt.send_keys('\b')
       Sprice_txt.send_keys('\b')
       Sprice_txt.send_keys('120')

def Date_Picker(chromeBrowser):
    #  Select_Date = chromeBrowser.find_element(By.XPATH,"//input[@id='special_from_date']").click()
      Date = chromeBrowser.find_element(By.XPATH, "//div[@class='ant-picker-cell-inner'][normalize-space()='25']").click()
      

def book_Value (chromeBrowser):
      Book= chromeBrowser.find_element(By.XPATH, "//input[@id='bookvalue']").click()

def SKU (chromeBrowser):
      SKU= chromeBrowser.find_element(By.XPATH, "//input[@id='sku']").click()
  
    
      #ActionChains(chromeBrowser).move_to_element(Edit_dots).perform()


#//div[3]//div[6]//div[1]//button[1]
#/html[1]/body[1]/div[1]/div[1]/section[1]/section[1]/main[1]/div[2]/div[1]/div[3]/div[6]/div[1]/button[1]/div[1]
def switch_link(chromeBrowser):
     switch_link =  chromeBrowser.find_element(By.XPATH,"//div[3]//div[6]//div[1]//button[1]")
     switch_link().click





     