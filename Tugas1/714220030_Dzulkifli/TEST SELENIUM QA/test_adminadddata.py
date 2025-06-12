from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup ChromeDriver otomatis
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Buka halaman login
driver.get("https://parkirgratis.if.co.id/pages/login/login.html")
time.sleep(2)

# Login dulu
driver.find_element(By.NAME, "username").send_keys("adminparkir")
driver.find_element(By.NAME, "password").send_keys("parkir123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Tunggu OTP manual
input("📲 Masukkan OTP di browser lalu tekan Enter...")

# Akses halaman admin
driver.get("https://parkirgratis.if.co.id/pages/admin/admin.html")
time.sleep(2)

# Klik tombol update berdasarkan ID lokasi
try:
    lokasi_id = "66865544f162312b216c27e0"
    xpath_button = f"//button[contains(@onclick, '{lokasi_id}')]"
    update_button = driver.find_element(By.XPATH, xpath_button)
    update_button.click()
    print(f"✅ Tombol Update untuk ID {lokasi_id} berhasil diklik.")

    time.sleep(2)

    # Contoh validasi setelah klik (opsional)
    nama_input = driver.find_element(By.ID, "namaTempat")
    print("📋 Nama tempat terisi:", nama_input.get_attribute("value"))

except Exception as e:
    print("❌ Gagal klik tombol Update:", e)

# Tunggu biar kelihatan
time.sleep(5)
driver.quit()
