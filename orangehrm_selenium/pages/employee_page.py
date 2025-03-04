from selenium.webdriver.common.by import By
import time

class EmployeePage:
    def __init__(self, driver):
        self.driver = driver
        self.pim_menu = (By.XPATH, "//span[text()='PIM']")
        self.add_employee_button = (By.XPATH, "//button[text()=' Add ']")
        self.first_name_field = (By.NAME, "firstName")
        self.last_name_field = (By.NAME, "lastName")
        self.save_button = (By.XPATH, "//button[text()=' Save ']")

    def add_employee(self, first_name, last_name):
        self.driver.find_element(*self.pim_menu).click()
        self.driver.find_element(*self.add_employee_button).click()
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.save_button).click()

    def search_employee(self, name):
        search_field = (By.XPATH, "//input[@placeholder='Type for hints...']")
        search_button = (By.XPATH, "//button[text()=' Search ']")

        self.driver.find_element(*search_field).send_keys(name)
        self.driver.find_element(*search_button).click()

    def edit_employee(self, new_last_name):
        """Mengedit data employee"""
        edit_button = (By.XPATH, "//i[@class='oxd-icon bi-pencil-fill']")
        last_name_field = (By.NAME, "lastName")
        save_button = (By.XPATH, "//button[text()=' Save ']")

        self.driver.find_element(*edit_button).click()
        self.driver.find_element(*last_name_field).clear()
        self.driver.find_element(*last_name_field).send_keys(new_last_name)
        self.driver.find_element(*save_button).click()

    def delete_employee(self):
        delete_button = (By.XPATH, "//i[@class='oxd-icon bi-trash']")
        confirm_button = (By.XPATH, "//button[text()=' Yes, Delete ']")

        self.driver.find_element(*delete_button).click()
        time.sleep(1)
        self.driver.find_element(*confirm_button).click()


