from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException, TimeoutException
import time

driver = webdriver.Firefox()

try:
    driver.get("https://syncroapp.github.io/login/")
    
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "username")))
    driver.find_element(By.ID, "username").send_keys("testuser123") 
    driver.find_element(By.ID, "submitone").click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "passkey")))
    time.sleep(0.5)  
    driver.find_element(By.ID, "passkey").send_keys("TestPass@1234")
    driver.find_element(By.ID, "submittwo").click()

    time.sleep(2)

    try:
        alert = driver.switch_to.alert
        print(f"[!] ALERT: {alert.text}")
        alert.accept()
    except:
        print("[✓] No alert detected after login.")

    if "Desk" in driver.current_url:
        print("[✓] Login successful, redirected to dashboard.")
    else:
        print("[!] Login may have failed or no redirect occurred.")

except UnexpectedAlertPresentException as e:
    print(f"[!] Unexpected Alert: {e.alert_text}")
    driver.switch_to.alert.accept()

except TimeoutException:
    print("[✗] Timeout waiting for elements.")

finally:
    time.sleep(2)
    driver.quit()