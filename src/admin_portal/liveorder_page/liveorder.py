import time
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

#


def liveorder_main(chromeBrowser):
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
    element_complete = chromeBrowser.find_element(
        By.XPATH, "//span[normalize-space()='Complete']")
    element_complete.click()
    element_ok = chromeBrowser.find_element(
        By.XPATH, "//body[1]/div[4]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/button[2]/b[1]")
    element_ok.click()


def liveorder_quick_action_cancel_order(chromeBrowser):
    element_cancel_order = chromeBrowser.find_element(
        By.XPATH, "//span[normalize-space()='Cancel Order']")
    element_cancel_order.click()
    element_reject_order = chromeBrowser.find_element(
        By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div[3]/button[2]/span")
    element_reject_order.click()


def liveorder_quick_action_update_payment_cash(chromeBrowser):
    element_update_payment = chromeBrowser.find_element(
        By.XPATH, "//span[normalize-space()='Update Payment']")
    element_update_payment.click()
    time.sleep(2)
    element_cash = chromeBrowser.find_element(
        By.XPATH, "//span[normalize-space()='Cash']")
    element_cash.click()
    time.sleep(2)
    element_ok = chromeBrowser.find_element(
        By.XPATH, "//span[normalize-space()='OK']")
    element_ok.click()


def liveorder_quick_action_update_payment_card(chromeBrowser):
    element_update_payment = chromeBrowser.find_element(
        By.XPATH, "//span[normalize-space()='Update Payment']")
    element_update_payment.click()
    time.sleep(2)
    element_card_payment = chromeBrowser.find_element(
        By.XPATH, "//span[normalize-space()='Card Payment (in person)']")
    element_card_payment.click()
    time.sleep(2)
    element_ok = chromeBrowser.find_element(
        By.XPATH, "//span[normalize-space()='OK']")
    element_ok.click()


def liveorder_quick_action_update_payment_wechat(chromeBrowser):
    element_update_payment = chromeBrowser.find_element(
        By.XPATH, "//span[normalize-space()='Update Payment']")
    element_update_payment.click()
    element_wechat = chromeBrowser.find_element(
        By.XPATH, "//span[normalize-space()='Wechat Pay']")
    element_wechat.click()
    time.sleep(3)
    element_ok = chromeBrowser.find_element(
        By.XPATH, "//span[normalize-space()='OK']")
    element_ok.click()


def liveorder_quick_action_update_payment_alipay(chromeBrowser):
    element_update_payment = chromeBrowser.find_element(
        By.XPATH, "//span[normalize-space()='Update Payment']")
    element_update_payment.click()
    element_alipay = chromeBrowser.find_element(
        By.XPATH, "//span[normalize-space()='Alipay']")
    element_alipay.click()
    time.sleep(3)
    element_ok = chromeBrowser.find_element(
        By.XPATH, "/html/body/div[5]/div/div[2]/div/div[2]/div/div/div[2]/button[2]/span")
    element_ok.click()


def liveorder_quick_action_update_payment_union(chromeBrowser):
    element_update_payment = chromeBrowser.find_element(
        By.XPATH, "//span[normalize-space()='Update Payment']")
    element_update_payment.click()
    element_union = chromeBrowser.find_element(
        By.XPATH, "//span[normalize-space()='Union Pay']")
    element_union.click()
    time.sleep(3)
    element_ok = chromeBrowser.find_element(
        By.XPATH, "//span[normalize-space()='OK']")
    element_ok.click()


def liveorder_copy_customer_name(chromeBrowser):
    element_copy_customer_name = chromeBrowser.find_element(
        By.XPATH, "//div[@class='recent-order-first-row'][normalize-space()='QA Customer']//span[@aria-label='copy']")
    hover = ActionChains(chromeBrowser).move_to_element(
        element_copy_customer_name)
    hover.perform()
    time.sleep(3)
    click_copy = ActionChains(chromeBrowser)
    element_click_copy = chromeBrowser.find_element(
        By.XPATH, "//div[@class='recent-order-first-row'][normalize-space()='QA Customer']//span[@aria-label='copy']")
    click_copy.double_click(element_click_copy).perform()


def liveorder_copy_customer_phone_number(chromeBrowser):
    element_phone_number = chromeBrowser.find_element(
        By.XPATH, "//div[@class='phone-row content-sec-row-col-content']")
    click_copy = chromeBrowser.find_element(
        By.XPATH, "//div[@class='phone-row content-sec-row-col-content']//span[@aria-label='copy']//*[name()='svg']//*[name()='path' and contains(@d,'M832 64H29')]")
    hover = ActionChains(chromeBrowser).move_to_element(element_phone_number)
    hover.perform()
    time.sleep(3)
    copy_phone_number = ActionChains(chromeBrowser)
    copy_phone_number.double_click(click_copy).perform()


def liveorder_display_item_detail_page(chromeBrowser):
    element_display_detail_page = chromeBrowser.find_element(
        By.XPATH, "//div[@class='item-name-link-container']//a//*[name()='svg']")
    element_display_detail_page.click()


def liveorder_add_comment(chromeBrowser):
    element_add_comment = chromeBrowser.find_element(
        By.XPATH, "//div[@class='add-comment-button-text']")
    element_add_comment.click()
    time.sleep(2)
    element_input_txt = chromeBrowser.find_element(
        By.XPATH, "//textarea[@class='ant-input']")
    element_input_txt.send_keys('Testing')
    time.sleep(2)
    element_submit_btn = chromeBrowser.find_element(
        By.XPATH, "//button[normalize-space()='Submit']")
    element_submit_btn.click()


def liveorder_display_order_history(chromeBrowser):
    element_order_history_btn = chromeBrowser.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[4]/div[1]/div[2]/div[2]")
    element_order_history_btn.click()
    time.sleep(2)
    scroll_down = ActionChains(chromeBrowser)
    element_order_history_detail = chromeBrowser.find_element(By.XPATH, "//div[@class='message']")
    scroll_down.move_to_element(element_order_history_detail).perform()

def liveorder_display_address_on_map(chromeBrowser):
    element_address_btn = chromeBrowser.find_element(By.XPATH, "//div[contains(@class,'border-bottom content-sec-row')]//span[2]")
    element_address_btn.click()

#prereq-must have a preparing delivery order
def liveorder_change_pick_up_time(chromeBrowser):
    element_delivery_order = chromeBrowser.find_element(By.XPATH, "/html/body/div/div/section/section/main/div[2]/div/div/div/div/div/div[2]/div[1]/div/div/div[3]/div[2]/div[2]/div/div/div[2]")
    element_delivery_order.click()
    time.sleep(2)
    element_est_delivery_btn  = chromeBrowser.find_element(By.XPATH, "//body[1]/div[1]/div[1]/section[1]/section[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]")
    element_est_delivery_btn.click()
    time.sleep(2)
    element_pick_up_time_change_btn = chromeBrowser.find_element(By.XPATH, "//body[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/button[2]/span[1]/div[1]")
    element_pick_up_time_change_btn.click()
    time.sleep(2)
    element_confirm_btn = chromeBrowser.find_element(By.XPATH, "//body[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/button[1]")
    element_confirm_btn.click()

def liveorder_change_commute_time(chromeBrowser):
    element_delivery_order = chromeBrowser.find_element(By.XPATH, "/html/body/div/div/section/section/main/div[2]/div/div/div/div/div/div[2]/div[1]/div/div/div[3]/div[2]/div[2]/div/div/div[2]")
    element_delivery_order.click()
    time.sleep(2)
    element_est_delivery_btn  = chromeBrowser.find_element(By.XPATH, "//body[1]/div[1]/div[1]/section[1]/section[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]")
    element_est_delivery_btn.click()
    time.sleep(2)
    element_commute_time_change_btn = chromeBrowser.find_element(By.XPATH, "//body[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[4]/button[1]/span[1]")
    element_commute_time_change_btn.click()
    time.sleep(2)
    element_confirm_btn = chromeBrowser.find_element(By.XPATH, "//body[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/button[1]")
    element_confirm_btn.click()

#prereq-must have a new/pending delivery order 
def liveorder_accept_delivery_order(chromeBrowser):
    element_accept_btn = chromeBrowser.find_element(By.XPATH,"//body[1]/div[1]/div[1]/section[1]/section[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]")
    element_accept_btn.click()
    time.sleep(2)
    element_confirm_btn = chromeBrowser.find_element(By.XPATH, "//div[contains(@class,'ant-modal-footer')]//div[2]")
    element_confirm_btn.click()

def liveorder_ready_for_delivery(chromeBrowser):
    element_ready_for_delivery_btn = chromeBrowser.find_element( By.XPATH, "//div[contains(@class,'order-list-list-style-control-panel')]//div[contains(@class,'ant-row content-head-col-processing-buttons')]//div[1]")
    element_ready_for_delivery_btn.click()
    time.sleep(2)
    element_confirm_btn = chromeBrowser.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[2]/button[2]")
    element_confirm_btn.click()

def liverorder_start_delivery(chromeBrowser):
    element_start_delivery_btn = chromeBrowser.find_element(By.XPATH, "/html/body/div/div/section/section/main/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]")
    element_start_delivery_btn.click()
    time.sleep(2)
    element_confirm_btn = chromeBrowser.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[2]/button[2]")
    element_confirm_btn.click()
