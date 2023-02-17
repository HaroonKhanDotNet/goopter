import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def liveorder_main(chromeBrowser):

    # WebDriverWait(chromeBrowser, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/section/section/aside[2]/div/div/div[2]/ul/li[2]/span[2]/span")))
    liveorder_btn = chromeBrowser.find_element(
        By.XPATH, "/html/body/div/div/section/section/aside[2]/div/div/div[2]/ul/li[2]")

    liveorder_btn.click()
    time.sleep(2)

def liveorder_export(chromeBrowser):
    liveorder_export_btn = chromeBrowser.find_element(By.CLASS_NAME, "order-list-export-order-icon")
    liveorder_export_btn.click()
    time.sleep(3)

    liveorder_export_confirm_btn =chromeBrowser.find_element(By.XPATH, "//b[normalize-space()='Export']")
    liveorder_export_confirm_btn.click()
    time.sleep(2)

def liverorder_search(chromeBrowser):
    liveorder_search_txt= chromeBrowser.find_element(By.XPATH, "//input[@placeholder='Search by name, phone or table number']")
    liveorder_search_txt.send_keys("Harry Potter")
    time.sleep(3)
