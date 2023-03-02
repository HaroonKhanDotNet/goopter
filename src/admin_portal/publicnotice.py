import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# PATH = "C:\Program Files (x86)\chromedriver.exe"


driver = webdriver.Chrome()

driver.maximize_window()
driver.get('https://admin-dev.goopter.com/')

# login

username_text = driver.find_element(By.NAME, 'username')
username_text.send_keys('devnav')

password_text = driver.find_element(By.NAME, 'password')
password_text.send_keys('230130')

login_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/form/div/div[3]/div/div/div/button')
login_btn.click()

time.sleep(3)

# sidebar element

element = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/aside[2]/div/div/div[2]/ul/li[16]/span[2]")
element.click()

time.sleep(2)

editbtn = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div[2]/div[2]/div[3]/div[3]")
editbtn.click()

time.sleep(2)

add = driver.find_element(By.XPATH, '/html/body/div[1]/div/section/section/main/div[2]/div/div[5]/button')
add.click()

time.sleep(2)

dropdown = driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/section[1]/section[1]/main[1]/div[2]/div[1]/div[6]/div[1]")
dropdown.click()

pickup = driver.find_element(By.XPATH,"//div[contains(@class,'ant-select-item ant-select-item-option ant-select-item-option-active')]//div[contains(@class,'ant-select-item-option-content')][normalize-space()='Pick Up']")
pickup.click()
time.sleep(2)

save = driver.find_element(By.XPATH,"/html/body/div[1]/div/section/section/main/div[2]/div/div[9]/button")
save.click()

time.sleep(4)

driver.quit()
