A Python Selenium test automation framework

Features:
Framework for writing cross-browser front-end test suites
Pre-defined test functions for commonly used test procedures
Utilities and extended functionality for the Selenium WebDriver package
Implementation of the Page Object Model with pre-defined page objects for common elements
Command line tool for quickly executing tests and generating test reports
Supports Headless browser testing

SETUP
Prerequisites
a) Install Python 3.6.x
b) Add Python 3.6.x to your PATH environment variable
c) If you do not have it already, get pip
(NOTE: Most recent Python distributions come with pip)
d) pip install -r requirements.txt to install dependencies
**Note:** Command may be ``pip3`` instead of ``pip`` depending on the system.
e) Get setup with your browser driver. If you don't know how to, please try:
For Chrome: https://sites.google.com/a/chromium.org/chromedriver/getting-started
For Firefox: https://developer.mozilla.org/en-US/docs/Mozilla/QA/Marionette/WebDriver #Note: Check firefox version & selenium version compatibility before downloading geckodriver.
For IE: https://support.microsoft.com/en-us/help/2990999/webdriver-support-for-internet-explorer-11
For Edge: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
For Safari: https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari
If your setup goes well, you should be able to run a simple test with this command:
python -m pytest {test_class_path} -k {test_case_name}

To Run Test with HTML Report Generation: 
pytest tests_cases/test_cases_blazedemo.py --html=tests_cases/html_report.html
pytest tests_pendingPoints/test_pending_points.py --html=tests_pendingPoints/html_report_pending_case.html

Notes:

1. Some workarounds are used that are not present in Python but only Jave (Pytest is used instead of TestNG)
2. Pytest HTML Reports are used instead of Extent Report
3. All the Test Cases are independent, Any Test Case can be run either independentally or with their Test Suite