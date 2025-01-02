import pytest
from selenium import webdriver

@pytest.fixture(scope='module')
def setup_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Test case for accessing admin dashboard
@pytest.mark.parametrize('username, password', [(valid_username, valid_password)])
def test_access_admin_dashboard(setup_driver, username, password):
    driver = setup_driver
    driver.get('http://example.com/login')
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_name('login').click()
    driver.get('http://example.com/admin')
    assert 'Admin Dashboard' in driver.title