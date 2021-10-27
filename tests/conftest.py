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
    if request.cls is not None:
        request.cls.driver = BrowserFactory.get_driver()
    request.cls.driver.maximize_window()
    yield request.cls.driver
    log.info('Running one time tear down...')
    request.addfinalizer(request.cls.driver.quit())
    request.cls.driver = None


