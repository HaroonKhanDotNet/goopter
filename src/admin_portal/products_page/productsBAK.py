from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def products_main(chromeBrowser):

    chromeBrowser.get('https://admin-dev.goopter.com/products')
    #products_link = chromeBrowser.find_element(By.XPATH, '//*[@id="root"]/div/section/section/aside[2]/div/div/div[2]/ul/li[6]/span[2]/a')
    #products_link.click()

def products_searchbox_type(chromeBrowser):

    searchbox = chromeBrowser.find_element(By.XPATH, '/html/body/div[1]/div/section/section/main/div[2]/div/div[1]/div[1]/div[1]/span/input')
    sleep(1)
    searchbox.send_keys('tea')
    
def products_threedots(chromeBrowser):
    #threedots = chromeBrowser.find_element(By.TAG_NAME, 'svg').click()
    
    print('trying threedots..')
    sleep(1)
    #threedots = chromeBrowser.find_element(By.XPATH, '//*[contains(., "M6")]')     # view/edit page
    #threedots=chromeBrowser.find_element(By.XPATH, '/html/body/div[1]/div/section/section/main/div[2]/div/div[2]/div/div/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[9]/div/div/button[2]')
    #threedots= chromeBrowser.find_element(By.CSS_SELECTOR, "svg[fill='currentColor']")    #dashboard page
    #threedots= chromeBrowser.find_element(By.CSS_SELECTOR, "svg[xmlns='http://www.w3.org/2000/svg']")    #dashboard page
    
    
    
    action = ActionChains(chromeBrowser)
    #//*[@id="products-table-container"]/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[9]/div/div/button[2]
    
    threedots = chromeBrowser.find_element(By.XPATH,'//*[@id="products-table-container"]/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[10]/div/div/button[2]')
    #threedots= chromeBrowser.find_element(By.XPATH, '/html/body/div[1]/div/section/section/main/div[2]/div/div[2]/div/div/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[9]/div/div/button[2]')
    #action.move_to_element_with_offset(threedots,0,0).context_click().perform()  #right click
    action.move_to_element(threedots).perform()
    
    
    sleep(10)
    # menu = chromeBrowser.find_element(By.XPATH, '')
    # action.move_to_element(menu).perform()
    # sleep(1)
    # threedots.find_element(By.XPATH, '')
    # threedots.find_element(By.LINK_TEXT, 'Delete').click()
    threedots.find_element(By.XPATH, '//p[contains(.,"Delete")]').click()
    # By.XPATH, '//*[contains(., "Log out")]'
    #threedots.click()
    #input()
    #threedots.find_element(By.LINK_TEXT, 'Description')
    #action.click().perform()
    #action.move_to_element(threedots).click()
    #threedots.click()
    
    sleep(1)
    
    #threedots.find_element(By.LINK_TEXT,'danger').click()
    #selection = chromeBrowser.find_element(By.XPATH, '/html/body/div[73]/div/div/div/div[2]/div/div/p[5]')
    
    #action.move_to_element(chromeBrowser.find_element(By.XPATH,'//*[contains(.,"danger")]')).click()
   # input()
    sleep(1) 
    answer=input('Delete ok?')
    if answer=='yes':
        threedots.find_element(By.XPATH, '//span[contains(.,"OK")]').click()
    else:
        threedots.find_element(By.XPATH, '//span[contains(.,"Cancel")]').click()
        
    
    #threedots.click()
    ##threedots.find_element(By.CLASS_NAME,'popover-item.danger.mb-1').click()
    #find_element(By.XPATH, '//*[contains(., "Log out")]')  #body > div:nth-child(57) > div > div > div > div.ant-popover-inner > div > div > p.popover-item.danger.m
    
    
   
    (By.XPATH, "//div[@class='order-list-title-end-section']//*[name()='svg']")
    
    from selectorshub