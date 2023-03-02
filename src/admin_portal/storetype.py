import time 
from selenium import webdriver 
from selenium.webdriver.common.by import By

#PATH = "C:\Program Files (x86)\chromedriver.exe"


driver=webdriver.Chrome()

driver.maximize_window()
driver.get('https://admin-dev.goopter.com/')

#login

username_text = driver.find_element(By.NAME, 'username')
username_text.send_keys('devnav')

password_text = driver.find_element(By.NAME, 'password')
password_text.send_keys('230130')

login_btn = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/form/div/div[3]/div/div/div/button')
login_btn.click()

time.sleep(3)

#sidebar element

element = driver.find_element(By.XPATH,"/html/body/div[1]/div/section/section/aside[2]/div/div/div[2]/ul/li[16]/span[2]")
element.click()

time.sleep(2)

editbtn = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div[2]/div[2]/div[1]/div[3]/div[2]")
editbtn.click()

time.sleep(2)

typestore = driver.find_element(By.XPATH, '/html/body/div[1]/div/section/section/main/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div')
typestore.click()

time.sleep(2)

drop = driver.find_element(By.XPATH, '/html/body/div[1]/div/section/section/main/div[2]/div/div[2]/div[2]/div/div[2]/div/form/div[1]/div[2]/table/tbody/tr/td/span/div/div/div/div/div/div')
drop.click()

time.sleep(2)

category = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div[2]/div[1]/div/div/div[3]')
category.click()

time.sleep(2)

driver.quit()