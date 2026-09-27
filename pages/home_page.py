import time
from selenium.webdriver.common.by import By


class HomePage:
    """
    Page Object Model representing the Scentrix Home Page.
    Encapsulates header navigation elements and homepage interactions.
    This is done for better code structure and readability.
    """

    # These are the navigation links in header bar
    FRAGRANCES_NAV = (By.XPATH, "//a[contains(@href, '/fragrances')]")
    COLLECTIONS_NAV = (By.XPATH, "//a[contains(@href, '/collections')]")
    LOGIN_NAV = (By.XPATH, "//a[contains(@href, '/login')]")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        """Navigate to the scentrix homepage."""
        self.driver.get("https://scentrix-frontend-4lcetwbh3q-el.a.run.app/")
        # Visual delay just for demo purposes
        time.sleep(3)

    def get_title(self):
        """Return browser window page title."""
        return self.driver.title

    def open_fragrances(self):
        """Navigate to the fragrances catalog page from header nav."""
        self.driver.find_element(*self.FRAGRANCES_NAV).click()
        time.sleep(3)

    def open_login(self):
        """Navigate to the login page from header nav."""
        self.driver.find_element(*self.LOGIN_NAV).click()
        time.sleep(3)