from selenium.common.exceptions import NoSuchElementException
from utils.engine import Engine

from traceback import print_stack
import logging

from utils.logger import use_logger


class BaseElement:
    """
    Provides Base class for the Web Element
    """
    log = use_logger(logging.DEBUG)

    def __init__(self, locator, name):
        """Constructor for BaseElement class"""
        self.locator = locator
        self.name = name

    def is_displayed(self):
        """Check if element is presence on a page"""
        return bool(self._find_element)

    def click(self):
        """Do click on the element"""
        try:
            self._find_element().click()
            self.log.info(f'Click element {self.name}.')
        except Exception:
            self.log.error(f' ### Can\'t click on element {self.name}.')
            print_stack()

    def get_attribute(self, attribute):
        """Get defined attribute of element"""
        return self._find_element().get_attribute(attribute)

    def _find_element(self):
        """Returns Web Element by locator if it is presence on a page"""
        try:
            element = Engine.find_element(*self.locator)
            self.log.info(f'Element {self.name} is found.')
            return element
        except NoSuchElementException:
            self.log.error(f' ### Element {self.name} is not found.')
            print_stack()
            return False
