import time
from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.employee_page import EmployeePage

def test_read_employee():
    driver = get_driver()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Login
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    # Search Employee
    employee_page = EmployeePage(driver)
    employee_page.search_employee("Bayu")

    print("Test Read Employee Berhasil!")

    time.sleep(3)
    driver.quit()
