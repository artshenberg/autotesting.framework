from base.browser_factory import BrowserFactory
from config.config import TestConfig


class BaseForm:
    def __init__(self, element, name):
        self.element = element
        self.name = name
        self.driver = BrowserFactory.get_driver(TestConfig.BROWSER_NAME)

    def is_displayed(self):
        return self.element.is_displayed()

    def wait_for_open(self):
        pass

    def current_url(self):
        return self.driver.current_url()
