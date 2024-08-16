# Selenium Test Automation Framework

This project is a robust Selenium-based test automation framework designed for web application testing, specifically for an e-commerce site (saucedemo.com). It utilizes Python, Selenium WebDriver, pytest, unittest, and Allure for reporting.

## Features

- Page Object Model (POM) design pattern
- Custom logger for detailed logging
- Allure reporting integration
- Support for multiple browsers (Chrome and Safari)
- Flexible element locator strategies
- Randomized product selection for cart testing
- Unified test suite for regression testing

## Project Structure

- `base/`: Contains base classes for WebDriver initialization and common Selenium operations
- `pages/`: Implements Page Object classes for different pages of the application
- `tests/`: Contains test cases using pytest and unittest
- `utils/`: Includes utility functions like custom logger

## Key Components

1. `BaseClass`: Provides wrapper methods for common Selenium operations
2. `Driver`: Manages WebDriver initialization for different browsers
3. `LoginPage`: Handles login functionality
4. `ProductsPage`: Manages product selection, cart operations, and checkout process
5. `TestLoginPage` and `TestProductsPage`: Contain test cases for login and product workflows

## Setup and Execution

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Installation

1. Clone the repository:
   https://github.com/dommarajunikhil26/Selenium_web_automation.git

cd Selenium_web_automation

2. Create and activate virtual environment
   python -m venv ven
   source venv/bin/activate # On Windows use venv\Scripts\activate

3. Install the required packages:
   pip install -r requirements.txt

### Running the Test Suite

To run the complete regression test suite, use the following command from the project root directory:
python -m unittest discover tests

This command will discover and run all test cases in the `tests` directory.

To run specific test classes or methods, you can use:
python -m unittest tests.test_login_page.TestLoginPage or pytest test_login_page.py
python -m unittest tests.test_products_page.TestProductsPage or pytest test_products_page.py

For more verbose output, add the `-v` flag:
python -m unittest discover -v tests
pytest test_login_page.py -v (for individual file)
pytest test_products_page.py -v (for individual file)

## Reporting

The framework uses Allure for generating detailed test reports. Screenshots are automatically captured for failed tests.

To generate and view Allure reports:

1. Run tests with Allure:
   pytest --alluredir=/path/to/allure_reports

2. Generate the report:
   allure serve /path/to/allure_reports
