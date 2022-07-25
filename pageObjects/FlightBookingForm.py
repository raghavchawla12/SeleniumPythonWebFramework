from selenium.webdriver.common.by import By


class FlightBookForm:

    def __init__(self, driver):
        self.driver = driver

    remember_me_checkbox = (By.ID, "rememberMe")
    remember_me_checkbox_wait = "input#rememberMe"
    name = (By.CSS_SELECTOR, "input#inputName")
    address = (By.CSS_SELECTOR, "input#address")
    city = (By.CSS_SELECTOR, "input#city")
    state = (By.CSS_SELECTOR, "input#state")
    zip = (By.CSS_SELECTOR, "input#zipCode")
    credit_card_number = (By.CSS_SELECTOR, "input#creditCardNumber")
    credit_card_month = (By.CSS_SELECTOR, "input#creditCardMonth")
    credit_card_year = (By.CSS_SELECTOR, "input#creditCardYear")
    name_on_card = (By.CSS_SELECTOR, "input#nameOnCard")
    purchase_flight_button = (By.CSS_SELECTOR, "input.btn.btn-primary")
    purchase_flight_button_wait = "input.btn.btn-primary"

    def get_remember_me_checkbox(self):
        return self.driver.find_element(*FlightBookForm.remember_me_checkbox)

    def get_name_locator(self):
        return self.driver.find_element(*FlightBookForm.name)

    def get_address_locator(self):
        return self.driver.find_element(*FlightBookForm.address)

    def get_city_locator(self):
        return self.driver.find_element(*FlightBookForm.city)

    def get_state_locator(self):
        return self.driver.find_element(*FlightBookForm.state)

    def get_zip_locator(self):
        return self.driver.find_element(*FlightBookForm.zip)

    def get_credit_card_number(self):
        return self.driver.find_element(*FlightBookForm.credit_card_number)

    def get_credit_card_month(self):
        return self.driver.find_element(*FlightBookForm.credit_card_month)

    def get_credit_card_year(self):
        return self.driver.find_element(*FlightBookForm.credit_card_year)

    def get_name_on_card(self):
        return self.driver.find_element(*FlightBookForm.name_on_card)

    def get_purchase_flight_button(self):
        return self.driver.find_element(*FlightBookForm.purchase_flight_button)

