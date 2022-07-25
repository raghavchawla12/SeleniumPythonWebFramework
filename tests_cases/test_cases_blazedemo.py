import urllib.request
import pytest

from TestData.expected_text_assertions import expected_text
from pageObjects.BookingConfirmation import BookingConfirmationPage
from pageObjects.FlightBookingForm import FlightBookForm
from pageObjects.LoginPage import LoginPage
from pageObjects.MainDestinaion import MainDestination
from pageObjects.MainPage import MainPage
from pageObjects.ReserveFlightPage import ReserveFlight
from utilities.BaseClass import BaseClass
from selenium.webdriver.support.select import Select
from utilities.basic_util_blazedemo import basic_util


class TestCases_Blazedemo(basic_util):
    """In First two test cases, TestData are used to just pick assertion expected text to show use of Test Data"""

    def test_01_verify_that_application_navigates_user_to_blazedemo_login_page_upon_clicking_on_home_button(
            self, get_test_cases_data):
        """Verify that Application displays User to Blazedemo Login Page upon clicking on home button"""
        log = self.getLogger()
        main_page = MainPage(self.driver)
        login_page = LoginPage(self.driver)
        expected_url = get_test_cases_data["test_case_1"]
        try:
            self.elementToClickableWait(locator=main_page.home_button_wait)
            main_page.get_home_button_locator().click()
            self.elementToClickableWait(locator=login_page.login_button_wait)
            self.assertEqual(a=expected_url, b=self.driver.current_url)
            log.info("Test Case is Passed")
        except Exception as assertion_error:
            log.info("Please check, There is some issue")
            self.driver.save_screenshot('screenshot_1.png')
            raise assertion_error
        finally:
            print("Write if any post condition in test that can not be written below yield")

    def test_02_verify_that_application_navigates_user_to_destination_with_image_upon_clicking_on_destination_of_week_link(
            self, get_test_cases_data):
        """Verify that Application navigates user to a destination with Image upon clicking on "Destination of Week,
        The Beach" Link """
        log = self.getLogger()
        main_page = MainPage(self.driver)
        main_destination = MainDestination(self.driver)
        expected_text = get_test_cases_data["test_case_2"]
        try:
            self.elementToClickableWait(locator=main_page.destination_link_wait)
            main_page.get_destination_link_locator().click()
            self.presenceOfElementExplicitWait(locator=main_destination.text_destination_wait)
            self.assertEqual(a=main_destination.get_text_destination_locator().text.strip(), b=expected_text)
            img = main_destination.get_image_locator()
            self.assert_image_is_displayed(image_locator=img)
            log.info("Test Case is Passed")
            # Image Download Function
            img_src = img.get_attribute('src')
            urllib.request.urlretrieve(img_src, "downloaded_image.png")
        except Exception as assertion_error:
            log.info("Please check, There is some issue")
            self.driver.save_screenshot('screenshot_2.png')
            raise assertion_error
        finally:
            print("Write if any post condition in test that can not be written below yield")

    def test_03_verify_that_user_is_able_to_select_any_departure_and_destination_city_from_dropdown(self):
        """Verify that User is able to select any Departure and Destination City from the Dropdown to book Flight"""
        log = self.getLogger()
        main_page = MainPage(self.driver)
        try:
            select1 = Select(main_page.get_departure_city_dropdown_locator())
            select1.select_by_value('Boston')
            self.assertEqual(a=main_page.get_departure_city_dropdown_locator().get_attribute('value'), b="Boston")
            select2 = Select(main_page.get_destination_city_dropdown_locator())
            select2.select_by_value('London')
            self.assertEqual(a=main_page.get_destination_city_dropdown_locator().get_attribute('value'), b="London")
            log.info("Test Case is Passed")
        except Exception as assertion_error:
            log.info("Please check, There is some issue")
            self.driver.save_screenshot('screenshot_3.png')
            raise assertion_error
        finally:
            print("Write if any post condition in test that can not be written below yield")

    def test_04_verify_that_application_displays_multiple_flight_options_upon_clicking_on_find_flights(self):
        """Verify that Application displays multiple flight options upon clicking on Find Flights"""
        log = self.getLogger()
        reserve_flight = ReserveFlight(self.driver)
        try:
            self.open_flight_booking_page(departure='Boston', destination='London')
            flights = reserve_flight.get_flight_rows()
            assert len(flights) > 1
            log.info("Test Case is Passed")
        except Exception as assertion_error:
            log.info("Please check, There is some issue")
            self.driver.save_screenshot('screenshot_4.png')
            raise assertion_error
        finally:
            print("Write if any post condition in test that can not be written below yield")

    def test_05_verify_that_application_displays_the_correct_departure_and_destination_in_flight_options(
            self, get_cities):
        """Verify that Application displays the correct Departure and Destination Name in the page in Flight Option
        Page """
        log = self.getLogger()
        reserve_flight = ReserveFlight(self.driver)
        expected_text = "Flights from " + get_cities['departure'] + " to " + get_cities['destination'] + ":"
        try:
            self.open_flight_booking_page(departure=get_cities['departure'], destination=get_cities['destination'])
            flights_text = reserve_flight.get_flights_heading().text
            self.assertEqual(a=flights_text, b=expected_text)
            log.info("Test Case is Passed")
        except Exception as assertion_error:
            log.info("Please check, There is some issue")
            self.driver.save_screenshot('screenshot_5.png')
            raise assertion_error
        finally:
            print("Write if any post condition in test that can not be written below yield")

    def test_06_verify_that_application_displays_checkbox_and_user_is_able_to_check_checkbox_in_book_flight_form(self):
        """Verify that Application displays the checkbox "Remember Me" in Book Flight Form and User is able to check
        the checkbox """
        log = self.getLogger()
        reserve_flight = ReserveFlight(self.driver)
        booking_form = FlightBookForm(self.driver)
        try:
            self.open_flight_booking_page(departure='Boston', destination='London')
            reserve_flight.get_choose_this_flight_first().click()
            self.presenceOfElementExplicitWait(locator=booking_form.remember_me_checkbox_wait)
            self.assertEqual(a=booking_form.get_remember_me_checkbox().is_displayed(), b=True)
            booking_form.get_remember_me_checkbox().click()
            self.force_wait(1)
            self.assertEqual(a=booking_form.get_remember_me_checkbox().is_selected(), b=True)
            log.info("Test Case is Passed")
        except Exception as assertion_error:
            log.info("Please check, There is some issue")
            self.driver.save_screenshot('screenshot_6.png')
            raise assertion_error
        finally:
            print("Write if any post condition in test that can not be written below yield")

    @pytest.mark.smoke
    def test_07_verify_that_user_is_able_to_book_the_flight_upon_filling_the_correct_details(self, flight_book_form_data):
        """Verify that User is able to book the flight upon filling the correct details"""
        log = self.getLogger()
        reserve_flight = ReserveFlight(self.driver)
        booking_form = FlightBookForm(self.driver)
        confirmed_booking = BookingConfirmationPage(self.driver)
        try:
            self.open_flight_booking_page(departure='Boston', destination='London')
            reserve_flight.get_choose_this_flight_first().click()
            self.presenceOfElementExplicitWait(locator=booking_form.remember_me_checkbox_wait)
            booking_form.get_name_locator().send_keys(flight_book_form_data["name"])
            booking_form.get_address_locator().send_keys(flight_book_form_data["address"])
            booking_form.get_city_locator().send_keys(flight_book_form_data["city"])
            booking_form.get_state_locator().send_keys(flight_book_form_data["state"])
            booking_form.get_zip_locator().send_keys(flight_book_form_data["zip"])
            booking_form.get_credit_card_number().send_keys(flight_book_form_data["card_number"])
            booking_form.get_credit_card_month().send_keys(flight_book_form_data["month"])
            booking_form.get_credit_card_year().send_keys(flight_book_form_data["year"])
            booking_form.get_name_on_card().send_keys(flight_book_form_data["name"])
            self.elementToClickableWait(locator=booking_form.purchase_flight_button_wait)
            booking_form.get_purchase_flight_button().click()
            self.presenceOfElementExplicitWait(locator=confirmed_booking.purchase_successful_text_wait)
            self.assertEqual(a=confirmed_booking.get_purchase_successful_text().text,
                             b="Thank you for your purchase today!")
            log.info("Test Case is Passed")
        except Exception as assertion_error:
            log.info("Please check, There is some issue")
            self.driver.save_screenshot('screenshot_7.png')
            raise assertion_error
        finally:
            print("Write if any post condition in test that can not be written below yield")

    def test_08_verify_the_url_of_flight_booking_confirmation_page(self, flight_book_form_data):
        """Verify that the URL of Flight booking confirmation Page is https://blazedemo.com/confirmation.php"""
        log = self.getLogger()
        try:
            self.book_flight(name=flight_book_form_data["name"], address=flight_book_form_data["address"],
                             city=flight_book_form_data["city"], state=flight_book_form_data["state"],
                             zip_code=flight_book_form_data["zip"], card_number=flight_book_form_data["card_number"],
                             month=flight_book_form_data["month"], year=flight_book_form_data["year"])
            self.assertEqual(a=self.driver.current_url, b="https://blazedemo.com/confirmation.php")
            log.info("Test Case is Passed")
        except Exception as assertion_error:
            log.info("Please check, There is some issue")
            self.driver.save_screenshot('screenshot_8.png')
            raise assertion_error
        finally:
            print("Write if any post condition in test that can not be written below yield")

    def test_09_verify_application_displays_error_upon_entering_invalid_email_in_blazedemo_login_page(self):
        """Verify that Application displays an error if user tries to enter invalid email in Blazedemo Login Page"""
        log = self.getLogger()
        login_page = LoginPage(self.driver)
        invalid_email = "invalid email"
        validation_message_expected = "Please include an '@' in the email address. 'invalid email' is missing an '@'."
        try:
            self.login_to_blazedemo(email=invalid_email, password=invalid_email)
            element = login_page.get_email_field()
            validation_message = self.driver.execute_script('return arguments[0].validationMessage;', element)
            self.assertEqual(a=validation_message_expected, b=validation_message)
            print(validation_message)
            log.info("Test Case is Passed")
        except Exception as assertion_error:
            log.info("Please check, There is some issue")
            self.driver.save_screenshot('screenshot_9.png')
            raise assertion_error
        finally:
            print("Write if any post condition in test that can not be written below yield")

    def test_10_verify_that_application_navigates_to_correct_url_for_forgot_password(self):
        """Verify that Application navigates user to correct URL upon clicking on Forgot Password from Blazedemo
        Login Page """
        log = self.getLogger()
        login_page = LoginPage(self.driver)
        main_page = MainPage(self.driver)
        try:
            self.elementToClickableWait(locator=main_page.home_button_wait)
            main_page.get_home_button_locator().click()
            self.elementToClickableWait(locator=login_page.forgot_password_wait)
            self.assert_current_external_link(external_link_locator=login_page.get_forgot_password(),
                                              expected_link="https://blazedemo.com/password/reset")
            log.info("Test Case is Passed")
        except Exception as assertion_error:
            log.info("Please check, There is some issue")
            self.driver.save_screenshot('screenshot_10.png')
            raise assertion_error
        finally:
            print("Write if any post condition in test that can not be written below yield")

    def test_11_verify_that_application_displays_validation_message_if_user_tries_to_login_with_blank_password(self):
        """Verify the Application displays a Validation message if user tries to login with blank password"""
        log = self.getLogger()
        login_page = LoginPage(self.driver)
        email = "test@test.com"
        validation_message_expected = "Please fill out this field."
        try:
            self.login_to_blazedemo(email=email, password="")
            element = login_page.get_password_field()
            validation_message = self.driver.execute_script('return arguments[0].validationMessage;', element)
            self.assertEqual(a=validation_message_expected, b=validation_message)
            log.info("Test Case is Passed")
        except Exception as assertion_error:
            log.info("Please check, There is some issue")
            self.driver.save_screenshot('screenshot_11.png')
            raise assertion_error
        finally:
            print("Write if any post condition in test that can not be written below yield")

    @pytest.fixture(params=expected_text.test_cases)
    def get_test_cases_data(self, request):
        return request.param

    @pytest.fixture(params=expected_text.test_case_5)
    def get_cities(self, request):
        return request.param

    @pytest.fixture(params=expected_text.flight_book_form)
    def flight_book_form_data(self, request):
        return request.param
