from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_herokuapp(username, password):
    print(f"\n🔐 MULAI TEST LOGIN: username='{username}', password='{password}'")
    
    driver = webdriver.Chrome()
    driver.get("http://the-internet.herokuapp.com/login")
    time.sleep(2)

    try:
        # Isi username
        driver.find_element(By.ID, "username").clear()
        driver.find_element(By.ID, "username").send_keys(username)

        # Isi password
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "password").send_keys(password)

        # Klik tombol login
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)

        # Ambil pesan flash
        flash_element = driver.find_element(By.ID, "flash")
        flash_text = flash_element.text.strip()

        if "You logged into a secure area!" in flash_text:
            print(f"[✔] Login berhasil: {flash_text}")
        else:
            print(f"[✖] Login gagal: {flash_text}")

    except Exception as e:
        print(f"[!] Terjadi error: {e}")
    
    driver.quit()

# Contoh penggunaan
test_login_herokuapp("tomsmith", "SuperSecretPassword!")  # ✅ valid credentials
test_login_herokuapp("salah", "password")                 # ❌ invalid credentials