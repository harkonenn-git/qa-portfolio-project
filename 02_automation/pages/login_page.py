from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    Page Object Class for the Login page at
    https://the-internet.herokuapp.com/login
    """

    # Page URL
    URL = "https://the-internet.herokuapp.com/login"

    # Locators (All element selectors in one place)
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".flash.success")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".flash.error")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        """Navigate to the login page."""
        self.driver.get(self.URL)
        return self

    def enter_credentials(self, username, password):
        """Enter username and password into their fields."""
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        return self

    def click_login(self):
        """Click the login button."""
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        return self

    def login(self, username, password):
        """Complete login action: Load page, enter credentials, click login."""
        self.load()
        self.enter_credentials(username, password)
        self.click_login()

    def get_success_message(self):
        """Get the text of the success message after login."""
        return (
            WebDriverWait(self.driver, 10)
            .until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE))
            .text
        )

    def get_error_message(self):
        """Get the text of the error message after failed login."""
        return (
            WebDriverWait(self.driver, 10)
            .until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
            .text
        )
