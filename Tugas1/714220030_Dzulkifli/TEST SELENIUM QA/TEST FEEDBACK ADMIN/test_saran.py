from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

    # Tunggu sebentar agar login selesai dan session tersimpan
    time.sleep(3)

    # Langsung buka halaman saran
    driver.get("https://parkirgratis.if.co.id/pages/admin/saran.html")
    time.sleep(2)

    # Cek apakah halaman saran terbuka (contoh: cari heading "Saran")
    saran_heading = driver.find_element(By.XPATH, "//h3[contains(text(), 'Saran')]")
    print("✅ Berhasil masuk ke halaman:", saran_heading.text)

except Exception as e:
    print("❌ Terjadi error:", e)

time.sleep(5)
driver.quit()
