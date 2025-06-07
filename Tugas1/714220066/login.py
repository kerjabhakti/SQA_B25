from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Firefox()

try:

    driver.get("https://sc01100100.github.io/SaveCash/pages/signin.html")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))

    driver.find_element(By.ID, "email").send_keys("test@example.com")  # <-- Replace with valid email
    driver.find_element(By.ID, "password").send_keys("TestPass@123")  # <-- Replace with valid/invalid password

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    alert = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "alert-container"))
    )

    time.sleep(2)
    print("[INFO] Alert content:")
    print(alert.text.strip())

    if "home.html" in driver.current_url:
        print("[✓] Successfully logged in and redirected.")
    else:
        print("[!] No redirect occurred. Login may have failed.")

except Exception as e:
    print(f"[✗] Error occurred: {e}")
finally:
    time.sleep(3)
    driver.quit()
