from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.color import Color
from selenium.common.exceptions import NoSuchElementException

from datetime import date, timedelta, datetime

from random_word import RandomWords


def test_products_searchbox_type(browser: Chrome, products):

    searchbox = browser.find_element(
        By.XPATH, '/html/body/div[1]/div/section/section/main/div[2]/div/div[1]/div[1]/div[1]/span/input')

    searchbox.send_keys('tea')


# Actions
def test_add_group_purchase_product(browser: Chrome, products):
 
    # create_item
    browser.find_element(By.XPATH, "//button[normalize-space()='Create Item']").click()

    # back to list - back_arrow 
    browser.find_element(By.XPATH, "//span[@aria-label='arrow-left']//*[name()='svg']").click()

    # re-do create item
    browser.find_element(By.XPATH, "//button[normalize-space()='Create Item']").click()
    
    tag_item_info = browser.find_element(By.XPATH, "//div[contains(.,'Item Info')]")
    tag_item_info.click()

    action = ActionChains(browser)
    # choose type
    tag_item_info.find_element(By.XPATH, "//span[@title='Regular Product']").click()

    tag_item_info.find_element(By.XPATH, "//div[contains(text(),'Group Purchase')]").click()

    # turn on status //button[@id='status']
    status_switch = tag_item_info.find_element(By.XPATH, "//button[@id='status']")
    status_switch_color = status_switch.value_of_css_property('background-color')

    if Color.from_string(status_switch_color).hex != '#3898c8': status_switch.click()

    # enter title
    random_words = RandomWords()
    item_title = "testing "+random_words.get_random_word()

    tag_item_info.find_element(By.XPATH, "//input[@id='name_en']").send_keys(item_title)

    # choose category
    tag_item_info.find_element(By.XPATH, "//*[@id='category_ids']").click()

    tag_item_info.find_element(By.XPATH, "//div[contains(text(),'Dim Sum')]").click()

    tag_item_info.find_element(By.XPATH, "//div[contains(text(),'Pub here')]").click()

    tag_item_info.find_element(By.XPATH, "//div[contains(text(),'Test category')]").click()

    #action.move_by_offset(100, 0).click().perform()

    # turn on store show switch
    store_switch = tag_item_info.find_element(By.XPATH, "//button[@id='show_store_link']")
    action.move_to_element(store_switch).perform()

    store_switch_color = store_switch.value_of_css_property('background-color')

    if Color.from_string(store_switch_color).hex != '#3898c8': store_switch.click()

    # turn on hide on frontend (still show in group purchase)
    frontend_switch = tag_item_info.find_element(By.XPATH, "//button[@id='is_hidden']//div[@class='ant-switch-handle']")
    frontend_switch_color = frontend_switch.value_of_css_property('background-color')

    if Color.from_string(frontend_switch_color).hex != '#3898c8': frontend_switch.click()

    # enable special request
    special_request = tag_item_info.find_element(By.XPATH, "//button[@id='enable_special_request']")
    special_request_color = special_request.value_of_css_property('background-color')

    if Color.from_string(special_request_color).hex != '#3898c8': special_request.click()

    # start & end date
    my_date = datetime.now()
    start_date = tag_item_info.find_element(By.XPATH, "//input[@id='start_date']")
    start_date.click()

    start_date.send_keys(Keys.CONTROL, 'a', Keys.BACK_SPACE, my_date.strftime('%Y-%m-%d'))

    # tag_item_info.find_element(By.XPATH, "(//span[contains(text(),'Ok')])[2]").click()   # animating without extra node = false

    end_date = tag_item_info.find_element(By.XPATH, "//input[@id='end_date']")
    end_date.click()

    end = my_date + timedelta(days=30, hours=-1)

    end_date.send_keys(Keys.CONTROL, 'a', Keys.BACK_SPACE, end.strftime('%Y-%m-%d'))

    tag_item_info.find_element(By.XPATH, "//button[@ant-click-animating-without-extra-node='false']//span[contains(text(),'Ok')]").click()

    # action.move_by_offset(100, 0).click().perform()

    # description
    description = browser.find_element(By.XPATH, "(//div[@contenteditable='true'])[1]")

    item_text = 'New testing ' + item_title + ' are delicious, from goopter test... ' + random_words.get_random_word()
    description.send_keys(item_text)

    # submit
    tag_item_info.find_element(By.XPATH, "//button[@type='submit']").click()

    action = ActionChains(browser)

    # take care other tags such as seo, options and up-sales
    # to access by editting the item
    my_edit = browser.find_element(By.XPATH, "(//div[@class='ag-react-container'])[3]")

    my_edit.click()
    # fill the option form

    # tag_options =  my_edit.find_element(By.XPATH, "//div[@id='rc-tabs-18-tab-options']")     # this id kept rolling such as 17,18,19
    # raise exception_class(message, screen, stacktrace)
    # selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: element is not attached to the page document
    #
    # action.move_to_element(tag_options).click().perform()
    # tag_options.click()
    tag_options = browser.find_element(By.XPATH, "//div[contains(text(),'Options')]")
    action.key_down(Keys.CONTROL).click(tag_options).key_up(Keys.CONTROL).perform()
    # sleep(6)

    tag_options.send_keys(Keys.PAGE_DOWN)

    # browser.switch_to.window(browser.window_handles[1])  #index out of range

    tag_options.find_element(By.XPATH, "//button[normalize-space()='Add option value']").click()

    # @id='rc_select_530' keep rolling, upto @id='rc_select_878'  ...
    # option_title = tag_options.find_element(By.XPATH, "//input[@id='rc_select_530']").click()
    # option_title = tag_options.find_element(By.XPATH, "//*[contains(.,'search')]")
    option_title = tag_options.find_element(By.XPATH, "(//div[@class='ant-select-selector'])[7]")

    action.key_down(Keys.CONTROL).click(option_title).key_up(Keys.CONTROL).perform()

    # sleep(5)

    # option_title.find_element(By.XPATH, "//div[contains(text(),'Cooking Style')]").click() # click intercepted, other element receive the click??
    option_title.find_element(By.XPATH, "//div[@title='Cooking Style']").click()

    option_type = browser.find_element(By.XPATH, "//div[@class='option-item-component']//div[@class='ant-select ant-select-lg ant-select-single ant-select-show-arrow']")

    option_type.click()

    option_type.find_element(By.XPATH, "//div[contains(text(),'Dropdown')]").click()

    tag_options.find_element(By.XPATH, "(//div[@class='ant-switch-handle'])[6]").click()

    min = tag_options.find_element(By.XPATH, "//div[@class='col-left']//input[@value='1']")

    min.click()

    min.send_keys(Keys.BACKSPACE, '2')  # not take numbers >1

    max = tag_options.find_element(By.XPATH, "//div[@class='col-right']//input[@value='1']")

    max.click()

    max.send_keys(Keys.BACKSPACE, '9')

    add_value_button = tag_options.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-default'][normalize-space()='Add option value']").click()

    op_name = tag_options.find_element(By.XPATH, "//div[@class='input-lan-select-parent-right']//input[@type='text']")
    op_name.click()

    op_name.send_keys('large dish')

    price = tag_options.find_element(By.XPATH, "//div[@class='option-item-component']//input[@value='0']")
    price.click()

    price.send_keys('9.99')

    tag_options.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-default'][normalize-space()='Add option value']").click()

    op_name2 = tag_options.find_element(By.XPATH, "(//input[@type='text'])[24]")
    op_name2.click()

    op_name2.send_keys('grant dish')

    price2 = tag_options.find_element(By.XPATH, "(//input[@value='0'])[4]")
    price2.click()

    price2.send_keys(Keys.BACKSPACE, '19.99')

    button_ok = tag_options.find_element(By.XPATH, "//button[normalize-space()='OK']")

    action.key_down(Keys.CONTROL).click(button_ok).key_up(Keys.CONTROL).perform()

    # sleep(5)

    tag_options.find_element(By.XPATH, "//button[normalize-space()='Save & Close']").click()


def test_products_threedots(browser: Chrome, products):

    print('trying threedots..')

    action = ActionChains(browser)

# Delete
    threedots = browser.find_element(
        By.XPATH, '//*[@id="products-table-container"]/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[10]/div/div/button[2]')

    action.move_to_element(threedots).perform()

    # sleep(10)

    threedots.find_element(By.XPATH, '//p[contains(.,"Delete")]').click()

    # answer=input('Delete ok?')
    answer = 'no'
    if answer == 'yes':
        threedots.find_element(By.XPATH, '//span[contains(.,"OK")]').click()
    else:
        threedots.find_element(
            By.XPATH, '//span[contains(.,"Cancel")]').click()
    # sleep(10)

# Description
    threedots = browser.find_element(
        By.XPATH, '//*[@id="products-table-container"]/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[10]/div/div/button[2]')

    action.move_to_element(threedots).perform()

    threedots.find_element(By.XPATH, '//p[.="Description"]').click()

    threedots.find_element(
        By.XPATH, '//p[contains(.,"any")]').send_keys('testing stuff...')
    # threedots.find_element(By.XPATH,'/html/body/div[42]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div[2]')

    # sleep(10)
    threedots.find_element(By.XPATH, '//button[contains(., "Apply")]').click()
    # sleep(10)


#   Copy to New product
    threedots = browser.find_element(
        By.XPATH, '//*[@id="products-table-container"]/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[10]/div/div/button[2]')

    action.move_to_element(threedots).perform()

    threedots.find_element(
        By.XPATH, '//p[contains(.,"Copy to New Product")]').click()

    threedots.find_element(By.XPATH, '//span[.="Cancel"]').click()
    # sleep(10)

 # View Edit

    threedots = browser.find_element(
        By.XPATH, '//*[@id="products-table-container"]/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[10]/div/div/button[2]')

    action.move_to_element(threedots).perform()

    threedots.find_element(By.XPATH, '//p[contains(.,"View/Edit")]').click()
    # sleep(4)

    (By.XPATH, '//li[6]')
    # Short  (manual testing for button Apply)
    browser.get('https://admin-dev.goopter.com/products/')
    # sleep(10)
    threedots = browser.find_element(
        By.XPATH, '//*[@id="products-table-container"]/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[10]/div/div/button[2]')
    action.move_to_element(threedots).perform()

    # sleep(4)
    try:
        threedots.find_element(
            By.XPATH, '//p[contains(.,"Short Description")]').click()

        threedots.click()

        threedots.find_element(
            By.XPATH, '//textarea[contains(.,"thing")]').send_keys('testing...')

    # <button type="button" class="ant-btn ant-btn-primary" ant-click-animating-without-extra-node="false">Apply</button>
    # threedots.find_element(By.XPATH,'/html/body/div[44]/div/div[2]/div/div[2]/div[2]/div/div[2]/button').click()
    # threedots.find_element(By.XPATH,'//button[.="Apply"]').click()
    # action.move_to_element_with_offset(threedots.find_element(By.XPATH,'//button[.="Apply"]'), 1000,10).click().perform()
    # M563
        sel = 0
        if sel:

            threedots.find_element(
                By.XPATH, '(//button[normalize-space()="Apply"])[1]')
        else:
            threedots.find_element(
                By.XPATH, '//*[contains(.,"close")]').click()
    except NoSuchElementException:  # spelling error making this code not work as expected
        pass

    # sleep(10)


def test_products_sharing(browser: Chrome, products):

    print('try sharing..')

    sharing = browser.find_element(
        By.XPATH, '//*[@id="products-table-container"]/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[10]/div/div/button[1]')

    action = ActionChains(browser)

    action.move_to_element(sharing).perform()

# via facebook
    sharing.find_element(
        By.XPATH, '//p[contains(.,"Share via Facebook")]').click()

    handles = browser.window_handles

    browser.switch_to.window(handles[1])
    browser.close()
    browser.switch_to.window(handles[0])
    # sleep(5)
# via twitter
    sharing = browser.find_element(
        By.XPATH, '//*[@id="products-table-container"]/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[10]/div/div/button[1]')

    action = ActionChains(browser)

    action.move_to_element(sharing).perform()

    sharing.find_element(
        By.XPATH, '//p[contains(.,"Share via Twitter")]').click()

    handles = browser.window_handles

    browser.switch_to.window(handles[1])
    browser.close()
    browser.switch_to.window(handles[0])


# via email  (manual testing for email app)
    sharing = browser.find_element(
        By.XPATH, '//*[@id="products-table-container"]/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[10]/div/div/button[1]')

    action = ActionChains(browser)

    action.move_to_element(sharing).perform()

    sharing.find_element(
        By.XPATH, '//p[contains(.,"Share via Email")]').click()

    handles = browser.window_handles
    print('how many windows? ', handles)

    # browser.switch_to.window(handles[1])
    # browser.close()
    # browser.switch_to.window(handles[0])
   # sharing.find_element(By.XPATH, "//*['Share Product - Message (HTML)']").send_keys(Keys.ESCAPE)
    #chroweBrowser.context_click().find_elecment(By.LINK_TEXT,'Close').click().find_element(By.BUTTON, 'No').click()

    # sleep(15)
# QR Code
    sharing = browser.find_element(
        By.XPATH, '//*[@id="products-table-container"]/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[10]/div/div/button[1]')

    action = ActionChains(browser)

    action.move_to_element(sharing).perform()

    sharing.find_element(By.XPATH, "//p[normalize-space()='QR Code']").click()

    sharing.find_element(
        By.XPATH, "//span[normalize-space()='Regular product QR code']").click()

    sharing.find_element(
        By.XPATH, "//span[normalize-space()='Instant Checkout QR Code']").click()

    sharing.find_element(
        By.XPATH, "//*[name()='path' and contains(@d,'M563.8 512')]").click()
    # sleep(10)
# open store url

    sharing = browser.find_element(
        By.XPATH, '//*[@id="products-table-container"]/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[10]/div/div/button[1]')

    action = ActionChains(browser)

    action.move_to_element(sharing).perform()

    sharing.find_element(By.XPATH, "//p[contains(.,'Webpage')]").click()
    # sleep(5)
    handles = browser.window_handles

    browser.switch_to.window(handles[1])
    browser.close()
    browser.switch_to.window(handles[0])
    # sleep(8)
# copy URL
    sharing = browser.find_element(
        By.XPATH, '//*[@id="products-table-container"]/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[10]/div/div/button[1]')

    action = ActionChains(browser)

    action.move_to_element(sharing).perform()

    sharing.find_element(By.XPATH, "//p[contains(.,'URL')]").click()


# Poster
    sharing = browser.find_element(
        By.XPATH, '//*[@id="products-table-container"]/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[10]/div/div/button[1]')

    action = ActionChains(browser)

    action.move_to_element(sharing).perform()

    sharing.find_element(By.XPATH, "//p[normalize-space()='Poster']").click()

    sharing.find_element(By.XPATH, "//span[normalize-space()='Low']").click()

    sharing.find_element(By.XPATH, "//div[contains(text(),'High')]").click()

    action.move_to_element(sharing).click().perform()
    # sleep(10)


def test_product_enable(browser: Chrome, products):

    enable = browser.find_element(
        By.XPATH, "/html[1]/body[1]/div[1]/div[1]/section[1]/section[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/div[9]/div[1]/div[1]").click()


#
