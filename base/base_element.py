from selenium.common.exceptions import NoSuchElementException
from .browser_factory import BrowserFactory


class BaseElement:
    """
    Provides Base class for the Web Element
    """
    def __init__(self, locator, name):
        """Constructor for BaseElement class"""
        self.locator = locator
        self.name = name

    @staticmethod
    def is_displayed(self):
        """Check if element is presence on a page"""
        return bool(self._find_element)

    def click(self):
        """Do click on the element"""
        self._find_element(self).click()

    def get_attribute(self, attribute):
        """Get defined attribute of element"""
        return self._find_element(self).get_attribute(attribute)

    @staticmethod
    def _find_element(self):
        """Returns Web Element by locator if it is presence on a page"""
        try:
            driver = BrowserFactory.__get__()
            return self.driver.find_element(*self.locator)
        except (NoSuchElementException):
            print(f'Element {self.name} is not found.')
            return False
