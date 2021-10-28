from selenium.common.exceptions import *
import logging
from utils.logger import use_logger
from utils.driver_util import DriverUtil

LOG = use_logger(logging.DEBUG)


class Alerts:

    @staticmethod
    def switch_to_alert():
        try:
            return DriverUtil().get_driver().switch_to.alert
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
