from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.headless = False

driver = webdriver.Firefox(service=FirefoxService(), options=options)
driver.get("https://sc01100100.github.io/SaveCash/pages/signup.html")

driver.find_element("id", "name").send_keys("Test User")
driver.find_element("id", "email").send_keys("test@example.com") 
driver.find_element("id", "password").send_keys("TestPass@123")

submit_button = driver.find_element("css selector", "button[type='submit']")
submit_button.click()

try:
    alert_div = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#alert-container > div"))
    )
    print("Alert message shown:", alert_div.text)
except:
    print("No alert message detected")

time.sleep(3)
driver.quit()
