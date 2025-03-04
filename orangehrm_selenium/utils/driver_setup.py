from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    """Setup Chrome WebDriver"""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Full screen browser
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)
