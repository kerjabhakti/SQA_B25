from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Chrome()
driver.get("https://id.biz.id/LoginPage/")
driver.maximize_window()

try:
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    email_input.send_keys("ruthdianaps@gmail.com")

    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password_input.send_keys("Purnamasari29")

    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    )
    login_button.click()

    print("Tunggu SweetAlert muncul...")
    sweetalert = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "swal2-popup"))
    )

    alert_text = sweetalert.text
    print("Isi SweetAlert:", alert_text)

    if "berhasil" in alert_text.lower() or "login berhasil" in alert_text.lower():
        print("Login berhasil! Testing sukses.")
    else:
        print("SweetAlert muncul tapi bukan tanda berhasil.")

except TimeoutException:
    print("Timeout: SweetAlert tidak muncul. Login gagal atau indikator salah.")
except Exception as e:
    print("Login gagal atau error terjadi:", e)

finally:
    time.sleep(3)
    driver.quit()
