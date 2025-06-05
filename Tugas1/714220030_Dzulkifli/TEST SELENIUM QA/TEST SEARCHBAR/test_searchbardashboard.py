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
    # Isi form login
    driver.find_element(By.NAME, "username").send_keys("adminparkir")
    driver.find_element(By.NAME, "password").send_keys("parkir123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Tunggu redirect ke dashboard
    time.sleep(3)

    # Verifikasi masuk ke dashboard
    dashboard_header = driver.find_element(By.XPATH, "//h3[contains(text(), 'Dashboard')]")
    print("✅ Login berhasil tanpa OTP! Sekarang sudah di halaman:", dashboard_header.text)

    # Cari elemen search bar dan masukkan kata kunci "alfamart"
    search_input = driver.find_element(By.XPATH, "//input[@placeholder='Search anything...']")
    search_input.clear()
    search_input.send_keys("alfamart")

    time.sleep(2)  # Tunggu hasil filter tampil

    # Cek apakah hasil yang ditampilkan sesuai
    results = driver.find_elements(By.XPATH, "//td[contains(text(), 'Alfamart')]")
    if results:
        print(f"✅ Search berhasil, ditemukan {len(results)} hasil yang mengandung 'Alfamart'.")
        for result in results:
            print("Hasil:", result.text)
    else:
        print("❌ Tidak ada hasil ditemukan untuk pencarian 'Alfamart'.")

except Exception as e:
    print("❌ Terjadi error:", e)

time.sleep(5)
driver.quit()
