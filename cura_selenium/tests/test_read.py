import time
from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.appointment_page import AppointmentPage, AppointmentConfirmationPage
from selenium.webdriver.common.by import By

def test_read_appointment():
    driver = get_driver()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    driver.find_element(By.LINK_TEXT, "Make Appointment").click()

    # Login
    login_page = LoginPage(driver)
    login_page.login("John Doe", "ThisIsNotAPassword")

    appointment_page = AppointmentPage(driver)
    appointment_page.create_appointment("Hongkong CURA Healthcare Center", "12/03/2025", "Testing read")

    confirmation_page = AppointmentConfirmationPage(driver)
    assert confirmation_page.get_facility() == "Hongkong CURA Healthcare Center"
    assert confirmation_page.get_program() == "Medicaid"
    assert confirmation_page.get_comment() == "Testing read"

    print("✅ Test Read Appointment Berhasil!")

    time.sleep(3)
    driver.quit()
