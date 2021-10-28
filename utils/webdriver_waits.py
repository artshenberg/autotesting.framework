from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from utils.logger import use_logger
from utils.reader import DataLoader
from utils.driver_util import DriverUtil

LOG = use_logger(logging.DEBUG)


class Waits:
    """
    Provides Selenium WebDriverWaits
    """
    CONFIG = DataLoader.open_file('a.shenberg', 'config/config.json')

    @staticmethod
    def wait_for_presence_of_element(element, name,  timeout=CONFIG['WAIT_TIME']):
        LOG.info(f'Waiting for maximum "{str(timeout)}" seconds for element "{name}" to be presence')
        return WebDriverWait(DriverUtil().get_driver(), timeout=timeout)\
            .until(EC.presence_of_element_located(element))

    @staticmethod
    def wait_for_presence_of_all_elements(element, name,  timeout=CONFIG['WAIT_TIME']):
        LOG.info(f'Waiting for maximum "{str(timeout)}" seconds for all elements "{name}" to be presence')
        return WebDriverWait(DriverUtil().get_driver(), timeout=timeout)\
            .until(EC.presence_of_all_elements_located(element))
