from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def GiftCard_main(chromeBrowser):
      chromeBrowser.get('https://admin-dev.goopter.com/giftCards')


def giftcard_link(chromeBrowser):     
        giftcard_link = chromeBrowser.find_element(By.XPATH, "//li[9]")
        giftcard_link.click()
        
def three_dots_link(chromerBrowser):   
       three_dots = chromerBrowser.find_element(By.XPATH,"//div[4]//div[7]//div[1]//label[1]")
       ActionChains(chromerBrowser).move_to_element(three_dots).perform()


def Delete(chromeBrowser):
      Delete_dots= chromeBrowser.find_element(By.XPATH,"//span[normalize-space()='Delete']").click()
      
def confirmation(chromeBrowser):
      ok_messege = chromeBrowser.find_element(By.XPATH,"//span[normalize-space()='OK']")
      ActionChains(chromeBrowser).move_to_element(ok_messege).perform()
      
def filter_link(chromerBrowser):   
      filter_link =  chromerBrowser.find_element(By.XPATH,"//button[@class='ant-btn ant-btn-default ant-btn-lg filter-button']")
      filter_link().click

def filter_txt(chromeBrowser):
      txt = chromeBrowser.find_element(By.XPATH, "//input[@id='product_name']").click()

def SKU_filter(chromeBrowser):
      Sku = chromeBrowser.find_element(By.XPATH, "//input[@id='product_sku']").click()


   
def switch_link(chromeBrowser):
     switch_link =  chromeBrowser.find_element(By.XPATH,"//div[3]//div[6]//div[1]//button[1]")
     switch_link().click
