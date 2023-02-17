
from selenium import webdriver

from admin_portal import login
from admin_portal.products_page import products
from admin_portal.Gift_card import gift_card
from admin_portal.categories_page import categories
from time import sleep

def goopter_main():

    chromeBrowser = webdriver.Chrome()
    #chromeBrowser.maximize_window()
    
   # MainWindow = chromeBrowser.current_window_handle()

    # login automation
    login.admin_login(chromeBrowser)
    
    sleep(10)
    
   # gift_card.gift_card(chromeBrowser)
   # sleep(5)
    
    # products automation
    products.products_main(chromeBrowser)
    sleep(5)

    # products searchbox type
    products.products_searchbox_type(chromeBrowser)
    sleep(1)

    products.products_sharing(chromeBrowser)  
    sleep(1)
    
    products.products_threedots(chromeBrowser)
    sleep(1)
    
    
    
    print('88')
    chromeBrowser.quit()


if __name__ == '__main__':
    goopter_main()
    
    
