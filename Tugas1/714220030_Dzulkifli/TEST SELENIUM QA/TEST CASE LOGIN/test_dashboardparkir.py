from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup otomatis ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Buka halaman login
driver.get("https://parkirgratis.if.co.id/pages/login/login.html")
time.sleep(2)

try:
    # Isi login form
    driver.find_element(By.NAME, "username").send_keys("adminparkir")
    driver.find_element(By.NAME, "password").send_keys("parkir123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Tunggu sebentar untuk redirect (bisa disesuaikan)
    time.sleep(3)

    # Cek apakah langsung masuk ke dashboard tanpa OTP
    dashboard_header = driver.find_element(By.XPATH, "//h3[contains(text(), 'Dashboard')]")
    print("✅ Login berhasil tanpa OTP! Sekarang sudah di halaman:", dashboard_header.text)

except Exception as e:
    print("❌ Terjadi error:", e)

time.sleep(5)
driver.quit()
