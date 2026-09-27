import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    """
    Pytest fixture to initialize and close down the Chrome WebDriver.
    Ensures each test runs in an isolated browser session.
    """
    options = Options()
    # Launch browser maximized for visual visibility during test execution, just for demo purposes otherwise we could have done it in terminal itself in headless mode instead of visible mode for faster execution
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    # Provide the driver instance to test functions
    yield driver

    # This closes the browser after the test completes
    driver.quit()