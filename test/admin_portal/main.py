
from selenium import webdriver
import logging
from admin_portal import test_login
from admin_portal.products_page import test_products
from admin_portal.Gift_card import test_gift_card
from admin_portal.categories_page import categories
from time import sleep
from selenium.webdriver.support.color import Color
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def test_goopter_main():

    chromeBrowser = webdriver.Chrome()
    #chromeBrowser.maximize_window()
    
   # MainWindow = chromeBrowser.current_window_handle()

    # login automation
    test_login.test_admin_login(chromeBrowser)
    sleep(5)
    
# on control
    action = ActionChains(chromeBrowser)
    sleep(2)
    select=chromeBrowser.find_element(By.XPATH, " //*[name()='path' and contains(@d,'M4 12v8a2 ')]")
    action.move_to_element(select).perform()
    sleep(2)
    
    
    selection=chromeBrowser.find_element(By.XPATH,"//span[contains(text(),'Goopter')]")
    sleep(2)
    action.move_to_element(selection).perform()
    sleep(6)
    
    select=chromeBrowser.find_element(By.XPATH, " //*[name()='path' and contains(@d,'M4 12v8a2 ')]")
    action.move_to_element(select).perform()
    sleep(6)
    
# localized  (manual testing) <button type="button" class="ant-btn ant-btn-default ant-btn-sm ant-dropdown-trigger" style="border: none; box-shadow: none; display: flex; justify-content: space-between; align-items: center; color: rgb(56, 152, 200);" ant-click-animating-without-extra-node="false"><span>English</span><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 1024 1024" height="14" width="14" xmlns="http://www.w3.org/2000/svg" style="margin-left: 8px;"><path d="M884 256h-75c-5.1 0-9.9 2.5-12.9 6.6L512 654.2 227.9 262.6c-3-4.1-7.8-6.6-12.9-6.6h-75c-6.5 0-10.3 7.4-6.5 12.7l352.6 486.1c12.8 17.6 39 17.6 51.7 0l352.6-486.1c3.9-5.3.1-12.7-6.4-12.7z"></path></svg></button>
    action = ActionChains(chromeBrowser)
    sleep(3)
    
    selection=chromeBrowser.find_element(By.XPATH,"//button[@type='button']//span[contains(text(),'English')]")
    
    action.move_to_element(selection).perform()
    
    sleep(5)
    
# on sync

    sync_location=chromeBrowser.find_element(By.XPATH,"//div[contains(@class,'publish-tag')]")
    sync_color = sync_location.value_of_css_property('background-color')
    if Color.from_string(sync_color).hex == '#57a857':
        print('All sync ..')
    else:
        sync_location.click()
        sleep(1)
        sync_location.find_element(By.XPATH, "//span[normalize-space()='OK']").click()
        sleep(20)
    sleep(5)


# online switch
    online = chromeBrowser.find_element(By.XPATH,'//button[@role="switch"]').click()
    sleep(1)
    
    handles=chromeBrowser.window_handles
    
    if (len(handles)==2) : 
        online.find_element(By.XPATH, "//span[normalize-space()='OK']").click()
        sleep(2)
        online = chromeBrowser.find_element(By.XPATH,'//button[@role="switch"]').click()
    
    sleep(4)



#on gift card
   # gift_card.gift_card(chromeBrowser)
   # sleep(5)
   
    
    # on products page
    
    logging.basicConfig(filename='logs/products_page.log', encoding='utf-8', level=logging.INFO, format='%(levelname)s %(asctime)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

    test_products.test_products_main(chromeBrowser)
    sleep(5)

    test_products.test_product_enable(chromeBrowser)
    sleep (3)
    
    # products.product_enable(chromeBrowser)
    # sleep (3)
    # products searchbox type
    test_products.test_products_searchbox_type(chromeBrowser)
    sleep(1)
    
    test_products.test_add_group_purchase_product(chromeBrowser)
    sleep(1)

    test_products.test_products_sharing(chromeBrowser)  
    sleep(1)
    
    test_products.test_products_threedots(chromeBrowser)
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


# if __name__ == '__main__':
#     goopter_main()
    
    
