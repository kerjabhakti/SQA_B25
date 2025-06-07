from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

driver.get("https://syncro.herobuxx.me/signup/")

username_input = driver.find_element(By.ID, "username")
username_input.send_keys("testuser123")

submit_one = driver.find_element(By.ID, "submitone")
submit_one.click()

WebDriverWait(driver, 10).until(
    EC.invisibility_of_element_located((By.ID, "stepone"))
)
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "steptwo"))
)

passkey_input = driver.find_element(By.ID, "passkey")
passkey_confirm_input = driver.find_element(By.ID, "passkey-confirm")

passkey_input.send_keys("Password1!")
passkey_confirm_input.send_keys("Password1!")

submittwo = driver.find_element(By.ID, "submittwo")
driver.execute_script("arguments[0].scrollIntoView(true);", submittwo)
submittwo.click()