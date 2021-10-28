import logging
from utils.logger import use_logger


class BaseForm:
    """
    Provides Base class for the Web Page
    """
    LOG = use_logger(logging.DEBUG)

    def __init__(self, element, name):
        """Constructor for BaseForm class"""
        self.element = element
        self.name = name

    def is_displayed(self):
        """Check if form is presence"""
        self.LOG.info(f'Checking if form "{self.name}" is displayed.')
        return self.element.is_displayed()

    def wait_for_open(self):
        """Waiting for open form (waiting for unique element)"""
        self.LOG.info(f'Waiting for open form "{self.name}".')
        return self.element.wait_for_element()
