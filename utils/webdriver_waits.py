from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from utils.logger import use_logger
from utils.reader import DataLoader
from factory.browser_factory import BrowserFactory

LOG = use_logger(logging.DEBUG)


class Waits:
    """
    Provides Selenium WebDriverWait
    """
    CONFIG = DataLoader.open_file('/config/config.json')

    @staticmethod
    def wait(element, name,  timeout=CONFIG['WAIT_TIME']):
        LOG.info(f'Waiting for maximum "{str(timeout)}" seconds for element "{name}" to be presence')
        WebDriverWait(BrowserFactory.get_driver(), timeout=timeout).until(EC.presence_of_element_located(element))
