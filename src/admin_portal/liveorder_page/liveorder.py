import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


def liveorder_main(chromeBrowser):
    # WebDriverWait(chromeBrowser, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/section/section/aside[2]/div/div/div[2]/ul/li[2]/span[2]/span")))
    liveorder_btn = chromeBrowser.find_element(
        By.XPATH, "/html/body/div/div/section/section/aside[2]/div/div/div[2]/ul/li[2]")

    liveorder_btn.click()
    time.sleep(2)


def liveorder_export(chromeBrowser):
    liveorder_export_btn = chromeBrowser.find_element(
        By.CLASS_NAME, "order-list-export-order-icon")
    liveorder_export_btn.click()
    time.sleep(3)

    liveorder_export_confirm_btn = chromeBrowser.find_element(
        By.XPATH, "//b[normalize-space()='Export']")
    liveorder_export_confirm_btn.click()
    time.sleep(2)


def liverorder_search(chromeBrowser):
    liveorder_search_txt = chromeBrowser.find_element(
        By.XPATH, "//input[@placeholder='Search by name, phone or table number']")
    liveorder_search_txt.send_keys("Harry Potter")
    time.sleep(3)


def liverorder_quick_action(chromeBrowser):
    element_three_dot = chromeBrowser.find_element(
        By.XPATH, "/html/body/div[1]/div/section/section/main/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div/div/div[1]/div[2]/span[3] ")
    hover = ActionChains(chromeBrowser).move_to_element(element_three_dot)
    hover.perform()


def liveorder_quick_action_print(chromeBrowser):
    element_print = chromeBrowser.find_element(
        By.XPATH, "//span[normalize-space()='Print']")
    element_print.click()

def liveorder_quick_action_complete(chromeBrowser):
    element_complete = chromeBrowser.find_element(By.XPATH, "//span[normalize-space()='Complete']")
    element_complete.click()
    element_ok = chromeBrowser.find_element(By.XPATH, "//body[1]/div[4]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/button[2]/b[1]")
    element_ok.click()

def liveorder_quick_action_cancel_order(chromeBrowser):
    element_cancel_order = chromeBrowser.find_element(By.XPATH, "//span[normalize-space()='Cancel Order']")
    element_cancel_order.click()
    element_reject_order = chromeBrowser.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div[3]/button[2]/span")
    element_reject_order.click()

def liveorder_quick_action_update_payment_cash(chromeBrowser):
    element_update_payment = chromeBrowser.find_element(By.XPATH, "//span[normalize-space()='Update Payment']")
    element_update_payment.click()
    time.sleep(2)
    element_cash = chromeBrowser.find_element(By.XPATH, "//span[normalize-space()='Cash']")
    element_cash.click()
    time.sleep(2)
    element_ok = chromeBrowser.find_element(By.XPATH, "//span[normalize-space()='OK']")
    element_ok.click()

def liveorder_quick_action_update_payment_card(chromeBrowser):
    element_update_payment = chromeBrowser.find_element(By.XPATH, "//span[normalize-space()='Update Payment']")
    element_update_payment.click()
    time.sleep(2)
    element_card_payment = chromeBrowser.find_element(By.XPATH, "//span[normalize-space()='Card Payment (in person)']")
    element_card_payment.click()
    time.sleep(2)
    element_ok = chromeBrowser.find_element(By.XPATH, "//span[normalize-space()='OK']")
    element_ok.click()

def liveorder_quick_action_update_payment_wechat(chromeBrowser):
    element_update_payment = chromeBrowser.find_element(By.XPATH, "//span[normalize-space()='Update Payment']")
    element_update_payment.click()
    element_wechat = chromeBrowser.find_element(By.XPATH, "//span[normalize-space()='Wechat Pay']")
    element_wechat.click()
    time.sleep(3)
    element_ok = chromeBrowser.find_element(By.XPATH, "//span[normalize-space()='OK']")
    element_ok.click()


def liveorder_quick_action_update_payment_alipay(chromeBrowser):    
    element_update_payment = chromeBrowser.find_element(By.XPATH, "//span[normalize-space()='Update Payment']")
    element_update_payment.click()
    element_alipay = chromeBrowser.find_element(By.XPATH, "//span[normalize-space()='Alipay']")
    element_alipay.click()
    time.sleep(3)
    element_ok = chromeBrowser.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div/div[2]/div/div/div[2]/button[2]/span")
    element_ok.click()

def liveorder_quick_action_update_payment_union(chromeBrowser):
    element_update_payment = chromeBrowser.find_element(By.XPATH, "//span[normalize-space()='Update Payment']")
    element_update_payment.click()
    element_union = chromeBrowser.find_element(By.XPATH, "//span[normalize-space()='Union Pay']")
    element_union.click()
    time.sleep(3)
    element_ok = chromeBrowser.find_element(By.XPATH, "//span[normalize-space()='OK']")
    element_ok.click()
