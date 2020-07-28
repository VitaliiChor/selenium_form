# Open https://the-internet.herokuapp.com/login

# Please automate next test cases:
# 1. Login with valid creds (tomsmith/SuperSecretPassword!) and assert you successfully logged in
# 2. Login with invalid creds and check validation error
# 3. Logout from app and assert you successfully logged out
from selenium import webdriver
import time

DATA1 = {
        'username': 'tomsmith',
        'password': 'SuperSecretPassword!'
    }

DATA2 = {
        'username': 'toms',
        'password': '1234567890qwe'
    }

driver = webdriver.Chrome(executable_path="C:/Users/USER/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/login")

driver.find_element_by_id("username").send_keys(DATA1['username'])
driver.find_element_by_id("password").send_keys(DATA1['password'])
driver.find_element_by_css_selector("#login > button").click()
time.sleep(3)

assert "You logged into a secure area!" in driver.page_source
driver.quit()

driver = webdriver.Chrome(executable_path="C:/Users/USER/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/login")

driver.find_element_by_id("username").send_keys(DATA2['username'])
driver.find_element_by_id("password").send_keys(DATA2['password'])
driver.find_element_by_css_selector("#login > button").click()
time.sleep(3)

assert "Your username is invalid!" in driver.page_source
driver.quit()