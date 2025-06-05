from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Membuka browser
driver1 = webdriver.Chrome()

# Membuka halaman
driver1.get("https://the-internet.herokuapp.com/login")

# Mengisi input username
driver1.find_element(By.ID, "username").send_keys("tomsmith")
driver1.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver1.find_element(By.CSS_SELECTOR, "#login > button").click()


# Tunggu selama 10 detik agar bisa melihat hasilnya
time.sleep(6)

#PAK INI PAKAI WEB ORANG LAIN , SOALNYA WEB YANG MAU SAYA UJI BELUM DI HOSTING / HOSTINGANNYA SUDAH HABIS