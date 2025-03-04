import time
from utils.driver_setup import get_driver
from pages.login_page import LoginPage, LogoutPage
from pages.appointment_page import AppointmentPage
from selenium.webdriver.common.by import By

def test_delete_appointment():
    driver = get_driver()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    driver.find_element(By.LINK_TEXT, "Make Appointment").click()

    # Login
    login_page = LoginPage(driver)
    login_page.login("John Doe", "ThisIsNotAPassword")

    appointment_page = AppointmentPage(driver)
    appointment_page.create_appointment("Hongkong CURA Healthcare Center", "12/03/2025", "Testing delete")

    logout_page = LogoutPage(driver)
    logout_page.logout()

    assert "Login" in driver.title
    print("✅ Test Delete Appointment Berhasil!")

    time.sleep(3)
    driver.quit()
