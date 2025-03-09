import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)

def test_successful_login(login_page):
    login_page.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.login("Admin", "admin123")

    # Assertion: Check if dashboard loads after login
    assert "dashboard" in login_page.page.url, "Login failed!"
