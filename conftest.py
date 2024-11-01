import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def setup_driver():
    mobile_emulation = {"deviceName": "iPhone XR"}
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def pytest_sessionstart(session):
    session.driver = setup_driver()

def pytest_sessionfinish(session):
    session.driver.quit()

@pytest.fixture(scope="session")
def driver(request):
    return request.session.driver
