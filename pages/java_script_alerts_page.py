from base.base_form import BaseForm
from selenium.webdriver.common.by import By

from tests.test_data import TestData


class JavaScriptAlertsPage(BaseForm):

    button_bjsAlert = (By.XPATH, '//*[contains(@onclick,"jsAlert")]')
    button_jsConfirm = (By.XPATH, '//*[contains(@onclick,"jsConfirm")]')
    button_jsPrompt = (By.XPATH, '//*[contains(@onclick,"jsPrompt")]')

    def should_be_java_script_alerts_page(self):
        return self.driver.current_url() == TestData.LINK_JAVASCRIPT_ALERTS
