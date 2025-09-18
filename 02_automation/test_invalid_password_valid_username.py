# Import the necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest


# This fixture sets up and tears down the browser for each test
@pytest.fixture
def driver():
    # Setup: This automatically downloads and uses the correct ChromeDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()  # Maximize the browser window
    yield driver  # Provide the driver to the test
    # Teardown: Close the browser after the test is done
    driver.quit()


# Test function for invalid login
def test_invalid_login(driver):
    """
    Test that a user is shown an error message when using invalid credentials.
    This automates the invalid login test case.
    """
    # 1. Navigate to the login page
    driver.get("https://the-internet.herokuapp.com/login")

    # 2. Find the web elements (username field, password field, login button)
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    # 3. Perform the actions with INVALID data
    username_field.send_keys("tomsmith")  # Enter valid username
    password_field.send_keys("anyPassword")  # Enter invalid password
    login_button.click()  # Click the login button

    # 4. VERIFICATION: Assert that the login failed and an error appears
    #    - Check that we are NOT on the secure page (login failed)
    assert "/secure" not in driver.current_url

    #    - Check that an ERROR message is displayed
    error_message = driver.find_element(By.CSS_SELECTOR, ".flash.error")
    assert "Your password is invalid!" in error_message.text

    # If the test reaches this point, all assertions passed
    print("Test Passed: Error message for invalid login was correctly displayed.")
