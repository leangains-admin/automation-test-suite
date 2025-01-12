import pytest
import os
from selenium import webdriver

@pytest.fixture(scope='module')
def setup_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.parametrize("username, password, expected_result", [
    (os.environ.get("VALID_USERNAME"), os.environ.get("VALID_PASSWORD"), "Admin Dashboard"),
    (os.environ.get("INVALID_USERNAME"), os.environ.get("INVALID_PASSWORD"), "Login"),
    (os.environ.get("VALID_USERNAME"), os.environ.get("INVALID_PASSWORD"), "Login"),
])
def test_login_scenarios(setup_driver, username, password, expected_result):
    driver = setup_driver
    base_url = os.environ.get("BASE_URL")
    login_url = f"{base_url}/login"
    driver.get(login_url)
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("login").click()

    if expected_result == "Admin Dashboard":
        driver.get(f"{base_url}/admin")
        assert expected_result in driver.title, f"Expected {expected_result} in title, but got {driver.title}"
    else:
        assert expected_result in driver.title, f"Expected {expected_result} in title, but got {driver.title}"