from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoAlertPresentException
import time

def test_register_user(username, password, role):
    print(f"\n📝 MULAI TEST REGISTER: username='{username}', password='{password}', role='{role}'")
    
    driver = webdriver.Chrome()
    driver.get("https://serlip06.github.io/fe_ATS_serli/pages/register.html")
    time.sleep(2)

    try:
        # Isi username
        driver.find_element(By.ID, "username").clear()
        driver.find_element(By.ID, "username").send_keys(username)

        # Pilih role
        select = Select(driver.find_element(By.ID, "role"))
        select.select_by_visible_text(role)

        # Isi password
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "password").send_keys(password)

        # Klik tombol register (asumsi tombol ada text 'Register')
        driver.find_element(By.XPATH, "//button[text()='Register']").click()
        time.sleep(2)

        # Cek alert (jika muncul error/register gagal)
        try:
            alert = driver.switch_to.alert
            print(f"[✖] Register gagal: {alert.text}")
            alert.accept()
        except NoAlertPresentException:
            print(f"[✔] Register berhasil: {username}")

    except Exception as e:
        print(f"[!] Terjadi error: {e}")

    driver.quit()

# Contoh panggil fungsi test register
test_register_user("Customer1", "12345", "Customer")
