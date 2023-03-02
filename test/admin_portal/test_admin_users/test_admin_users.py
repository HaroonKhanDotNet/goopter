from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import json

import pytest
@pytest.fixture(scope='module')
def browser():
    #ec.
    #options = Options()
    #options.add_argument('--headless=new')
    #chromeBrowser = webdriver.Chrome(options=options)
    chromeBrowser = webdriver.Chrome()
    chromeBrowser.maximize_window()
    exp_wait = WebDriverWait(chromeBrowser, timeout=10)
    #chromeBrowser.implicitly_wait(10)

    goopter_file = open('data/goopter.json', 'r')
    gc = json.load(goopter_file)

    #chromeBrowser.get('https://admin-dev.goopter.com/')
    chromeBrowser.get( gc['goopter-login']['goopter-url'] )
    chromeBrowser.find_element( By.NAME, gc['goopter-login']['username'][1]).send_keys(gc['goopter-login']['username'][2])
    chromeBrowser.find_element(By.NAME, 'password').send_keys('20230130')
    chromeBrowser.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/form/div/div[3]/div/div/div/button').click()

    # //li[2])
    # //li[@role='menuitem'])[14]
    # //*[@id="root"]/div/section/section/aside[2]/div/div/div[2]/ul/li[14]
    # wait.until(lambda d: d.find_element(By.XPATH, '//li[14]')).click()
    exp_wait.until(ec.element_to_be_clickable((By.XPATH, '//li[14]'))).click()

    yield chromeBrowser

    # todo: need to perform logout automation
    chromeBrowser.quit()


def test_add_admin(browser):

    new_user_link = browser.find_element(
        By.XPATH, '/html/body/div[1]/div/section/section/main/div[2]/div/div[2]/div[2]/button')
    new_user_link.click()

    # Fill in the fields to create a new user
    username_field = browser.find_element(
        By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/input')
    username_field.send_keys('newadmin')
    password_field = browser.find_element(
        By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div[5]/div[2]/div[2]/input')
    password_field.send_keys('newpassword123')
    firstname_field = browser.find_element(
        By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div[4]/div[1]/input')
    firstname_field.send_keys('test')
    lastname_field = browser.find_element(
        By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div[4]/div[2]/input')
    lastname_field.send_keys('name')
    submit_button = browser.find_element(
        By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[1]/button')
    submit_button.click()
