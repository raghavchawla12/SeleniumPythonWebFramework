from selenium.webdriver.common.by import By


class BookingConfirmationPage:

    def __init__(self, driver):
        self.driver = driver

    purchase_successful_text = (By.TAG_NAME, "h1")
    purchase_successful_text_wait = "h1"

    def get_purchase_successful_text(self):
        return self.driver.find_element(*BookingConfirmationPage.purchase_successful_text)
