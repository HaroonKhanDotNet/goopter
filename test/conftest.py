from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from selenium.webdriver.chrome.options import Options

import json

import pytest

@pytest.fixture(scope='session')
def browser():
    #ec.
    #options = Options()
    #options.add_argument('--headless=new')
    #chromeBrowser = webdriver.Chrome(options=options)
    chromeBrowser = Chrome()
    chromeBrowser.maximize_window()
    chromeBrowser.implicitly_wait(10)

    goopter_file = open('data/goopter.json', 'r')
    gc = json.load(goopter_file)

    #chromeBrowser.get('https://admin-dev.goopter.com/')
    chromeBrowser.get( gc['goopter-login']['goopter-url'] )
    chromeBrowser.find_element(By.NAME, gc['goopter-login']['username'][1]).send_keys(gc['goopter-login']['username'][2])
    chromeBrowser.find_element(By.NAME, 'password').send_keys('20230130')
    chromeBrowser.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/form/div/div[3]/div/div/div/button').click()

    yield chromeBrowser

    #sign out
    selection=chromeBrowser.find_element(By.XPATH,"//span[contains(text(),'Goopter')]")
    selection.find_element(By.XPATH,"//span[normalize-space()='Sign Out']").click()
    chromeBrowser.quit()

@pytest.fixture(scope='class')
def admin_users(browser):
        #exp_wait = WebDriverWait(browser, timeout=10)

        # //li[14])
        # //li[@role='menuitem'])[14]
        # //*[@id="root"]/div/section/section/aside[2]/div/div/div[2]/ul/li[14]
        # exp_wait.until(lambda d: d.find_element(By.XPATH, '//li[14]')).click()
        # exp_wait.until(ec.element_to_be_clickable((By.XPATH, '//li[14]'))).click()
        browser.find_element(By.XPATH, '//li[14]').click()

@pytest.fixture(scope='class')
def products(browser):
        #exp_wait = WebDriverWait(browser, timeout=10)

        # //li[6])
        # //li[@role='menuitem'])[6]
        # //*[@id="root"]/div/section/section/aside[2]/div/div/div[2]/ul/li[6]
        # exp_wait.until(lambda d: d.find_element(By.XPATH, '//li[6]')).click()
        #exp_wait.until(ec.element_to_be_clickable((By.XPATH, '//li[6]'))).click()
        browser.find_element(By.XPATH, '//li[6]').click()

