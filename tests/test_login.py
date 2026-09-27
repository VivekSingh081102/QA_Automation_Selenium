import logging
from pages.login_page import LoginPage

logging.basicConfig(level=logging.INFO)


def test_login_page_loads(driver):
    """Verify login page renders with correct site title."""
    print("\n[LOG] Starting test: test_login_page_loads")
    login_page = LoginPage(driver)
    
    print("[LOG] Opening Scentrix login page...")
    login_page.open()
    
    print("[LOG] Validating page title contains 'SCENT-RIX'...")
    assert "SCENT-RIX" in driver.title
    print("[LOG] Test passed: Login page loaded successfully.")


def test_invalid_login(driver):
    """Verify submitting invalid credentials prevents unauthorized login."""
    print("\n[LOG] Starting test: test_invalid_login")
    login_page = LoginPage(driver)
    
    print("[LOG] Opening login page...")
    login_page.open()
    
    print("[LOG] Attempting login with invalid credentials...")
    login_page.login("invalid_user@example.com", "wrongpassword")

    print("[LOG] Verifying user remains blocked on login route...")
    assert "login" in driver.current_url or login_page.get_error_message() != ""
    print("[LOG] Test passed: Invalid login attempt correctly blocked.")

"""
In this I have used the logging info because all the tests were passed smoothly so therer were no logs to display in the generated report of result...THus to make sure every test was passed the logging has been done even for successful cases...
"""