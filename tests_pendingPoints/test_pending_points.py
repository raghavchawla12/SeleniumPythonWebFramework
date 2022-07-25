from pageObjects.herukuapp_locators import HerekuApp
from utilities.BaseClass import BaseClass


class Test_Pending_Points(BaseClass):

    def test_01_multiple_checkbox_select(self):
        hereku = HerekuApp(self.driver)
        try:
            self.elementToClickableWait(locator=hereku.checkbox_link_wait)
            hereku.get_checkbox_link().click()
            self.elementToClickableWait(locator="#checkboxes > input[type=checkbox]:nth-child(1)")
            checkboxes = hereku.get_checkboxes()
            for checkbox in checkboxes:
                if not checkbox.is_selected():
                    checkbox.click()
            assert checkbox.is_selected()
        except Exception as assertion_error:
            self.driver.save_screenshot('screenshot_checkbox.png')
            raise assertion_error

    def test_02_file_upload(self):
        hereku = HerekuApp(self.driver)
        try:
            self.elementToClickableWait(locator=hereku.file_upload_link_wait)
            hereku.get_file_upload_link().click()
            self.elementToClickableWait(locator=hereku.upload_button_wait)
            upload_button = hereku.get_file_upload_button()
            file_location = "/Users/mac/Documents/sample_pdf.pdf"
            upload_button.send_keys(file_location)
            self.force_wait(2)
            hereku.get_upload_button().click()
            self.text_to_be_present_in_a_locator_wait(locator=hereku.file_uploaded_text_wait, text="File Uploaded!")
            self.assertEqual(a=hereku.get_file_uploaded_text().text, b="File Uploaded!")
        except Exception as assertion_error:
            self.driver.save_screenshot('screenshot_file_upload.png')
            raise assertion_error
