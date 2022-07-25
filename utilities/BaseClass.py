import inspect
import logging
import time

import pytest
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def presenceOfElementExplicitWait(self, locator):
        wait = WebDriverWait(self.driver, 120)
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, locator)))

    def visibilityOfElementLocated(self, locator):
        wait = WebDriverWait(self.driver, 60)
        wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locator)))

    def elementToClickableWait(self, locator):
        wait = WebDriverWait(self.driver, 90)
        wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, locator)))

    def force_wait(self, time_in_seconds=None):
        if time_in_seconds is None:
            time.sleep(2)
        else:
            time.sleep(time_in_seconds)

    def assert_image_is_displayed(self, image_locator):
        current_link = image_locator.get_attribute('src')
        r = requests.get(current_link)
        try:
            self.assertEqual(r.status_code, 200)
        except AssertionError as e:
            self.verificationErrors.append(current_link + ' delivered response code of ' + r.status_code)
            raise e

    def assert_current_external_link(self, external_link_locator, expected_link):
        external_link_locator_href = external_link_locator.get_attribute('href')
        r = requests.get(external_link_locator_href)
        try:
            # self.assertEqual(r.status_code, 200)
            self.assertEqual(external_link_locator_href, expected_link)
        except AssertionError as e:
            self.verificationErrors.append(external_link_locator_href + ' delivered response code of ' + r.status_code)
            raise e

    def text_to_be_present_in_a_locator_wait(self, locator, text):
        wait = WebDriverWait(self.driver, 120)
        wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, locator), text))

    def assertEqual(self, a, b):
        assert a == b
