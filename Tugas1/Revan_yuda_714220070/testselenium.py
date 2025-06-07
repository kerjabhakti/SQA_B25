from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://revan232.github.io/Projectv1/pages/login.html")
time.sleep(2)

driver.find_element(By.ID, "loginUsername").send_keys("admin")
driver.find_element(By.ID, "loginPassword").send_keys("password123")
driver.find_element(By.ID, "login-btn").click()

time.sleep(3) 

driver.quit()
