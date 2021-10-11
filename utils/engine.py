from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from traceback import print_stack
import logging
import pytest

from utils.logger import use_logger


class Engine:

    @pytest.mark.usefixtures('ones_set_up')
    def __init__(self, ones_set_up):
        self.driver = ones_set_up

    def find_element(self, locator):
        return self.driver.find_element(locator)
