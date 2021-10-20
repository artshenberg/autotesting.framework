from factory.browser_factory import BrowserFactory
import logging
from utils.logger import use_logger
from utils.webdriver_waits import Waits

LOG = use_logger(logging.DEBUG)


class Engine:

    @staticmethod
    def get_url(url):
        LOG.info(f'Getting URL "{url}".')
        BrowserFactory.get_driver().get(url)

    @staticmethod
    def authorize(login, password, url):
        url = url[:8] + login + ':' + password + '@' + url[8:]
        LOG.info(f'Authorizing by URL "{url}".')
        BrowserFactory.get_driver().get(url)

