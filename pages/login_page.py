import time
from selenium.webdriver.common.by import By


class LoginPage:
    """
    Page Object Model representing the Scentrix Login Page.
    Encapsulates UI locators and authentication user actions.
    """

    # THese are the locators for login page elements
    EMAIL = (By.ID, "lgn-email")
    PASSWORD = (By.ID, "lgn-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".lgn-submit")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".text-red-500, [role='alert']")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        """Navigate to Scentrix login URL."""
        self.driver.get("https://scentrix-frontend-4lcetwbh3q-el.a.run.app/login")
        # Again Visual delay jsut for demo purposes
        time.sleep(3)

    def login(self, email, password):
        """Fill credentials and submit authentication form."""
        # Enter user email
        self.driver.find_element(*self.EMAIL).clear()
        self.driver.find_element(*self.EMAIL).send_keys(email)
        time.sleep(3)

        # Enter password
        self.driver.find_element(*self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        time.sleep(3)

        # Click submit
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        time.sleep(3)

    def get_error_message(self):
        """Retrieve validation or auth error message if displayed."""
        errors = self.driver.find_elements(*self.ERROR_MESSAGE)
        return errors[0].text if errors else ""