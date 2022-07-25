from selenium.webdriver.support.select import Select

from pageObjects.BookingConfirmation import BookingConfirmationPage
from pageObjects.FlightBookingForm import FlightBookForm
from pageObjects.LoginPage import LoginPage
from pageObjects.MainPage import MainPage
from pageObjects.ReserveFlightPage import ReserveFlight
from utilities.BaseClass import BaseClass


class basic_util(BaseClass):

    def open_flight_booking_page(self, departure, destination):
        main_page = MainPage(self.driver)
        reserve_flight = ReserveFlight(self.driver)
        select1 = Select(main_page.get_departure_city_dropdown_locator())
        select1.select_by_value(departure)
        self.assertEqual(a=main_page.get_departure_city_dropdown_locator().get_attribute('value'), b="Boston")
        select2 = Select(main_page.get_destination_city_dropdown_locator())
        select2.select_by_value(destination)
        self.elementToClickableWait(locator=main_page.find_flights_button_wait)
        main_page.get_find_flights_button_locator().click()
        self.elementToClickableWait(locator=reserve_flight.choose_this_flight_first_wait)

    def book_flight(self, name, address, city, state, zip_code, card_number, month, year):
        reserve_flight = ReserveFlight(self.driver)
        booking_form = FlightBookForm(self.driver)
        confirmed_booking = BookingConfirmationPage(self.driver)
        self.open_flight_booking_page(departure='Boston', destination='London')
        reserve_flight.get_choose_this_flight_first().click()
        self.presenceOfElementExplicitWait(locator=booking_form.remember_me_checkbox_wait)
        booking_form.get_name_locator().send_keys(name)
        booking_form.get_address_locator().send_keys(address)
        booking_form.get_city_locator().send_keys(city)
        booking_form.get_state_locator().send_keys(state)
        booking_form.get_zip_locator().send_keys(zip_code)
        booking_form.get_credit_card_number().send_keys(card_number)
        booking_form.get_credit_card_month().send_keys(month)
        booking_form.get_credit_card_year().send_keys(year)
        booking_form.get_name_on_card().send_keys(name)
        self.elementToClickableWait(locator=booking_form.purchase_flight_button_wait)
        booking_form.get_purchase_flight_button().click()
        self.presenceOfElementExplicitWait(locator=confirmed_booking.purchase_successful_text_wait)
        self.assertEqual(a=confirmed_booking.get_purchase_successful_text().text,
                         b="Thank you for your purchase today!")

    def login_to_blazedemo(self, email, password):
        main_page = MainPage(self.driver)
        login_page = LoginPage(self.driver)
        self.elementToClickableWait(locator=main_page.home_button_wait)
        main_page.get_home_button_locator().click()
        self.elementToClickableWait(locator=login_page.login_button_wait)
        login_page.get_email_field().send_keys(email)
        login_page.get_password_field().send_keys(password)
        login_page.get_login_button().click()
