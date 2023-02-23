from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains




# def GiftCard_main(chromeBrowser):
#       chromeBrowser.get('https://admin-dev.goopter.com/giftCards')


def giftcard_link(chromeBrowser):     
        giftcard_link = chromeBrowser.find_element(By.XPATH, "//li[9]")
        giftcard_link.click()



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

def  picture(chromeBrowser):
     # pic=chromeBrowser.find_element(By.XPATH, "//div[@class='ant-upload-drag-container']//div//div[1]//*[name()='svg']")
      # pic1 = chromeBrowser.find_element(By.XPATH,"C:/Users/Zaina/Downloads/giftcard.png")
      # ActionChains(chromeBrowser).move_to_element(pic1).perform()
     # pic.send_keys('C:/Users/Zaina/Downloads/giftcard.png')
      
          giftcard_pic = chromeBrowser.find_element(By.XPATH, "//div[@class='ant-upload-drag-container']//div//div[1]//*[name()='svg']")
          giftcard_pic.send_keys("./giftcard.png")
   
      
      # Runtime.getRuntime().exec(" C:\Users\Zaina\Downloads\giftcard.png")
      # WebElement upload  = chromeBrowse.findElement(By.id("btnSave"));  
      # upload.click()
      #    #Upload button

      

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
   
     date= chromeBrowser.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div[2]/form/div[1]/div[2]/div/div[1]/div/div[1]/div[6]/div[1]/div/div[2]/div/div/div/div/div/input").click()
     
     
      
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
      Desc2 = chromeBrowser.find_elemet(By.XPATH,"//body/div[@id='root']/div/section[@class='ant-layout']/section[@class='ant-layout ant-layout-has-sider']/main[@class='ant-layout-content']/div[@class='wrapper-child']/form[@class='ant-form ant-form-horizontal ant-form-large items-info-form']/div[@class='ant-tabs ant-tabs-top ant-tabs-large ant-tabs-card']/div[@class='ant-tabs-content-holder']/div[@class='ant-tabs-content ant-tabs-content-top']/div[@id='rc-tabs-1-panel-item_info']/div[@class='items-tab']/div/div[@class='input-lan-select-parent']/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]")
      Desc2.send_keys('\b')
      Desc2.send_keys('\b')
      Desc2.send_keys('\b')
      Desc2.send_keys('\b')
      Desc2.send_keys('\b')
      Desc2.send_keys('\b')
      Desc2.send_keys('new cheese pizza with mozerrila and lots of cheeeesseeeee')

def saveButton (chromeBrowser):
      save = chromeBrowser.find_element(By.XPATH, "//button[@type='submit']").click()
  
 




     