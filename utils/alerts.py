from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from utils.logger import use_logger
from utils.reader import DataLoader
from factory.browser_factory import BrowserFactory

LOG = use_logger(logging.DEBUG)


class Alerts:

    CONFIG = DataLoader.open_file('/config/config.json')

    @staticmethod
    def switch_to_alert():
        try:
            return BrowserFactory.get_driver().switch_to.alert
        except NoAlertPresentException:
            return False

    @staticmethod
    def get_alert_text(alert):
        return alert.text

    @staticmethod
    def alert_accept(alert):
        alert.accept()

    @staticmethod
    def alert_dismiss(alert):
        alert.dismiss()

    @staticmethod
    def alert_send_keys(alert, text):
        alert.send_keys(text)
