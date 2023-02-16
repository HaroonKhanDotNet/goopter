
from selenium.webdriver.common.by import By

def liveorder_main(chromeBrowser):
    
    #liveOrders_ele = chromeBrowser.find_element(By.XPATH, "//a[@href='/liveOrders']").click()
    liveOrders_ele = chromeBrowser.find_element(By.XPATH, "//li[2]").click()


def liveorder_add(chromeBrowser):

    add_element = chromeBrowser.find_element(By.XPATH, "//div[@class='order-list-title-end-section']//*[name()='svg']")
    add_element.click()