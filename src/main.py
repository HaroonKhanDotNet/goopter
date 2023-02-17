
from selenium import webdriver

from admin_portal import login
from admin_portal.liveorder_page import liveorder
from time import sleep

#from admin_portal.products_page import products
#from admin_portal.categories_page import categories

def goopter_main():

    chromeBrowser = webdriver.Chrome()
    chromeBrowser.maximize_window()

    # login automation
    login.admin_login(chromeBrowser)
    sleep(3)
    
    liveorder.liveorder_main(chromeBrowser)
    sleep(3)
    
    liveorder.add_order(chromeBrowser)
    sleep(3)
    
    liveorder.add_pickup(chromeBrowser)
    sleep(3)
    
    liveorder.add_quickpay(chromeBrowser)
    sleep(3)
    
    
    liveorder.add_delivery(chromeBrowser)
    sleep(3)
    
    
    liveorder.add_continue(chromeBrowser)
    sleep(3)
    
    liveorder.add_chinesecuisine(chromeBrowser)
    sleep(3)
    
    liveorder.search_box(chromeBrowser)
    sleep(3)
    
    liveorder.product_name(chromeBrowser)
    sleep(3)
    
    liveorder.product_option_large(chromeBrowser)
    sleep(3)
    
    liveorder.confirm_button(chromeBrowser)
    sleep(3)
    
    liveorder.continue_button(chromeBrowser)
    sleep(10)
    

    # products automation
    #products.products_main(chromeBrowser)
    #input()

    # products searchbox type
    #products.products_searchbox_type(chromeBrowser)
    #input()

    chromeBrowser.quit()


if __name__ == '__main__':
    goopter_main()
