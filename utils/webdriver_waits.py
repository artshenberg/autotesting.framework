from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from utils.logger import use_logger
from utils.reader import DataLoader
from factory.browser_factory import BrowserFactory

LOG = use_logger(logging.DEBUG)


class Waits:
    """
    Provides Selenium WebDriverWaits
    """
    CONFIG = DataLoader.open_file('/config/config.json')

    @staticmethod
    def wait_for_presence_of_element(element, name,  timeout=CONFIG['WAIT_TIME']):
        LOG.info(f'Waiting for maximum "{str(timeout)}" seconds for element "{name}" to be presence')
        WebDriverWait(BrowserFactory.get_driver(), timeout=timeout)\
            .until(EC.presence_of_element_located(element))

    @staticmethod
    def wait_for_presence_of_elements(element, name,  timeout=CONFIG['WAIT_TIME']):
        LOG.info(f'Waiting for maximum "{str(timeout)}" seconds for element "{name}" to be presence')
        WebDriverWait(BrowserFactory.get_driver(), timeout=timeout)\
            .until(EC.presence_of_all_elements_located(element))
