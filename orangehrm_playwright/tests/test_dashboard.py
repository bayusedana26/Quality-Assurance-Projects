import pytest
from playwright.sync_api import Page

@pytest.fixture
def setup(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield page

def test_dashboard_visibility(setup):
    assert setup.locator("h6").text_content() == "Dashboard", "Dashboard not visible"
