from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import logging

logging.basicConfig(format='%(levelname)s - %(asctime)s - %(message)s', 
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    filename='logs/login_page.log', 
                    encoding='utf-8',
                    level = logging.INFO)



chromeBrowser = webdriver.Chrome()
logging.info("Maximizing: Chrome Browser Window...")
chromeBrowser.maximize_window()
logging.info("Maximized: Chrome Browser Window...")
logging.info("Loading: https://admin-dev.goopter.com/")

#* this will try to access 
pingCounter = 0
while pingCounter < 2: 
    try:
        chromeBrowser.get('https://admin-dev.goopterdfg.com/')
    except WebDriverException as ex:
        logging.critical(f'PingCounter={pingCounter} {ex.msg}')
        pingCounter = pingCounter + 1
 
logging.info("Loaded: https://admin-dev.goopter.com/")
logging.warning("Try: Entering ...")

try:
    logging.warning("Assert: Comparing the Page Title")
    assert chromeBrowser.title == 'Goopter Business Porta'

except AssertionError:
    logging.error("Assert: Fail to match title...")
    print("Title doesn't match")

try: 
    id = chromeBrowser.find_element(By.ID, 'anyID')

except NoSuchElementException:     
    logging.error("chromeBrowser.find_element(By.ID, 'anyID')")

logging.info('Try: Passed')

f = open('pg.txt', 'w')
f.write(chromeBrowser.page_source.replace('\n', ''))
logging.info("Closing Browser")
chromeBrowser.quit
logging.info("Closed Browser")
