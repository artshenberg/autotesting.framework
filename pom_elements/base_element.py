from selenium.common.exceptions import *
from factory.browser_factory import BrowserFactory
import logging
from utils.logger import use_logger
from utils.webdriver_waits import Waits


class BaseElement:
    """
    Provides Base class for the Web Element
    """
    LOG = use_logger(logging.DEBUG)

    def __init__(self, locator, name):
        """Constructor for BaseElement class"""
        self.locator = locator
        self.name = name

    def click(self):
        """Do click on the element"""
        self.LOG.info(f'Clicking on element "{self.name}".')
        self.find_element().click()

    def find_element(self):
        """Returns Web Element by locator if it is presence on a page"""
        try:
            self.LOG.info(f'Finding element "{self.name}".')
            return BrowserFactory.get_driver().find_element(*self.locator)
        except NoSuchElementException:
            self.LOG.error(f' ### Can\'t find element "{self.name}".')

    def find_elements(self):
        """Returns Web Elements list by locator if they are presence on a page"""
        try:
            self.LOG.info(f'Finding element "{self.name}".')
            return BrowserFactory.get_driver().find_elements(*self.locator)
        except NoSuchElementException:
            self.LOG.error(f' ### Can\'t find element "{self.name}".')

    def get_attribute(self, attribute):
        """Get defined attribute of element"""
        self.LOG.info(f'Getting attribute "{attribute}" of element "{self.name}".')
        return self.find_element().get_attribute(attribute)

    def get_text(self):
        self.LOG.info(f'Getting text of element "{self.name}".')
        return self.find_element().text

    def is_displayed(self):
        """Check if element is presence on a page"""
        self.LOG.info(f'Checking if element "{self.name}" is displayed.')
        return len(self.find_elements()) > 0

    def wait_for_element(self):
        self.LOG.info(f'Waiting for element "{self.name}".')
        return Waits.wait_for_presence_of_element(self.locator, self.name)

    def wait_for_elements(self):
        self.LOG.info(f'Waiting for list of elements "{self.name}".')
        return Waits.wait_for_presence_of_elements(self.locator, self.name)
