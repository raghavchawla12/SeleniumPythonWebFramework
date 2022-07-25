from selenium.webdriver.common.by import By


class HerekuApp:

    def __init__(self, driver):
        self.driver = driver

    checkbox_link_wait = "li:nth-child(6) > a"
    checkbox_link = (By.CSS_SELECTOR, "li:nth-child(6) > a")
    checkboxes = (By.CSS_SELECTOR, "#checkboxes > input")
    file_upload_link_wait = "li:nth-child(18) > a"
    file_upload_link = (By.CSS_SELECTOR, "li:nth-child(18) > a")
    upload_button_wait = "input.button"
    upload_button = (By.CSS_SELECTOR, "input.button")
    file_upload_button = (By.CSS_SELECTOR, "input#file-upload")
    file_uploaded_text = (By.TAG_NAME, "h3")
    file_uploaded_text_wait = "h3"

    def get_checkbox_link(self):
        return self.driver.find_element(*HerekuApp.checkbox_link)

    def get_checkboxes(self):
        return self.driver.find_elements(*HerekuApp.checkboxes)

    def get_file_upload_link(self):
        return self.driver.find_element(*HerekuApp.file_upload_link)

    def get_upload_button(self):
        return self.driver.find_element(*HerekuApp.upload_button)

    def get_file_upload_button(self):
        return self.driver.find_element(*HerekuApp.file_upload_button)

    def get_file_uploaded_text(self):
        return self.driver.find_element(*HerekuApp.file_uploaded_text)
