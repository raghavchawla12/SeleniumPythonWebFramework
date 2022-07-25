from selenium.webdriver.common.by import By


class ReserveFlight:

    def __init__(self, driver):
        self.driver = driver

    choose_this_flight_first = (By.CSS_SELECTOR, "tr:nth-child(1) input.btn.btn-small")
    choose_this_flight_first_wait = "tr:nth-child(1) input.btn.btn-small"
    flight_rows = (By.CSS_SELECTOR, "tbody tr")
    flights_heading = (By.TAG_NAME, "h3")

    def get_choose_this_flight_first(self):
        return self.driver.find_element(*ReserveFlight.choose_this_flight_first)

    def get_flight_rows(self):
        return self.driver.find_elements(*ReserveFlight.flight_rows)

    def get_flights_heading(self):
        return self.driver.find_element(*ReserveFlight.flights_heading)
