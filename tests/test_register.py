import pytest
from selenium import webdriver

# Dummy test data
valid_email = 'test@example.com'
invalid_email = 'invalidemail'
valid_username = 'newuser'
valid_password = 'password123'

@pytest.fixture(scope='module')
def setup_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Positive test case for registration
@pytest.mark.parametrize('email, username, password', [(valid_email, valid_username, valid_password)])
def test_register_positive(setup_driver, email, username, password):
    driver = setup_driver
    driver.get('http://example.com/register')
    driver.find_element_by_name('email').send_keys(email)
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_name('register').click()
    assert 'Registration successful' in driver.page_source

# Negative test case for registration
@pytest.mark.parametrize('email, username, password', [(invalid_email, valid_username, valid_password)])
def test_register_negative(setup_driver, email, username, password):
    driver = setup_driver
    driver.get('http://example.com/register')
    driver.find_element_by_name('email').send_keys(email)
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_name('register').click()
    assert 'Invalid email' in driver.page_source