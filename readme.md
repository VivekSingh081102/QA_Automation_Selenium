# Selenium QA Automation

## Task: 
### Write automation tests using selenium framework. Simple example and how you handle good test coverage


## Website Used for testing

[Scentrix Fragrances](https://scentrix-frontend-4lcetwbh3q-el.a.run.app/)

## A Simple demonstation of testing Login Page and Products Page

### Login
- Login page load & title verification
- Invalid credentials testing

### Products & Navigation
- Home page title verification
- Navigation to Fragrances collection page

## For good test Coverage

- I tested for both happy paths (page load, catalog navigation) and negative test cases (invalid credentials, error message validation). Because the expected test cases are easy to check, to have a good test coverage and a robust sytem it is important to test the system against the negative test cases and see how our system handles it.
- To demonstrate it properly the execution was done in visible mode with a sleep of 3 seconds during each test.
- But for actual testing the headless mode will be much faster.


## Steps to achieve the task

- For test setup: i used a centralized conftest.py using Pytest fixtures for browser setup and cleanup automatically.
- To main tain the readability and code structure: I encapsulated UI locators and element interactions in dedicated Page classes (LoginPage, HomePage), which keeps the actual test files (test_login.py, test_products.py) clean and readable.
- I have even used pytest.ini file to make the central configuration file for Pytest so that every developr in team gets the same behavour after running `pytest` command
- For generating html report with captured logs: I used pytest-html plugin.


## Tech Stack

- Python 3.12
- Selenium WebDriver
- Pytest
- Pytest-HTML (For Report Generation)


## How to Run

```bash
# Create virtual envirmonment beofre running the below commands and install the required packages though requirements.txt

# To run the tests in terminal
pytest -v

# TO run the tests and generate HTML report
pytest -v --html=report.html
```