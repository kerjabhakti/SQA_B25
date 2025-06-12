from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException
import time


driver = webdriver.Chrome()

driver.get("https://jul003.github.io/Fe_Tb/Login.html")
time.sleep(2)

assert "Document" in driver.page_source
print("✅ Halaman Login Berhasil Dibuka")


username_field = driver.find_element(By.NAME, "email")
username_field.send_keys("dzulkiflifaiz11@gmail.com")

password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("ganteng")
password_field.send_keys(Keys.RETURN)

time.sleep(2)


try:
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(f"⚠️ Alert muncul: {alert_text}")
    
    if "Selamat datang" in alert_text:
        print("✅ Login berhasil")
    else:
        print("❌ Login gagal")
    alert.accept()
except NoAlertPresentException:
    print("⚠️ Tidak ada alert muncul")

time.sleep(2)


if "https://jul003.github.io/Fe_Tb/data.html" in driver.current_url:
    print("✅ Berhasil diarahkan ke halaman dashboard")
else:
    print("❌ Gagal diarahkan ke dashboard")

time.sleep(2)
driver.quit()
