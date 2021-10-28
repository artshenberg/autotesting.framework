from factory.browser_factory import BrowserFactory
from singleton_decorator import singleton



class DriverUtil:
    """
    Calls same instance of webdriver
    """
    _driver = None

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            cls._driver = BrowserFactory.driver()
        return cls._driver
