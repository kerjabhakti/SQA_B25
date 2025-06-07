from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Buka halaman login
driver.get("https://revan232.github.io/Projectv1/pages/login.html")

# Tunggu sedikit agar halaman termuat
time.sleep(2)

# Isi username dan password
driver.find_element(By.NAME, "username").send_keys("admin")  # ganti sesuai kebutuhan
driver.find_element(By.NAME, "password").send_keys("password123")  # ganti sesuai kebutuhan

# Klik tombol login
driver.find_element(By.XPATH, '//button[text()="Login"]').click()

# Tunggu biar bisa lihat hasilnya
time.sleep(5)

