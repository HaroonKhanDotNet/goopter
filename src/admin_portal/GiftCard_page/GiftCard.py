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
      EditTtile.send_keys('new gift card ')

def  picture(ChromeBrowser):
      pic = ChromeBrowser.find_element(By.XPATH, "//div[@class='ant-upload-drag-container']//div//div[1]//*[name()='svg']").click()
      pic.send_keys('C:\Users\Zaina\Downloads\giftcard.png')
      

#       def FileName = 'C:\\Users\\jdoe\\MyDocs\\Sample.pdf'
# //Wait for the 'UploadButton' to display
# WebUI.waitForElementVisible(findTestObject('ManObjects/UploadButton'), 30, FailureHandling.OPTIONAL))
# WebUI.sendKeys(findTestObject('ManObjects/DocumentUpload'), File

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
      #Date = chromeBrowser.find_element(By.XPATH, "//input[@id='special_from_date']").click()
      #date = chromeBrowser.find_element(By.XPATH, "//div[@class='ant-picker ant-picker-large ant-picker-status-success ant-picker-focused']//div[@class='ant-picker-input']").click()
     # pick_the_date = chromeBrowser.find_elment(By.XPATH, "//td[@class='ant-picker-cell ant-picker-cell-in-view ant-picker-cell-selected']//div[@class='ant-picker-cell-inner'][normalize-space()='10']").click()
     # ok_btn = chromeBrowser.find_element (By.XPATH, "//body[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[2]/button[1]").click()
      date= chromeBrowser.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div[2]/form/div[1]/div[2]/div/div[1]/div/div[1]/div[6]/div[1]/div/div[2]/div/div/div/div/div/input").click()
      #selectDate = chromeBrowser.find_element(By.XPATH,"//body[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/ul[1]/li[15]/div[1]").click()
     # DatePicked = chromeBrowser.find_element(By.XPATH, "//td[@title='2023-04-14']//div[@class='ant-picker-cell-inner'][normalize-space()='14']").click()
      #date1= chromeBrowser.find_element(By.XPATH, "//button[@ant-click-animating-without-extra-node='false']//span[contains(text(),'Ok')]").click()
      
      #ActionChains(chromeBrowser).move_to_element(Date_Picker).perform()
     
      
def sale_End_Date(chromeBrowser):
    Date = chromeBrowser.find_element (By.XPATH, "/html/body/div[1]/div/section/section/main/div[2]/form/div[1]/div[2]/div/div[1]/div/div[1]/div[6]/div[2]/div/div[2]/div/div/div/div/div/input").click()
     
def book_Value (chromeBrowser):
      Book= chromeBrowser.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div[2]/form/div[1]/div[2]/div/div[1]/div/div[1]/div[7]/div[1]/div/div[2]/div/div/div/div/div/div[2]/input")
      Book.send_keys('\b')
      Book.send_keys('\b')
      Book.send_keys('\b')
      Book.send_keys('23')

def SKU (chromeBrowser):
      SKUs= chromeBrowser.find_element(By.XPATH, "//input[@id='sku']")
      SKUs.send_keys('\b')
      SKUs.send_keys('\b')
      SKUs.send_keys('\b')
      SKUs.send_keys('22')


def Short_Desc(chromeBrower):
      Desc = chromeBrower.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div[2]/form/div[1]/div[2]/div/div[1]/div/div[1]/div[8]/div[1]/div/div[2]/div/div/div/div/span/textarea")
      Desc.send_keys('\b')
      Desc.send_keys('\b')
      Desc.send_keys('\b')
      Desc.send_keys('\b')
      Desc.send_keys('\b')
      Desc.send_keys('\b')
      Desc.send_keys('new cheese pizza')

def Description(chromeBrowser):
      Desc2 = chromeBrowser.find_elemet(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/section[1]/section[1]/main[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[10]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/p[1]")
      Desc2.send_keys('\b')
      Desc2.send_keys('\b')
      Desc2.send_keys('\b')
      Desc2.send_keys('\b')
      Desc2.send_keys('\b')
      Desc2.send_keys('\b')
      Desc2.send_keys('new cheese pizza with mozerrila')

  
    
      #ActionChains(chromeBrowser).move_to_element(Edit_dots).perform()


#//div[3]//div[6]//div[1]//button[1]
#/html[1]/body[1]/div[1]/div[1]/section[1]/section[1]/main[1]/div[2]/div[1]/div[3]/div[6]/div[1]/button[1]/div[1]
def switch_link(chromeBrowser):
     switch_link =  chromeBrowser.find_element(By.XPATH,"//div[3]//div[6]//div[1]//button[1]")
     switch_link().click





     