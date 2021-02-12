from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import os

#launch
url = "https://freebinancecoin.com"
timeout = 100
mail = 'shola6241@gmail.com'
key = 'Calvary_22#'

# create a new Firefox session
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
driver.get(url)

try:    
    element_present = EC.presence_of_element_located((By.CLASS_NAME, 'form-control'))
    WebDriverWait(driver, timeout).until(element_present)

    email = driver.find_element_by_xpath("//input[@name='email']")
    email.send_keys(mail)

    password = driver.find_element_by_xpath("//input[@name='password']")
    password.send_keys(key)

    driver.execute_script("document.getElementsByClassName('d-none d-lg-block')[0].firstElementChild.click()")

    signupbutton = driver.find_element_by_class_name('login')
    signupbutton.click()

except TimeoutException:
    pass# print("Error during login")
    

try:
    element_roll = EC.presence_of_element_located((By.CLASS_NAME, 'main-button-2'))
    WebDriverWait(driver, timeout).until(element_roll)
    roll = driver.find_element_by_class_name('main-button-2')
    roll.click()
except:
    pass# print('An error occured, while trying to click.')

driver.quit()