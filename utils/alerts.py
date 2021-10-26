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
    def wait_for_alert(alert_type, timeout=CONFIG['WAIT_TIME']):
        wait = WebDriverWait(BrowserFactory.get_driver(), timeout=timeout,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        if alert_type == 'alert':
            alert = wait.until(EC.alert_is_present())
        elif alert_type == 'confirm' or 'prompt':
            wait.until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
        else:
            print(' ### Unexpected alert type')
        return alert

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
