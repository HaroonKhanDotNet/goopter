
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
    sleep(5)
    
    liveorder.liveorder_main(chromeBrowser)
    sleep(5)
    
    liveorder.add_order(chromeBrowser)
    sleep(5)
    
    liveorder.add_pickup(chromeBrowser)
    sleep(5)
    
    liveorder.add_continue(chromeBrowser)
    sleep(5)

    # products automation
    #products.products_main(chromeBrowser)
    #input()

    # products searchbox type
    #products.products_searchbox_type(chromeBrowser)
    #input()

    chromeBrowser.quit()


if __name__ == '__main__':
    goopter_main()
