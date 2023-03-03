import time
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

def settings_main(chromeBrowser):
    element_settings_page = chromeBrowser.find_element(By.XPATH, "/html/body/div/div/section/section/aside[2]/div/div/div[2]/ul/li[16]/span[2]")
    element_settings_page.click()
    
def settings_public_notice_edit(chromeBrowser):
    element_edit_btn = chromeBrowser.find_element(By.XPATH, "/html/body/div/div/section/section/main/div[2]/div[2]/div[3]/div[3]/div[2]")
    element_edit_btn.click()

def settings_public_notice_add(chromeBrowser):
    element_add_btn = chromeBrowser.find_element(By.XPATH, "//button[normalize-space()='Add']")
    element_add_btn.click()

def settings_public_notice_drop_down(chromeBrowser):
    element_drop_down = chromeBrowser.find_element(By.XPATH, "//body[1]/div[1]/div[1]/section[1]/section[1]/main[1]/div[2]/div[1]/div[6]/div[1]")
    element_drop_down.click()

def settings_public_notice_pick_up(chromeBrowser):
    element_pick_up = chromeBrowser.find_element(By.XPATH,"//div[contains(@class,'ant-select-item ant-select-item-option ant-select-item-option-active')]//div[contains(@class,'ant-select-item-option-content')][normalize-space()='Pick Up']") 
    element_pick_up.click()
    time.sleep(2)
    element_add_btn = chromeBrowser.find_element(By.XPATH,"//button[normalize-space()='Add']")
    element_add_btn.click()