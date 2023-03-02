import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


from admin_portal import login
#from admin_portal import publishmanager_page
# from admin_portal.products_page import products
# from admin_portal.categories_page import categories
#from admin_portal.publishmanager_page import publishmanager
from admin_portal.liveorder_page import liveorder

def goopter_main():

    options = Options()
    options.add_argument("--disable-notifications")

    chromeBrowser = webdriver.Chrome(options=options)
    chromeBrowser.maximize_window()

    # login automation
    login.admin_login(chromeBrowser)
    time.sleep(2)

    #live order automation
    liveorder.liveorder_main(chromeBrowser)
    time.sleep(2)

    #liveorder.liverorder_quick_action(chromeBrowser)

    #liveorder.liveorder_quick_action_print(chromeBrowser)
    
    #liveorder.liveorder_quick_action_complete(chromeBrowser)
   
    #liveorder.liveorder_quick_action_cancel_order(chromeBrowser)
  
    #liveorder.liveorder_quick_action_update_payment_cash(chromeBrowser)

    #liveorder.liveorder_quick_action_update_payment_card(chromeBrowser)
    
    #liveorder.liveorder_quick_action_update_payment_wechat(chromeBrowser)
        
    #liveorder.liveorder_quick_action_update_payment_alipay(chromeBrowser)
    
    #liveorder.liveorder_quick_action_update_payment_union(chromeBrowser)
    
    #liveorder.liveorder_copy_customer_name(chromeBrowser)
        
    #liveorder.liveorder_copy_customer_phone_number(chromeBrowser)
    
    #liveorder.liveorder_display_item_detail_page(chromeBrowser)

    #liveorder.liveorder_add_comment(chromeBrowser)

    #liveorder.liveorder_display_order_history(chromeBrowser)

    #liveorder.liveorder_display_address_on_map(chromeBrowser)
    
    #liveorder.liveorder_change_pick_up_time(chromeBrowser)
    
    #liveorder.liveorder_change_commute_time(chromeBrowser)
    
    #liveorder.liveorder_accept_delivery_order(chromeBrowser)
    
    #liveorder.liveorder_ready_for_delivery(chromeBrowser)

    #liveorder.liverorder_start_delivery(chromeBrowser)

    #liveorder.liveorder_complete_delivery(chromeBrowser)

    #liveorder.liveorder_accept_pickup(chromeBrowser)
    
    liveorder.liveorder_ready_for_pickup(chromeBrowser)

    # live order automation
    #liveorder.liveorder_export(chromeBrowser)
    #liveorder.liverorder_search(chromeBrowser)

    # publish manager automation
    #publishmanager.publishmanager_main(chromeBrowser)
    #time.sleep(2)

    #publishmanager.publishmanager_republish(chromeBrowser)
    #time.sleep(2)
    
    #publishmanager.publishmanager_unpublish(chromeBrowser)
    #time.sleep(2)

    #publishmanager.publishmanager_sync(chromeBrowser)
    #time.sleep(5)

    # products automation
    #products.products_main(chromeBrowser)
    #input()

    # products searchbox type
    #products.products_searchbox_type(chromeBrowser)
    #input()


    input()
    chromeBrowser.quit()


if __name__ == '__main__':
    goopter_main()
