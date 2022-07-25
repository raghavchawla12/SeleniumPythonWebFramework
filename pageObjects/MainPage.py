from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    home_button_wait = "a:nth-child(3)"
    home_button = (By.CSS_SELECTOR, "a:nth-child(3)")
    destination_link_wait = "p a"
    destination_link = (By.CSS_SELECTOR, "p a")
    departure_city_dropdown = (By.CSS_SELECTOR, "select.form-inline:nth-child(1)")
    destination_city_dropdown = (By.CSS_SELECTOR, "select.form-inline:nth-child(4)")
    find_flights_button = (By.CSS_SELECTOR, "input.btn.btn-primary")
    find_flights_button_wait = "input.btn.btn-primary"

    def get_home_button_locator(self):
        return self.driver.find_element(*MainPage.home_button)

    def get_destination_link_locator(self):
        return self.driver.find_element(*MainPage.destination_link)

    def get_departure_city_dropdown_locator(self):
        return self.driver.find_element(*MainPage.departure_city_dropdown)

    def get_destination_city_dropdown_locator(self):
        return self.driver.find_element(*MainPage.destination_city_dropdown)

    def get_find_flights_button_locator(self):
        return self.driver.find_element(*MainPage.find_flights_button)
