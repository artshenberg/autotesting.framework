import pytest

import logging

from utils.driver_util import DriverUtil
from utils.logger import use_logger
from utils.reader import DataLoader

CONFIG = DataLoader.open_file('a.shenberg', 'config/config.json')


@pytest.fixture(scope="module")
def set_up(request):
    log = use_logger(logging.DEBUG)
    log.info('=================== Running one time set up... ===================')
    driver = DriverUtil().get_driver()
    driver.maximize_window()
    yield driver
    log.info('=================== Running one time tear down... ===================')
    driver.quit()


