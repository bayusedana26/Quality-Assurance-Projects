from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AppointmentPage:
    def __init__(self, driver):
        self.driver = driver
        self.facility_dropdown = (By.ID, 'combo_facility')
        self.hospital_readmission_checkbox = (By.ID, 'chk_hosp_readmission')
        self.healthcare_program_radio = (By.ID, 'radio_program_medicaid')
        self.visit_date_input = (By.ID, 'txt_visit_date')
        self.comment_textarea = (By.ID, 'txt_comment')
        self.book_appointment_button = (By.ID, 'btn-book-appointment')

    def create_appointment(self, facility, date, comment):
        Select(self.driver.find_element(*self.facility_dropdown)).select_by_visible_text(facility)
        self.driver.find_element(*self.hospital_readmission_checkbox).click()
        self.driver.find_element(*self.healthcare_program_radio).click()
        self.driver.find_element(*self.visit_date_input).send_keys(date)
        self.driver.find_element(*self.comment_textarea).send_keys(comment)
        self.driver.find_element(*self.book_button).click()

class AppointmentConfirmationPage:
    def __init__(self, driver):
        self.driver = driver
        self.facility_text = (By.ID, "facility")
        self.program_text = (By.ID, "program")
        self.comment_text = (By.ID, "comment")

    def get_facility(self):
        return self.driver.find_element(*self.facility_text).text

    def get_program(self):
        return self.driver.find_element(*self.program_text).text

    def get_comment(self):
        return self.driver.find_element(*self.comment_text).text


