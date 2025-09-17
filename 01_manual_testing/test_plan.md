# Test Plan: Login Functionality

## 1. Objective
To verify that the Login functionality on https://the-internet.herokuapp.com/login works correctly for both valid and invalid users.

## 2. Scope
*   **In Scope:** Testing the login form, error messages, and successful redirect.
*   **Out of Scope:** Testing the "Logout" functionality or any other page on the site.

## 3. Testing Approach
We will perform manual functional testing, including:
*   Positive Testing: Logging in with valid credentials.
*   Negative Testing: Logging in with invalid credentials (wrong username, wrong password).
*   UI Testing: Ensuring all elements are present and functional.

## 4. Pass/Fail Criteria
*   **Pass:** A user can log in with valid credentials and is denied access with invalid credentials. Appropriate messages are displayed for each case.
*   **Fail:** Any deviation from the expected behavior.