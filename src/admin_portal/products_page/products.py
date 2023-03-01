from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.color import Color
from datetime import date, timedelta, datetime
from selenium.common.exceptions import NoSuchElementException
from random_word import RandomWords
import time
import selenium.webdriver.support.wait



def products_main(chromeBrowser):
    #chromeBrowser.implicitly_wait(10)
    chromeBrowser.get('https://admin-dev.goopter.com/products/')
    

def products_searchbox_type(chromeBrowser):
    sleep(2)
    #chromeBrowser.implicitly_wait(10)
    searchbox = chromeBrowser.find_element(By.XPATH, '/html/body/div[1]/div/section/section/main/div[2]/div/div[1]/div[1]/div[1]/span/input')
    sleep(1)
    searchbox.send_keys('tea')
    
    
#Actions
def add_group_purchase_product(chromeBrowser):
    #chromeBrowser.implicitly_wait(10)
    create_item = chromeBrowser.find_element(By.XPATH, "//button[normalize-space()='Create Item']")
    create_item.click()
    sleep(3)
#back to list
    back_arrow = chromeBrowser.find_element(By.XPATH,"//span[@aria-label='arrow-left']//*[name()='svg']").click()
    sleep(2)
#re-do create item
    chromeBrowser.find_element(By.XPATH, "//button[normalize-space()='Create Item']").click()
    tag_item_info = chromeBrowser.find_element(By.XPATH, "//div[contains(.,'Item Info')]")
    tag_item_info.click()
    
    sleep(1)
    action = ActionChains(chromeBrowser)
 #choose type   
    tag_item_info.find_element(By.XPATH, "//span[@title='Regular Product']").click()
    sleep(.5)
    tag_item_info.find_element(By.XPATH,"//div[contains(text(),'Group Purchase')]").click()
    sleep(2)
#turn on status //button[@id='status']
    status_switch = tag_item_info.find_element(By.XPATH, "//button[@id='status']")
    status_switch_color=status_switch.value_of_css_property('background-color')
    sleep(2)
    if Color.from_string(status_switch_color).hex != '#3898c8':
        status_switch.click()
    sleep(2)
#enter title
    random_words = RandomWords()
    item_title = "testing "+random_words.get_random_word()
    
    tag_item_info.find_element(By.XPATH, "//input[@id='name_en']").send_keys(item_title)
    sleep(2)
#choose category
    tag_item_info.find_element(By.XPATH, "//*[@id='category_ids']").click()
    sleep(2)
    tag_item_info.find_element(By.XPATH,"//div[contains(text(),'Dim Sum')]").click()
    sleep(1)
    tag_item_info.find_element(By.XPATH, "//div[contains(text(),'Pub here')]").click()
    sleep(1)
    tag_item_info.find_element(By.XPATH, "//div[contains(text(),'Test category')]").click()
    sleep(1)
    
    
    action.move_by_offset(100, 100).click().perform()

    sleep(2)
#turn on store show switch
    
    store_switch =tag_item_info.find_element(By.XPATH,"//button[@id='show_store_link']")
    action.move_to_element(store_switch).perform()
    sleep(1)
    store_switch_color=store_switch.value_of_css_property('background-color')
    sleep(2)
    if Color.from_string(store_switch_color).hex != '#3898c8':
        store_switch.click()
        
    sleep(1)
#turn on hide on frontend (still show in group purchase)
    frontend_switch = tag_item_info.find_element(By.XPATH, "//button[@id='is_hidden']//div[@class='ant-switch-handle']")
    frontend_switch_color=frontend_switch.value_of_css_property('background-color')
    sleep(2)
    if Color.from_string(frontend_switch_color).hex != '#3898c8':
        frontend_switch.click()
    sleep(1)
    
# enable special request
    special_request = tag_item_info.find_element(By.XPATH, "//button[@id='enable_special_request']")
    special_request_color= special_request.value_of_css_property('background-color')
    sleep(2)
    if Color.from_string(special_request_color).hex != '#3898c8':
        special_request.click()
    sleep(1)

#start & end date
    my_date = datetime.now()
    start_date = tag_item_info.find_element(By.XPATH,"//input[@id='start_date']")
    start_date.click()
    sleep(1)
    start_date.send_keys(Keys.CONTROL, 'a', Keys.BACK_SPACE, my_date.strftime('%Y-%m-%d'))
    sleep(1)
  #  tag_item_info.find_element(By.XPATH, "(//span[contains(text(),'Ok')])[2]").click()   # animating without extra node = false
    sleep(1)
    end_date = tag_item_info.find_element(By.XPATH, "//input[@id='end_date']")
    end_date.click()
    sleep(1)
    end = my_date + timedelta(days=30, hours=-1)
    
    end_date.send_keys(Keys.CONTROL, 'a', Keys.BACK_SPACE, end.strftime('%Y-%m-%d'))
  #  tag_item_info.find_element(By.XPATH, "//button[@ant-click-animating-without-extra-node='false']//span[contains(text(),'Ok')]").click()
    
    sleep(2)
    action.move_by_offset(100, 0).click().perform()
#description
    sleep(2)
    description= chromeBrowser.find_element(By.XPATH, "(//div[@contenteditable='true'])[1]")
    sleep(1)
    item_text = 'New testing '+ item_title + ' are delicious, from goopter test... ' + random_words.get_random_word()
    description.send_keys(item_text)
    
# submit
    tag_item_info.find_element(By.XPATH, "//button[@type='submit']").click()
    
    sleep(3)
    action = ActionChains(chromeBrowser)
    
#take care other tags such as seo, options and up-sales
# to access by editting the item
    my_edit = chromeBrowser.find_element(By.XPATH, "(//div[@class='ag-react-container'])[3]")
    
    sleep(1)
    my_edit.click()
#fill the option form 
    sleep(2)
    # tag_options =  my_edit.find_element(By.XPATH, "//div[@id='rc-tabs-18-tab-options']")     # this id kept rolling such as 17,18,19 
#     raise exception_class(message, screen, stacktrace)
# selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: element is not attached to the page document
    # sleep(2)
    # action.move_to_element(tag_options).click().perform()
    # tag_options.click()
    tag_options =  chromeBrowser.find_element(By.XPATH, "//div[contains(text(),'Options')]")
    action.key_down(Keys.CONTROL).click(tag_options).key_up(Keys.CONTROL).perform() 
    sleep(6)
    
    tag_options.send_keys(Keys.PAGE_DOWN)
    
    # chromeBrowser.switch_to.window(chromeBrowser.window_handles[1])  #index out of range
    sleep(3)
    
    tag_options.find_element(By.XPATH, "//button[contains(text(),'Add option value')]").click()
    sleep(1)
    # @id='rc_select_530' keep rolling, upto @id='rc_select_878'  ... 
    # option_title = tag_options.find_element(By.XPATH, "//input[@id='rc_select_530']").click()
    # option_title = tag_options.find_element(By.XPATH, "//*[contains(.,'search')]")
    option_title = tag_options.find_element(By.XPATH, "(//div[@class='ant-select-selector'])[7]")
    sleep(2)
    action.key_down(Keys.CONTROL).click(option_title).key_up(Keys.CONTROL).perform() 

    sleep(5)
    
    option_title.find_element(By.XPATH, "//div[@title='Cooking Style']").click()
    sleep(1)
    
    option_type=chromeBrowser.find_element(By.XPATH, "//div[@class='option-item-component']//div[@class='ant-select ant-select-lg ant-select-single ant-select-show-arrow']")
    sleep(1)
    option_type.click()
    sleep(1)
    option_type.find_element(By.XPATH,"//div[contains(text(),'Dropdown')]").click()   
    sleep(1)
    tag_options.find_element(By.XPATH, "(//div[@class='ant-switch-handle'])[6]").click()
    sleep(1)
    min=tag_options.find_element(By.XPATH, "//div[@class='col-left']//input[@value='1']")
    
    sleep(1)
    min.click()
    sleep(3)
    min.send_keys(Keys.BACKSPACE,'2')            #not take numbers >1
    sleep(1)
    
    max=tag_options.find_element(By.XPATH, "//div[@class='col-right']//input[@value='1']")
    
    sleep(1)
    max.click()
    sleep(2)
    max.send_keys(Keys.BACKSPACE, '9')
    sleep(1)
    add_value_button=tag_options.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-default'][normalize-space()='Add option value']").click()
    sleep(1)
    op_name = tag_options.find_element(By.XPATH, "//div[@class='input-lan-select-parent-right']//input[@type='text']")
    op_name.click()
    sleep(1)
    op_name.send_keys('large dish')
    sleep(1)
    price=tag_options.find_element(By.XPATH, "//div[@class='option-item-component']//input[@value='0']")
    price.click()
    sleep(1)
    price.send_keys('9.99')
    sleep(1)
    tag_options.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-default'][normalize-space()='Add option value']").click()
    sleep(1)
    op_name2 = tag_options.find_element(By.XPATH, "(//input[@type='text'])[24]")
    op_name2.click()
    sleep(1)
    op_name2.send_keys('grant dish')
    sleep(1)
    price2=tag_options.find_element(By.XPATH, "(//input[@value='0'])[4]")
    price2.click()
    sleep(1)
    price2.send_keys(Keys.BACKSPACE,'19.99')
    sleep(1)
    button_ok = tag_options.find_element(By.XPATH, "//button[normalize-space()='OK']")
    sleep(3)
    action.key_down(Keys.CONTROL).click(button_ok).key_up(Keys.CONTROL).perform() 

    sleep(5)
    
    tag_options.find_element(By.XPATH, "//button[normalize-space()='Save & Close']").click()
    sleep(3)
    
def products_threedots(chromeBrowser):
    #chromeBrowser.implicitly_wait(10)
    print('trying threedots..')
    sleep(1)
    
    action = ActionChains(chromeBrowser)
    
# Delete
    threedots = chromeBrowser.find_element(By.XPATH,'//*[@id="products-table-container"]/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[10]/div/div/button[2]')
    
    action.move_to_element(threedots).perform()
    
    sleep(10)
    
    threedots.find_element(By.XPATH, '//p[contains(.,"Delete")]').click()
   
    sleep(2)
    
    # answer=input('Delete ok?')
    answer='no'
    if answer=='yes':
        threedots.find_element(By.XPATH, '//span[contains(.,"OK")]').click()
    else:
        threedots.find_element(By.XPATH, '//span[contains(.,"Cancel")]').click()
    sleep(10)    
    
# Description
    threedots = chromeBrowser.find_element(By.XPATH,'//*[@id="products-table-container"]/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[10]/div/div/button[2]')
    
    action.move_to_element(threedots).perform()
    
    sleep(1)
    
    threedots.find_element(By.XPATH, '//p[.="Description"]').click()
    sleep(2)
    threedots.find_element(By.XPATH,'//p[contains(.,"any")]').send_keys('testing stuff...')
    # threedots.find_element(By.XPATH,'/html/body/div[42]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div[2]')
    
    sleep(10)
    threedots.find_element(By.XPATH,'//button[contains(., "Apply")]').click()
    sleep(10)
    

#   Copy to New product  
    threedots = chromeBrowser.find_element(By.XPATH,'//*[@id="products-table-container"]/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[10]/div/div/button[2]')
    
    action.move_to_element(threedots).perform()
    
    sleep(3)
    threedots.find_element(By.XPATH, '//p[contains(.,"Copy to New Product")]').click()
    sleep(2)
    
    threedots.find_element(By.XPATH, '//span[.="Cancel"]').click()
    sleep(10)
    
 #View Edit
 
    threedots = chromeBrowser.find_element(By.XPATH,'//*[@id="products-table-container"]/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[10]/div/div/button[2]')
    
    action.move_to_element(threedots).perform()
    
    sleep(3)

    threedots.find_element(By.XPATH, '//p[contains(.,"View/Edit")]').click()
    sleep(4)
    
    
    # Short  (manual testing for button Apply)
    chromeBrowser.get('https://admin-dev.goopter.com/products/')
    sleep(10)
    threedots = chromeBrowser.find_element(By.XPATH,'//*[@id="products-table-container"]/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[10]/div/div/button[2]')
    action.move_to_element(threedots).perform()
    
    sleep(4)
    try:
        threedots.find_element(By.XPATH, '//p[contains(.,"Short Description")]').click()
        sleep(1)
        threedots.click()
        sleep(2)
        threedots.find_element(By.XPATH,'//textarea[contains(.,"thing")]').send_keys('testing...')
        sleep(2)
    # <button type="button" class="ant-btn ant-btn-primary" ant-click-animating-without-extra-node="false">Apply</button>
    # threedots.find_element(By.XPATH,'/html/body/div[44]/div/div[2]/div/div[2]/div[2]/div/div[2]/button').click()
    # threedots.find_element(By.XPATH,'//button[.="Apply"]').click()
    # action.move_to_element_with_offset(threedots.find_element(By.XPATH,'//button[.="Apply"]'), 1000,10).click().perform()
    # M563
        sel=0
        if sel:
        
            threedots.find_element(By.XPATH, '(//button[normalize-space()="Apply"])[1]')
        else: 
            threedots.find_element(By.XPATH, '//*[contains(.,"close")]').click()
    except NoSuchElementException:  #spelling error making this code not work as expected
        pass
       
    
        
    sleep(10)
    
    
def products_sharing(chromeBrowser):
    #chromeBrowser.implicitly_wait(10)
    print('try sharing..')
    sleep(1)
    sharing = chromeBrowser.find_element(By.XPATH,'//*[@id="products-table-container"]/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[10]/div/div/button[1]')
        
    action = ActionChains(chromeBrowser)
        
    action.move_to_element(sharing).perform()
    sleep(3)
# via facebook
    sharing.find_element(By.XPATH,'//p[contains(.,"Share via Facebook")]').click()
    sleep(3)
    handles = chromeBrowser.window_handles

    chromeBrowser.switch_to.window(handles[1])
    chromeBrowser.close()
    chromeBrowser.switch_to.window(handles[0])
    sleep(10)
# via twitter
    sharing.find_element(By.XPATH,'//p[contains(.,"Share via Twitter")]').click()
    sleep(3)
    handles = chromeBrowser.window_handles

    chromeBrowser.switch_to.window(handles[1])
    chromeBrowser.close()
    chromeBrowser.switch_to.window(handles[0])
    
    sleep(3)
    
# via email  (manual testing for email app)
    sharing.find_element(By.XPATH,'//p[contains(.,"Share via Email")]').click()
    sleep(3)
    handles = chromeBrowser.window_handles
    print('how many windows? ', handles)
    
    # chromeBrowser.switch_to.window(handles[1])
    # chromeBrowser.close()
    # chromeBrowser.switch_to.window(handles[0])
   # sharing.find_element(By.XPATH, "//*['Share Product - Message (HTML)']").send_keys(Keys.ESCAPE)
    #chroweBrowser.context_click().find_elecment(By.LINK_TEXT,'Close').click().find_element(By.BUTTON, 'No').click()
    
    sleep(15)
# QR Code
    sharing = chromeBrowser.find_element(By.XPATH,'//*[@id="products-table-container"]/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[10]/div/div/button[1]')
        
    action = ActionChains(chromeBrowser)
        
    action.move_to_element(sharing).perform()
    sleep(1)
    
    sharing.find_element(By.XPATH,"//p[normalize-space()='QR Code']").click()
    sleep(3)
    
    sharing.find_element(By.XPATH,"//span[normalize-space()='Regular product QR code']").click()
    sleep(1)
    sharing.find_element(By.XPATH,"//span[normalize-space()='Instant Checkout QR Code']").click()
    sleep(1)
    sharing.find_element(By.XPATH, "//*[name()='path' and contains(@d,'M563.8 512')]").click()
    sleep(10)
# open store url

    sharing = chromeBrowser.find_element(By.XPATH,'//*[@id="products-table-container"]/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[10]/div/div/button[1]')
        
    action = ActionChains(chromeBrowser)
        
    action.move_to_element(sharing).perform()
    sleep(3)
    sharing.find_element(By.XPATH,"//p[contains(.,'Webpage')]").click()
    sleep(5)
    handles = chromeBrowser.window_handles

    chromeBrowser.switch_to.window(handles[1])
    chromeBrowser.close()
    chromeBrowser.switch_to.window(handles[0])
    sleep(8)
# copy URL
    sharing = chromeBrowser.find_element(By.XPATH,'//*[@id="products-table-container"]/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[10]/div/div/button[1]')
        
    action = ActionChains(chromeBrowser)
        
    action.move_to_element(sharing).perform()
    sleep(3)
    sharing.find_element(By.XPATH,"//p[contains(.,'URL')]").click()
    sleep(3)
    
# Poster    
    sharing = chromeBrowser.find_element(By.XPATH,'//*[@id="products-table-container"]/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[10]/div/div/button[1]')
        
    action = ActionChains(chromeBrowser)
        
    action.move_to_element(sharing).perform()
    sleep(3)
    sharing.find_element(By.XPATH,"//p[normalize-space()='Poster']").click()
    sleep(3)
    sharing.find_element(By.XPATH,"//span[normalize-space()='Low']").click()
    sleep(2)
    sharing.find_element(By.XPATH, "//div[contains(text(),'High')]").click()
    sleep(2)
    
    action.move_to_element(sharing).click().perform()
    sleep(10)

def product_enable(chromeBrowser):
    #chromeBrowser.implicitly_wait(10)
    enable = chromeBrowser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/section[1]/section[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/div[9]/div[1]/div[1]").click()
    
    sleep(1)

     
       
    
    
    
    
    
    

# 
        
        