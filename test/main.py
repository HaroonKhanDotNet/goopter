import time
from selenium import webdriver

from admin_portal import login
##from admin_portal import publishmanager_page
# from admin_portal.liveorder_page import liveorder
from time import sleep

#from admin_portal.products_page import products
from admin_portal.GiftCard_page import GiftCard
## from admin_portal.Gift_card import gift_card
#from admin_portal.categories_page import categories
#from datetime import date 
from admin_portal.GiftCard_page import Editpage#from admin_portal.publishmanager_page import publishmanager
from admin_portal.liveorder_page import liveorder
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
    input()

    chromeBrowser.quit()


if __name__ == '__main__':
    goopter_main()
    
    
