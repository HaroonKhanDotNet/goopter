
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def liveorder_main(chromeBrowser):

    chromeBrowser.get('https://admin-dev.goopter.com/liveOrders')
   
def add_order(chromeBrowser):
    
    
    add_element = chromeBrowser.find_element(
        By.XPATH, "//div[@class='order-list-title-end-section']//*[name()='svg']").click()
 
def add_pickup(chromeBrowser):

    pickup_element = chromeBrowser.find_element(By.XPATH, "//div[@class='ant-modal-body']//div[2]").click()
    
def add_quickpay(chromeBrowser):
    
    quickpay_element = chromeBrowser.find_element(By.XPATH, "//input[@value='6']").click()
    
def add_delivery(chromeBrowser):
    
    delivery_element = chromeBrowser.find_element(By.XPATH, "//input[@value='1']").click()   
    
    
def add_continue(chromeBrowser):
    
    chromeBrowser.find_element(
        By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-lg shipping-options-modal-continue-button']").click()
    
    
def add_chinesecuisine(chromeBrowser):
    
    chinese_element = chromeBrowser.find_element(By. XPATH, "//div[contains(text(),'Chinese Cuisine')]").click()
    
def search_box(chromeBrowser):
    
    search_box_element = chromeBrowser.find_element(
        By. XPATH, "//span[@class='ant-input-affix-wrapper']//input[@placeholder='Search by item']")
    search_box_element.send_keys('beef')
    
def product_name(chromeBrowser):
    
    product_name_element = chromeBrowser.find_element(By.ID, "product-name-109723").click()
    
def product_option_large(chromeBrowser):
    
    product_option_large_element = chromeBrowser.find_element(
        By. XPATH, "//span[@class='MuiButton-label'][normalize-space()='Large(+$7.00)']").click()
    
def confirm_button(chromeBrowser):
    
    confirm_button_element = chromeBrowser.find_element(
        By. XPATH, "//button[@class='ant-btn ant-btn-primary confirm-button']").click()

def continue_button(chromeBrowser):
    
    continue_button_element = chromeBrowser.find_element(
        By. XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[8]/div[4]/button").click()
    
def add_product_quantity(chromeBrowser):
    
    product_quantity_element = chromeBrowser.find_element(By. XPATH, "(//input[@value='1'])[1]")
    #product_quantity_element.clear()
    product_quantity_element.send_keys('\b4') 
    
def store_discount(chromeBrowser):
    store_discount_element = chromeBrowser.find_element(
        By.XPATH, "//div[@class='order-detail-price-title order-detail-price-title-clickable']").click()
    
def discount_type_amount(chromeBrowser):
    
    discount_type_amounnt_element = chromeBrowser.find_element(
        By. XPATH, "//span[normalize-space()='Amount']"
    ).click()
    
def discount_type_percentage(chromeBrowser):
    
    discount_type_percentage_element = chromeBrowser.find_element(By. XPATH, "//div[contains(text(),'Percentage')]" ).click()
    
def input_discount(chromeBrowser):
    
    input_discount_element = chromeBrowser.find_element(
        By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[2]/div/div[2]/div/div/span/span/div/div[2]/input")
    input_discount_element.send_keys('10')
    
def discount_reason(chromeBrowser):
    
    discount_reason_element = chromeBrowser.find_element(
        By. XPATH, "//div[@class='ant-form-item-control-input-content']//input[@type='text']")
    discount_reason_element.send_keys('Awesome client')
    
    
def done_button(chromeBrowser):
    
    done_button_element = chromeBrowser.find_element(By. XPATH, "//button[normalize-space()='Done']").click()
    