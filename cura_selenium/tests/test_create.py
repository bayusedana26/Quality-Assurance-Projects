from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.appointment_page import AppointmentPage
import time

service = Service(executable_pathh="chromedriver.exe")
driver = webdriver.Chrome(service=service)

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    service = Service(executable="chromedriver.exe")
    return webdriver.Chrome(service=service, options=options)

def test_create_appointment():
    driver = get_driver()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    
    driver.find_element(By.LINK_TEXT, "Make Appointment").click()

    # Login
    login_page = LoginPage(driver)
    login_page.login("John Doe", "ThisIsNotAPassword")

    # Create Appointment
    appointment_page = AppointmentPage(driver)
    appointment_page.create_appointment("Hongkong CURA Healthcare Center", "12/03/2025", "Testing automation")

    # Success Message
    success_message = driver.find_element(By.TAG_NAME, "h2").text
    assert success_message == "Appointment Confirmation"

    print("Test Create Appointment Berhasil!")

    time.sleep(3)
    driver.quit()

if __name__ == "__main__":
    test_create_appointment()