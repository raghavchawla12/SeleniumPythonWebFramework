import pytest
from selenium import webdriver

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome")


@pytest.fixture(scope="function")
def setup(request):
    global driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("headless")
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\ragha\\OneDrive\\Documents\\Chromedriver\\chromedriver"
                                                  ".exe",
                                  options=chrome_options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="/Users/mac/Documents/drivers/geckodriver")
    else:
        print("Only Chrome and Firefox driver are supportable")
    driver.maximize_window()
    driver.get("https://blazedemo.com/")
    request.cls.driver = driver
    yield
    driver.close()
