from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://id.biz.id/LoginPage/")
driver.maximize_window()

driver.find_element(By.ID, "register").click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "form"))
)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("ruthdiana01")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email-regis"))).send_keys("ruthdiana@gmail.com")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "phonenumber"))).send_keys("6289696649577")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password-regis"))).send_keys("Diana12345")

register_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Register')]"))
)
register_button.click()

try:
    # Tunggu munculnya pesan sukses (ubah sesuai selector pesan sukses di web)
    success_message = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "swal2-container"))
    )
    print("Testing BERHASIL: Pendaftaran berhasil.")
except:
    print("Testing GAGAL: Tidak ada pesan berhasil ditemukan.")

time.sleep(3)
driver.quit()
