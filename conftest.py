import pytest
from base.browser_factory import BrowserFactory

from traceback import print_stack
import logging

from utils.logger import use_logger
from config.config import TestConfig
from tests.test_data import TestData


@pytest.fixture(scope="class")
def ones_set_up(request, browser):
    log = use_logger(logging.DEBUG)
    try:
        log.info('Running one time set up...')
        factory = BrowserFactory()
        driver = factory.get_driver(browser)
        driver.implicitly_wait(TestConfig.WAIT_TIME)
        eval(TestConfig.WINDOW_SETTINGS)
        driver.get(TestData.BASE_URL)
        if request.cls is not None:
            request.cls.driver = driver
    except Exception:
        log.error(f' ### Exception occurred while setting up browser {browser.upper()}.')
        print_stack()

    yield driver
    try:
        driver.quit()
        log.info('Running one time tear down...')
    except Exception:
        log.error(f' ### Exception occurred while tearing down browser {browser.upper()}.')
        print_stack()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
