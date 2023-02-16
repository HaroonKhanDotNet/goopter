import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from admin_portal import login
from admin_portal import publishmanager_page
# from admin_portal.products_page import products
# from admin_portal.categories_page import categories
from admin_portal.publishmanager_page import publishmanager


def goopter_main():

    options = Options()
    options.add_argument("--disable-notifications")

    chromeBrowser = webdriver.Chrome(options=options)
    chromeBrowser.maximize_window()

    # login automation
    login.admin_login(chromeBrowser)
    time.sleep(3)

    # publish manager automation
    publishmanager.publishmanager_main(chromeBrowser)
    time.sleep(2)

    #publishmanager.publishmanager_republish(chromeBrowser)
    #time.sleep(2)
    
    publishmanager.publishmanager_unpublish(chromeBrowser)
    time.sleep(2)
    
    publishmanager.publishmanager_sync(chromeBrowser)
    time.sleep(5)

    # products automation
    # products.products_main(chromeBrowser)
    # input()

    # products searchbox type
    # products.products_searchbox_type(chromeBrowser)
    # input()

    input()
    chromeBrowser.quit()


if __name__ == '__main__':
    goopter_main()
