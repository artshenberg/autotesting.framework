from pom_pages.base_form import BaseForm
from pom_elements.button import Button
from pom_elements.page_text import PageText
from selenium.webdriver.common.by import By
from utils.js_executor import JSExecutor


class JavaScriptAlertsPage(BaseForm):

    PAGE_NAME = 'java_script_alerts_page'

    # Elements:
    BUTTON_JSALERT = Button((By.XPATH, '//*[contains(@onclick,"jsAlert")]'), 'BUTTON_BJSALERT')
    BUTTON_JSCONFIRM = Button((By.XPATH, '//*[contains(@onclick,"jsConfirm")]'), 'BUTTON_JSCONFIRM')
    BUTTON_JSPROMPT = Button((By.XPATH, '//*[contains(@onclick,"jsPrompt")]'), 'BUTTON_JSPROMPT')
    JS_ALERT_RESULT = PageText((By.ID, 'result'), 'JS_ALERT_RESULT')

    def __init__(self):
        super(JavaScriptAlertsPage, self).__init__(self.JS_ALERT_RESULT, self.PAGE_NAME)

    def do_click_on_button_jsalert_via_js(self):
        JSExecutor.js_click(self.BUTTON_JSALERT)

    def should_be_same_alert_text(self, text):
        return self.JS_ALERT_RESULT.get_text() == text

    def do_click_on_button_jsconfirm_via_js(self):
        JSExecutor.js_click(self.BUTTON_JSCONFIRM)

    def do_click_on_button_jsprompt_via_js(self):
        JSExecutor.js_click(self.BUTTON_JSPROMPT)
