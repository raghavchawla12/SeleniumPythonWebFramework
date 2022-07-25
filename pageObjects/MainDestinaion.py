from selenium.webdriver.common.by import By


class MainDestination:

    def __init__(self, driver):
        self.driver = driver

    text_destination_wait = "body > div.container"
    text_destination = (By.CSS_SELECTOR, "body > div.container")
    image_locator = (By.TAG_NAME, "img")

    def get_text_destination_locator(self):
        return self.driver.find_element(*MainDestination.text_destination)

    def get_image_locator(self):
        return self.driver.find_element(*MainDestination.image_locator)

