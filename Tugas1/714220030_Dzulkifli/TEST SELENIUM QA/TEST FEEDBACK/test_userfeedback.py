from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Buka halaman saran
driver.get("https://parkirgratis.if.co.id/pages/saran/saran.html")
time.sleep(2)

try:
    # Isi form feedback
    driver.find_element(By.ID, "nama").send_keys("Jul")
    driver.find_element(By.ID, "gmail").send_keys("wow@gmail.com")
    driver.find_element(By.ID, "saran").send_keys("Saran saya: Tambahkan fitur notifikasi realtime, ya!")

    # Klik tombol Kirim
    submit_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Kirim')]")
    submit_btn.click()
    print("📩 Form saran berhasil dikirim!")

    # Tunggu sebentar untuk efek (kalau ada popup/alert atau redirect)
    time.sleep(2)

except Exception as e:
    print("❌ Terjadi error saat kirim saran:", e)

time.sleep(3)
driver.quit()
