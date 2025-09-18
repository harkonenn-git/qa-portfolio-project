# Import the necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest


# This is a "fixture". It sets up and tears down the browser for each test.
@pytest.fixture
def driver():
    # Setup: This line automatically downloads and uses the correct ChromeDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()  # Maximize the browser window
    yield driver  # This provides the 'driver' object to our test function
    # Teardown: This runs after the test is done, closing the browser
    driver.quit()


# This is the test function itself. It uses the 'driver' fixture.
def test_valid_login(driver):
    """
    Test that a user can successfully log in with valid credentials.
    This automates test case TC-LOGIN-01.
    """
    # 1. Navigate to the login page
    driver.get("https://the-internet.herokuapp.com/login")

    # 2. Find the web elements (username field, password field, login button)
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    # 3. Perform the actions (enter credentials, click button)
    username_field.send_keys("tomsmith")  # Enter the valid username
    password_field.send_keys("SuperSecretPassword!")  # Enter the valid password
    login_button.click()  # Click the login button

    # 4. VERIFICATION: Assert that the login was successful
    #    - Check that we are on the correct URL after login
    assert "/secure" in driver.current_url
    #    - Check that the success message is displayed
    success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success")
    assert "You logged into a secure area!" in success_message.text

    # If the test reaches this point without throwing an assertion error, it PASSED.
    print("Test Passed: Valid login was successful.")