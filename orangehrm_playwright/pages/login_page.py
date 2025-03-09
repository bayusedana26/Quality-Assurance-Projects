from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_field = page.locator("input[name='username']")
        self.password_field = page.locator("input[name='password']")
        self.login_button = page.locator("button[type='submit']")

    def login(self, username: str, password: str):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()
