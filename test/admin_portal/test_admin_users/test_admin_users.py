from selenium import webdriver
from selenium.webdriver.common.by import By

chromeBrowser = None

def setup_module():
    global chromeBrowser
    chromeBrowser = webdriver.Chrome()
    chromeBrowser.implicitly_wait(10)
    admin_login()


def admin_login():

    chromeBrowser.get('https://admin-dev.goopter.com/')

    userName_txt = chromeBrowser.find_element(By.NAME, 'username')
    userName_txt.send_keys('haroondev')

    password_txt = chromeBrowser.find_element(By.NAME, 'password')
    password_txt.send_keys('20230130')

    login_btn = chromeBrowser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/form/div/div[3]/div/div/div/button')
    login_btn.click()


def test_add_admin():
    
    #Navigate to add admin user tab
    chromeBrowser.get("https://admin-dev.goopter.com/adminUsers")
    new_user_link = chromeBrowser.find_element(By.XPATH, '/html/body/div[1]/div/section/section/main/div[2]/div/div[2]/div[2]/button')
    new_user_link.click()

    # Fill in the fields to create a new user
    username_field = chromeBrowser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/input')
    username_field.send_keys('newadmin')
    password_field = chromeBrowser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div[5]/div[2]/div[2]/input')
    password_field.send_keys('newpassword123')
    firstname_field = chromeBrowser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div[4]/div[1]/input')
    firstname_field.send_keys('test')
    lastname_field = chromeBrowser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div[4]/div[2]/input')
    lastname_field.send_keys('name')
    submit_button =chromeBrowser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[1]/button')
    submit_button.click()


def teardown_module():
    chromeBrowser.quit()