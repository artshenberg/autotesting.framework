from pom_pages.base_form import BaseForm
from pom_elements.base_element import BaseElement
from selenium.webdriver.common.by import By

from tests.test_data import TestData


class JavaScriptAlertsPage(BaseForm):

    BUTTON_BJSALERT = BaseElement((By.XPATH, '//*[contains(@onclick,"jsAlert")]'), 'BUTTON_BJSALERT')
    BUTTON_JSCONFIRM = BaseElement((By.XPATH, '//*[contains(@onclick,"jsConfirm")]'), 'BUTTON_JSCONFIRM')
    BUTTON_JSPROMPT = BaseElement((By.XPATH, '//*[contains(@onclick,"jsPrompt")]'), 'BUTTON_JSPROMPT')


    def go_to_js_alert_page(self):
        self.get_url(TestData.LINK_JAVASCRIPT_ALERTS)

    def wait_for_open_js_alert_page(self):
        return self.wait_for_open(*self.footer) and self.current_url() == TestData.LINK_JAVASCRIPT_ALERTS

    def do_click_on_js_alerts(self):
        element = self.find_element(*self.button_bjsAlert)
        self.click(element)

    def get_js_alert(self):
        return self.wait_for_alert().text == TestData.ALERT_TEXT

    def accept_js_alert(self):
        self.wait_for_alert().accept()

    def check_js_alert_result(self):
        element = self.find_element(*self.js_alert_result)
        text = self.get_text(element)
        return text == TestData.ALERT_RESULT

    def do_click_on_js_confirm(self):
        element = self.find_element(*self.button_jsConfirm)
        self.click(element)

    def get_js_confirm(self):
        return self.wait_for_alert('confirm').text == TestData.CONFIRM_TEXT

    def check_js_confirm_result(self):
        element = self.find_element(*self.js_alert_result)
        text = self.get_text(element)
        return text == TestData.CONFIRM_RESULT

    def do_click_on_js_prompt(self):
        element = self.find_element(*self.button_jsPrompt)
        self.click(element)

    def get_js_prompt(self):
        alert = self.wait_for_alert('prompt')
        return alert, alert.text == TestData.PROMPT_TEXT

    def input_random_text_into_js_prompt(self):
        self.wait_for_alert().send_keys(self.random_text)

    def check_js_prompt_result(self):
        element = self.find_element(*self.js_alert_result)
        text = self.get_text(element)
        return text == TestData.PROMPT_RESULT + self.random_text
