from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()  

# 2. Buka halaman login
driver.get("https://zenith-infinity.github.io/zenverse-web/pages/signmenu.html") 
driver.maximize_window()

# 3. Isi form login
username_input = driver.find_element(By.ID, "username") 
password_input = driver.find_element(By.ID, "password")

username_input.send_keys("adminzenverseharis")
password_input.send_keys("hahay123")

# 4. Submit form
password_input.send_keys(Keys.RETURN)  

# 5. Tunggu dan verifikasi hasil login
time.sleep(10)  


if "dashboard" in driver.current_url:
    print("✅ Login berhasil!")
else:
    print("❌ Login gagal!")

# 6. Tutup browser
driver.quit()
