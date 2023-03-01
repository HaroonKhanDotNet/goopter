from selenium import webdriverfrom 
selenium.common.exceptions 
import NoSuchElementException, WebDriverExceptionfrom 
from selenium.webdriver.common.by import By 
import logging
logging.basicConfig (filename='logs/login_page.log',  encoding='utf-8', level=logging.INFO, format='%(levelname)s %(asctime)s - %(message)s',  datefmt='%m/%d/%Y %I:%M:%S %p')
firefox = webdriver.Firefox()
logging.info("Maximizing: Firefox Bowser Window ...")
firefox.maximize_window()
logging.info("Maximized: Firefox Bowser Window ...")
logging.info("Loading:https://admin-dev.goopter.com/")
# * this will try to access the login webpage three time
pingCounter = 0
while pingCounter < 3: 
    try: firefox.get('https://admin-dev.goopterdfg.com/')
    # todo: we need to move all the page testing code here 
    break 
except WebDriverException as ex: 
    logging.error(f'pingCounter={pingCounter} {ex.msg}') 
    pingCounter = pingCounter + 1 
    if pingCounter == 3: 
        logging.critical('Login Page is inaccessible')

logging.info("Loaded: https://admin-dev.goopter.com/")
logging.warning('Try: Entering ...')
try: 
    logging.warning('Assert: Comparing the Page Title') 
    assert firefox.title == 'Goopter Business Porta'
except AssertionError: 
    logging.error('Asser: Fail to match Title ...') 
    print("Title doesn't match")

try: 
    id = firefox.find_element(By.ID, 'anyID')
except NoSuchElementException: 
    logging.error("firefox.find_element(By.ID, 'anyID')")
    logging.info('Try: Passed')
    f = open('pg.txt', 'w')
    f.write( firefox.page_source.replace('\n', '') )
    f.close()logging.info('Closing: Browser')
