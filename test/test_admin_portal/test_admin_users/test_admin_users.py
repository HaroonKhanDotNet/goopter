from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

class TestAdminUsers:

    def test_add_admin(self, browser: Chrome, admin_users):

        # new_user_link
        browser.find_element(
            By.XPATH, '/html/body/div[1]/div/section/section/main/div[2]/div/div[2]/div[2]/button').click()

        # Filling in the fields to create a new user

        # username_field
        browser.find_element(
            By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/input').send_keys('newadmin')

        # password_field
        browser.find_element(
            By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div[5]/div[2]/div[2]/input').send_keys('newpassword123')

        # firstname_field
        browser.find_element(
            By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div[4]/div[1]/input').send_keys('test')

        # lastname_field
        browser.find_element(
            By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div[4]/div[2]/input').send_keys('name')

        # submit_button
        browser.find_element(
            By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[1]/button').click()
