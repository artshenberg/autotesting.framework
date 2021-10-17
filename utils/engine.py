from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from traceback import print_stack
import logging
import pytest

from utils.logger import use_logger
from config.config import TestConfig


class Engine:

    log = use_logger(logging.DEBUG)

    @pytest.mark.usefixtures('ones_set_up')
    def __init__(self, ones_set_up):
        self.driver = ones_set_up

    def find_element(self, locator, name):
        try:
            element = self.driver.find_element(locator, name)
            self.log.info(f'Element {name} is found.')
            return element
        except NoSuchElementException:
            self.log.error(f' ### Element {name} is not found.')
            print_stack()
            return False

    def wait_for_element(self, locator, name, timeout=TestConfig.WAIT_TIME):
        element = None
        try:
            self.driver.implicitly_wait(0)
            self.log.info(f'Waiting for maximum :: {str(timeout)} :: seconds for element to be clickable')
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable(locator))
            self.log.info(f'Element {name} appeared on the page')
            self.driver.implicitly_wait(TestConfig.WAIT_TIME)
        except Exception:
            self.log.info(f'Element {name} did not appear on the page')
            print_stack()
        return element

    def current_url(self):
        pass