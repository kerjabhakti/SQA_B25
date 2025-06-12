from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Buka halaman login
driver.get("https://parkirgratis.if.co.id/pages/login/login.html")
time.sleep(2)

try:
    # Login
    driver.find_element(By.NAME, "username").send_keys("adminparkir")
    driver.find_element(By.NAME, "password").send_keys("parkir123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)

    # Cek dashboard muncul
    dashboard_header = driver.find_element(By.XPATH, "//h3[contains(text(), 'Dashboard')]")
    print("✅ Login berhasil:", dashboard_header.text)

    # Klik avatar/profile pic untuk buka dropdown
    profile_avatar = driver.find_element(By.XPATH, "//img[@alt='Your avatar']")
    profile_avatar.click()
    time.sleep(1)  # kasih delay biar dropdown sempat muncul

    # Klik Logout di dalam dropdown
    logout_button = driver.find_element(By.ID, "logoutButton")
    logout_button.click()
    print("🔓 Logout button clicked!")

    time.sleep(2)

    # Verifikasi redirect ke login
    current_url = driver.current_url
    if "login" in current_url:
        print("✅ Logout berhasil, kembali ke halaman login:", current_url)
    else:
        print("❌ Logout gagal, masih di halaman:", current_url)

except Exception as e:
    print("❌ Terjadi error:", e)

time.sleep(3)
driver.quit()
