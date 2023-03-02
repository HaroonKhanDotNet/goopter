from selenium import webdriver
# from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time

# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://admin-dev.goopter.com/')

# login
username_text = driver.find_element(By.NAME, 'username').send_keys('tomdev')
password_text = driver.find_element(By.NAME, 'password').send_keys('20230130')
driver.find_element(By.XPATH, "//button[text()='Login']").click()

time.sleep(3)

# From the left panel of Admin main page, click Settings
driver.find_element(By.XPATH, '//li[@class="ant-menu-item"][.//span/text()="Settings"]').click()

time.sleep(3)

# Choose General and click Edit button
driver.find_element(By.XPATH, '//div[@class="setting-card"][./div[@class="setting-card-title"]/text()="General"]').click()

time.sleep(3)

# Click the forth section 'Business Features'
# Because the 'Business Features' tab can be blocked by the 'Content Language' menu, JavaScript is used here
tab = driver.find_element(By.XPATH, '//div[@class="ant-tabs-tab"][./div[@class="ant-tabs-tab-btn"]/text()="Business Features"]')
driver.execute_script('arguments[0].click();', tab)

time.sleep(3)

# Set store features and restaurant extras
labels = driver.find_elements(By.XPATH, '//label[contains(@class, "ant-checkbox-wrapper")]')
for label in labels:
    if not label.find_element(By.CLASS_NAME, 'ant-checkbox-input').is_selected():
        label.click()

buttons = driver.find_elements(By.XPATH, '//form//button[contains(@class, "ant-switch")]')
for button in buttons:
    if button.get_attribute('aria-checked') == 'false':
        button.click()

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

driver.find_element(By.XPATH, '//tr[contains(th/span/text(),"Alcohol")]//div[contains(@class, "ant-select-single")]').click()
time.sleep(1)   # This wait is required
options = driver.find_elements(By.XPATH, '//div[div[@id="general-settings has-floating-submit_allow_alcohol_list"]]//div[@class="ant-select-item-option-content"]')
for option in options:
    if option.text == 'Full Bar':
        option.click()
        break

driver.find_element(By.XPATH, '//tr[contains(th/span/text(),"Noise Level")]//div[contains(@class, "ant-select-single")]').click()
time.sleep(1)   # This wait is required
options = driver.find_elements(By.XPATH, '//div[div[@id="general-settings has-floating-submit_noise_level_list"]]//div[@class="ant-select-item-option-content"]')
for option in options:
    if option.text == 'Quiet':
        option.click()
        break

driver.find_element(By.XPATH, '//tr[contains(th/span/text(),"Environment")]//div[contains(@class, "ant-select-single")]').click()
time.sleep(1)   # This wait is required
options = driver.find_elements(By.XPATH, '//div[div[@id="general-settings has-floating-submit_environment_list"]]//div[@class="ant-select-item-option-content"]')
for option in options:
    if option.text == 'Hipster':
        option.click()
        break

driver.find_element(By.XPATH, '//tr[contains(th/span/text(),"Attire")]//div[contains(@class, "ant-select-single")]').click()
time.sleep(1)   # This wait is required
options = driver.find_elements(By.XPATH, '//div[div[@id="general-settings has-floating-submit_attire_list"]]//div[@class="ant-select-item-option-content"]')
for option in options:
    if option.text == 'Dressy':
        option.click()
        break

time.sleep(3)

save_button = driver.find_element(By.XPATH, '//button[text()="Save Changes"]')
#save_button = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '.ant-btn.ant-btn-primary.ant-btn-lg.save-button-handler')))
#driver.execute_script('arguments[0].click();', save_button)
# driver.implicitly_wait(10)
#ActionChains(driver).move_to_element(save_button).click(save_button).perform()
#save_button.click()

time.sleep(3)

#alert = driver.find_element(By.XPATH, '//div[@role="alert"]/div/div[@style="color: black;"]')
#assert alert.text == 'Store Information Saved'

driver.quit()
