import time
from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.employee_page import EmployeePage

def test_create_employee():
    driver = get_driver()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Login
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    # Add Employee
    employee_page = EmployeePage(driver)
    employee_page.add_employee("Bayu", "Sedana")

    print("Test Create Employee Berhasil!")

    time.sleep(3)
    driver.quit()
