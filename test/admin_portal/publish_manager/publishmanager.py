import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def publishmanager_main(chromeBrowser):
    click_publishmanager = chromeBrowser.find_element(By.XPATH, "/html/body/div/div/section/section/aside[2]/div/div/div[2]/ul/li[8]/span[2]")
    click_publishmanager.click()
    time.sleep(3)

def publishmanager_unpublish(chromeBrowser):
    unpublish_btn = chromeBrowser.find_element(By.XPATH, "/html/body/div/div/section/section/main/div[2]/div[2]/button[1]")
    unpublish_btn.click()
    time.sleep(3)

def publishmanager_republish(chromeBrowser):
    republish_btn = chromeBrowser.find_element(By.XPATH, "/html/body/div/div/section/section/main/div[2]/div[2]/button[2]")
    republish_btn.click()
    time.sleep(3)

def publishmanager_sync(chromeBrowser):
    sync_btn = chromeBrowser.find_element(By.XPATH, "/html/body/div/div/section/section/main/div[1]/div[2]/span/div/div[1]/div[1]")
    sync_btn.click()
    time.sleep(3)
    sync_confirm_btn = chromeBrowser.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[2]/button[2]/span")
    sync_confirm_btn.click()
    time.sleep(3)
