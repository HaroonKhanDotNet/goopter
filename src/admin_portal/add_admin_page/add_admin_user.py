from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://admin-dev.goopter.com/adminUsers")

def add_Admin():

    #Navigate to add admin user tab
    new_user_link = driver.find_element(By.XPATH, '/html/body/div[1]/div/section/section/main/div[2]/div/div[2]/div[2]/button')
    new_user_link.click()

    # Fill in the fields to create a new user
    username_field = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/input')
    username_field.send_keys('newadmin')
    password_field = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div[5]/div[2]/div[2]/input')
    password_field.send_keys('newpassword123')
    firstname_field = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div[4]/div[1]/input')
    firstname_field.send_keys('test')
    lastname_field = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div[4]/div[2]/input')
    lastname_field.send_keys('name')
    submit_button =driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[1]/button')
    submit_button.click()

    # Close the browser window

    driver.quit()