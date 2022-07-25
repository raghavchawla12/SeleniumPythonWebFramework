import string
import random


class expected_text:

    res = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k=7))

    name = "Test Name" + res

    test_cases = [{"test_case_1": "https://blazedemo.com/login", "test_case_2": "Destination of the week: Hawaii !"}]
    test_case_5 = [{"departure": "Boston", "destination": "London"}]
    flight_book_form = [{"name": name, "address": "123, Main Street", "city": "alabama", "state": "NY", "zip":
        "112211", "card_number": "4111111111111111", "month": "11", "year": "2024"}]
