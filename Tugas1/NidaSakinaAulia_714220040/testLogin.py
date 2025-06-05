from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoAlertPresentException
import time

def test_login_customer(username, password):
    print(f"\n🔐 MULAI TEST LOGIN CUSTOMER: username='{username}', password='{password}'")
    
    driver = webdriver.Chrome()
    driver.get("https://serlip06.github.io/fe_ATS_serli/pages/login.html")
    time.sleep(2)

    try:
        # Isi username
        driver.find_element(By.ID, "username").clear()
        driver.find_element(By.ID, "username").send_keys(username)

        # Pilih role customer
        select = Select(driver.find_element(By.ID, "role"))
        select.select_by_visible_text("Customer")

        # Isi password
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "password").send_keys(password)

        # Klik tombol login
        driver.find_element(By.XPATH, "//button[text()='Login']").click()
        time.sleep(2)

        # Cek alert (untuk login gagal)
        try:
            alert = driver.switch_to.alert
            print(f"[✖] Login gagal: {alert.text}")
            alert.accept()
        except NoAlertPresentException:
            print(f"[✔] Login customer berhasil: {username}")

    except Exception as e:
        print(f"[!] Terjadi error: {e}")
    
    driver.quit()

# Jalankan testing login sebagai customer
test_login_customer("Qinthar Ganteng", "1234")
