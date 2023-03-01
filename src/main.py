
from selenium import webdriver

from admin_portal import login
from admin_portal.liveorder_page import liveorder
from time import sleep

#from admin_portal.products_page import products
from admin_portal.Gift_card import gift_card
#from admin_portal.categories_page import categories
from time import sleep
from selenium.webdriver.support.color import Color
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.wait
from admin_portal.liveorder_page import liveorder

def goopter_main():

    
    chromeBrowser = webdriver.Chrome()
    chromeBrowser.maximize_window()

    # login automation
    login.admin_login(chromeBrowser)
    input()

    # products automation
    products.products_main(chromeBrowser)
    input()

    # products searchbox type
    products.products_searchbox_type(chromeBrowser)
    sleep(1)
    
    products.add_group_purchase_product(chromeBrowser)
    sleep(1)

    products.products_sharing(chromeBrowser)  
    sleep(1)
    
    products.products_threedots(chromeBrowser)
    sleep(1)
    
    #sign out
    selection=chromeBrowser.find_element(By.XPATH,"//span[contains(text(),'Goopter')]")
    sleep(2)
    action.move_to_element(selection).perform()
    sleep(6)
    selection.find_element(By.XPATH,"//span[normalize-space()='Sign Out']").click()
    sleep(3)
    
    print('88')
    chromeBrowser.quit()


if __name__ == '__main__':
    goopter_main()
    
    
