import pytest
from factory.browser_factory import BrowserFactory

import logging

from utils.logger import use_logger
from utils.reader import DataLoader

CONFIG = DataLoader.open_file('/config/config.json')


@pytest.fixture(scope="function")
def set_up(request):
    log = use_logger(logging.DEBUG)
    log.info('Running one time set up...')
    driver = BrowserFactory.get_driver()
    driver.maximize_window()
    '''
    # if singleton not works, try code below:
    if request.cls is not None:
        request.cls.driver = driver
    '''
    yield driver
    log.info('Running one time tear down...')
    driver.quit()

