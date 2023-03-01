
from selenium import webdriver


from admin_portal import login
from admin_portal.liveorder_page import liveorder
from time import sleep

#from admin_portal.products_page import products
#from admin_portal.categories_page import categories
from admin_portal.liveorder_page import liveorder

def goopter_main():

    
    chromeBrowser = webdriver.Chrome()
    chromeBrowser.maximize_window()
    chromeBrowser.implicitly_wait(10)

    # login automation
    login.admin_login(chromeBrowser)
    sleep(2)
    
    liveorder.liveorder_main(chromeBrowser)
    sleep(2)
    
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
    sleep(5)
    
    liveorder.add_product_quantity(chromeBrowser)
    sleep(5)
    
    liveorder.store_discount(chromeBrowser)
    sleep(5)
    
    liveorder.discount_type_amount(chromeBrowser)
    sleep(3)
    
    liveorder.discount_type_percentage(chromeBrowser)
    sleep(3)
    
    liveorder.input_discount(chromeBrowser)
    sleep(3)
    
    liveorder.discount_reason(chromeBrowser)
    sleep(3)
    
    liveorder.done_button(chromeBrowser)
    sleep(3)
    
    #liveorder.delivery_time(chromeBrowser)
    #sleep(3)
    
    #liveorder.pick_delivery_date(chromeBrowser)
    #sleep(3)
    
    #liveorder.pick_delivery_time(chromeBrowser)
    #sleep(3)
    
    liveorder.add_tip(chromeBrowser)
    sleep(3)
    
    liveorder.find_customer(chromeBrowser)
    sleep(3)
    
    liveorder.pick_customer(chromeBrowser)
    sleep(3)

    # products automation
    #products.products_main(chromeBrowser)
    #input()

    # products searchbox type
    products.products_searchbox_type(chromeBrowser)
    input()

    chromeBrowser.quit()


if __name__ == '__main__':
    goopter_main()
