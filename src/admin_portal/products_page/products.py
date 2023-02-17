from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

def products_main(chromeBrowser):

    chromeBrowser.get('https://admin-dev.goopter.com/products')
    

def products_searchbox_type(chromeBrowser):
    sleep(2)
    searchbox = chromeBrowser.find_element(By.XPATH, '/html/body/div[1]/div/section/section/main/div[2]/div/div[1]/div[1]/div[1]/span/input')
    sleep(1)
    searchbox.send_keys('tea')
    
def products_threedots(chromeBrowser):
    
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
    sleep(10)
    
    
    # Short
    chromeBrowser.get('https://admin-dev.goopter.com/products')
    sleep(10)
    threedots = chromeBrowser.find_element(By.XPATH,'//*[@id="products-table-container"]/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[10]/div/div/button[2]')
    
    action.move_to_element(threedots).perform()
    
    sleep(1)
    
    threedots.find_element(By.XPATH, '//p[contains(.,"Short Description")]').click()
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
    sleep(10)
    
def products_sharing(chromeBrowser):
        
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
    
# via email
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


       
    
    
    
    
    
    

# 
        
        