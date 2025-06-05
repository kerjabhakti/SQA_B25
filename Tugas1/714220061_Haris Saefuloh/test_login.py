from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://ramenkk.github.io/login/login.html")
time.sleep(2)

assert "Login" in driver.title
print("Accessing the login page...")

username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")

username.send_keys("irgi123")
password.send_keys("hahay123")

password.send_keys(Keys.RETURN)

if "Dashboard admin" in driver.title:
    print("Login successful!")
    input("Press Enter to exit...")
    time.sleep(3)
else:
    print("Login failed!")
    input("Press Enter to exit...")
driver.quit()