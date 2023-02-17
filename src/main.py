
from selenium import webdriver
from time import sleep

from admin_portal import login
#from admin_portal.products_page import products
from admin_portal.GiftCard_page import GiftCard
#from admin_portal.categories_page import categories

def goopter_main():

    chromeBrowser = webdriver.Chrome()
    chromeBrowser.maximize_window()

    # login automation
    
    login.admin_login(chromeBrowser)
    sleep(5)
    #don't make it less than 5 sec

    # GiftCard.GiftCard_main(chromeBrowser)
    # sleep(5)

    GiftCard.giftcard_link(chromeBrowser)
    sleep(5)
     
    # GiftCard.filter_link(chromeBrowser)
    # sleep(10)

    GiftCard.three_dots_link(chromeBrowser)
    sleep(5)
    GiftCard.Edit(chromeBrowser)
    sleep(5)
    GiftCard.Edit_title(chromeBrowser)
    sleep(5)
    # GiftCard.switch_link(chromeBrowser)
    # sleep(10)


    chromeBrowser.quit()


if __name__ == '__main__':
    goopter_main()
