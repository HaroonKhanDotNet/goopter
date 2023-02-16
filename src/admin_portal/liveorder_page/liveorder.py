
from selenium.webdriver.common.by import By


def liveorder_main(chromeBrowser):

    chromeBrowser.get('https://admin-dev.goopter.com/liveOrders')
   
def add_order(chromeBrowser):
    
    
    
    #add_element = chromeBrowser.find_element(By.XPATH, '//path[contains(.,"M19 13h-6v6h-2v-6H5v-2H6V5h2v6h6v2z")]').click()
    
    add_element = chromeBrowser.find_element(By.XPATH, "//div[@class='order-list-title-end-section']//*[name()='svg']").click()
 
    #add_element.click()   