import pytest
from selenium import webdriver

driver = None


@pytest.fixture(scope="function")
def setup(request):
    global driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("headless")

    driver = webdriver.Chrome(executable_path="/Users/mac/Documents/drivers/chromedriver",
                              options=chrome_options)
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/")
    request.cls.driver = driver
    yield
    driver.close()
