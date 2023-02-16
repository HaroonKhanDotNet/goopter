
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def products_main(chromeBrowser):

    liveOrders_ele = chromeBrowser.find_element(By.XPATH, "//li[6]").click()
    products_link.click()

def products_searchbox_type(chromeBrowser):

    searchbox = chromeBrowser.find_element(By.XPATH, '/html/body/div[1]/div/section/section/main/div[2]/div/div[1]/div[1]/div[1]/span/input')
    searchbox.send_keys('bubble')

def ant_btn_popup(chromeBrowser):

    dots_popup_menu = chromeBrowser.find_element(By.XPATH, '//*[@id="products-table-container"]/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[10]/div/div/button[2]')
    
    #pointer_actions mouse = new pointer_actions(chromeBrowser)

    ActionChains(chromeBrowser).move_to_element(dots_popup_menu).perform()
