from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup otomatis ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Buka halaman utama
driver.get("https://parkirgratis.if.co.id/index.html")
time.sleep(2)

try:
    # Klik tombol LOGIN ADMIN
    login_admin_button = driver.find_element(By.LINK_TEXT, "LOGIN ADMIN")
    login_admin_button.click()
    time.sleep(2)

    # Isi form login
    driver.find_element(By.NAME, "username").send_keys("adminparkir")
    driver.find_element(By.NAME, "password").send_keys("parkir123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Tunggu sebentar untuk redirect
    time.sleep(3)

    # Cek apakah berhasil masuk ke dashboard
    dashboard_header = driver.find_element(By.XPATH, "//h3[contains(text(), 'Dashboard')]")
    print("✅ Login berhasil tanpa OTP! Sekarang sudah di halaman:", dashboard_header.text)

except Exception as e:
    print("❌ Terjadi error:", e)

time.sleep(5)
driver.quit()
