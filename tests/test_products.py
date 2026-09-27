import logging
from pages.home_page import HomePage

logging.basicConfig(level=logging.INFO)


def test_home_page_title(driver):
    """Verify scentrix homepage loads and displays expected branding title."""
    print("\n[LOG] Starting test: test_home_page_title")
    home_page = HomePage(driver)
    
    print("[LOG] Navigating to homepage...")
    home_page.open()
    
    print("[LOG] Verifying branding title contains 'SCENT-RIX'...")
    assert "SCENT-RIX" in home_page.get_title()
    print("[LOG] Test passed: Homepage title verified.")


def test_navigate_to_fragrances(driver):
    """Verify header navigation successfully and opens the Fragrances catalog."""
    print("\n[LOG] Starting test: test_navigate_to_fragrances")
    home_page = HomePage(driver)
    
    print("[LOG] Opening homepage...")
    home_page.open()
    
    print("[LOG] Clicking Fragrances header navigation link...")
    home_page.open_fragrances()
    
    print("[LOG] Validating current URL contains 'fragrances'...")
    assert "fragrances" in driver.current_url
    print("[LOG] Test passed: Successfully navigated to Fragrances collection.")