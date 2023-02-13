
from selenium import webdriver

from admin_portal import login
from admin_portal.products_page import products
from admin_portal.categories_page import categories

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