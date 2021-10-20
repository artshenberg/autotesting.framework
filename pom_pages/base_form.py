import logging

from utils.logger import use_logger
from utils.engine import Engine
from utils.webdriver_waits import Waits


class BaseForm:
    """
    Provides Base class for the Web Page
    """
    log = use_logger(logging.DEBUG)

    def __init__(self, element, name):
        """Constructor for BaseForm class"""
        self.element = element
        self.name = name

    def is_displayed(self):
        """Check if page is presence"""
        return self.element.is_displayed()

    def wait_for_open(self):
        return Waits.wait(self.element, self.name)
