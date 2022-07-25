from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    login_button_wait = "button.btn.btn-primary"
    login_button = (By.CSS_SELECTOR, "button.btn.btn-primary")
    email_field = (By.CSS_SELECTOR, "input#email")
    password_field = (By.CSS_SELECTOR, "input#password")
    forgot_password = (By.CSS_SELECTOR, "a.btn.btn-link")
    forgot_password_wait = "a.btn.btn-link"
    status_code = (By.CSS_SELECTOR, "div.code")
    status_code_wait = "div.code"
    message = (By.CSS_SELECTOR, "div.message")


    def get_login_button(self):
        return self.driver.find_element(*LoginPage.login_button)

    def get_email_field(self):
        return self.driver.find_element(*LoginPage.email_field)

    def get_password_field(self):
        return self.driver.find_element(*LoginPage.password_field)

    def get_forgot_password(self):
        return self.driver.find_element(*LoginPage.forgot_password)

    def get_status_code(self):
        return self.driver.find_element(*LoginPage.status_code)

    def get_message(self):
        return self.driver.find_element(*LoginPage.message)
