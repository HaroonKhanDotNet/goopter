
from selenium.webdriver.common.by import By


def liveorder_main(chromeBrowser):

    chromeBrowser.get('https://admin-dev.goopter.com/liveOrders')
   
def add_order(chromeBrowser):
    
    
    add_element = chromeBrowser.find_element(By.XPATH, "//div[@class='order-list-title-end-section']//*[name()='svg']").click()
 
def add_pickup(chromeBrowser):

    pickup_element = chromeBrowser.find_element(By.XPATH, "//div[@class='ant-modal-body']//div[2]").click()
    
def add_quickpay(chromeBrowser):
    
    quickpay_element = chromeBrowser.find_element(By.XPATH, "//input[@value='6']").click()
    
def add_delivery(chromeBrowser):
    
    delivery_element = chromeBrowser.find_element(By.XPATH, "//input[@value='1']").click()   
    
    
def add_continue(chromeBrowser):
    
    chromeBrowser.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-lg shipping-options-modal-continue-button']").click()
    
    
def add_chinesecuisine(chromeBrowser):
    
    chinese_element = chromeBrowser.find_element(By. XPATH, "//div[contains(text(),'Chinese Cuisine')]").click()
    
def search_box(chromeBrowser):
    
    search_box_element = chromeBrowser.find_element(By. XPATH, "//span[@class='ant-input-affix-wrapper']//input[@placeholder='Search by item']")
    search_box_element.send_keys('beef')
    
def product_name(chromeBrowser):
    
    product_name_element = chromeBrowser.find_element(By.ID, "product-name-109723").click()
    
def product_option_large(chromeBrowser):
    
    product_option_large_element = chromeBrowser.find_element(By. XPATH, "//span[@class='MuiButton-label'][normalize-space()='Large(+$7.00)']").click()
    
def confirm_button(chromeBrowser):
    
    confirm_button_element = chromeBrowser.find_element(By. XPATH, "//button[@class='ant-btn ant-btn-primary confirm-button']").click()

   