import pytest
from pages.login_page import LoginPage


class TestLogin:

    def test_valid_login(self, driver):
        """Test successful login with valid credentials."""
        login_page = LoginPage(driver)
        login_page.login("tomsmith", "SuperSecretPassword!")

        # Assertions
        assert "/secure" in driver.current_url
        assert "You logged into a secure area!" in login_page.get_success_message()

    def test_invalid_username(self, driver):
        """Test error message with invalid username."""
        login_page = LoginPage(driver)
        login_page.login("invalid_user", "any_password")

        # Assertions
        assert "/secure" not in driver.current_url
        assert "Your username is invalid!" in login_page.get_error_message()

    def test_invalid_password(self, driver):
        """Test error message with invalid password."""
        login_page = LoginPage(driver)
        login_page.login("tomsmith", "wrong_password")

        # Assertions
        assert "/secure" not in driver.current_url
        assert "Your password is invalid!" in login_page.get_error_message()
