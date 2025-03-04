import time
from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.employee_page import EmployeePage

def test_update_employee():
    driver = get_driver()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Login
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    # Searcj Employee
    employee_page = EmployeePage(driver)
    employee_page.search_employee("Bayu")

    # Edit Employee
    employee_page.edit_employee("Sedana Updated")

    print("Test Update Employee Berhasil!")

    time.sleep(3)
    driver.quit()
