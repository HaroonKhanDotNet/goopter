
from selenium.webdriver.common.by import By


def liveorder_main(chromeBrowser):

    chromeBrowser.get('https://admin-dev.goopter.com/liveOrders')
   
def add_order(chromeBrowser):
    
    
    add_element = chromeBrowser.find_element(By.XPATH, "//div[@class='order-list-title-end-section']//*[name()='svg']").click()
 
def add_pickup(chromeBrowser):

    pickup_element = chromeBrowser.find_element(By.XPATH, "//div[@class='ant-modal-body']//div[2]").click()
    
    
def add_continue(chromeBrowser):
    
    chromeBrowser.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-lg shipping-options-modal-continue-button']").click()

   