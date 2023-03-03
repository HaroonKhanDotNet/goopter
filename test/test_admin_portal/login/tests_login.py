from selenium import webdriver
from selenium.webdriver.common.by import By

import pytest

#chromeBrowser = None

# def setup_module():

#     global chromeBrowser
#     chromeBrowser = webdriver.Chrome()
#     chromeBrowser.get('https://admin-dev.goopter.com/')

#     chromeBrowser.find_element(By.NAME, 'username').send_keys('haroondev')
#     chromeBrowser.find_element(By.NAME, 'password').send_keys('20230130')
#     chromeBrowser.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/form/div/div[3]/div/div/div/button').click()
#     input()

#def teardown_module():

#    # todo: we need to perform logout
#    chromeBrowser.quit()

# * pytest recommends fixture to perform setup/teardown

@pytest.fixture(scope='module')
def browser():

    print('setup')
    yield
    print('teardown')


def test_admin_login(browser):
    print('Inside test')