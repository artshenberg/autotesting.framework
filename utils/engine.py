from factory.browser_factory import BrowserFactory
import logging
from utils.logger import use_logger
from utils.webdriver_waits import Waits
from utils.action_chains import Actions
import os

LOG = use_logger(logging.DEBUG)


class Engine:

    @staticmethod
    def get_url(url):
        LOG.info(f'Getting URL "{url}".')
        browser = BrowserFactory()
        LOG.info(f'Driver instance id is "{id(browser)}".')
        browser.get_driver().get(url)

    @staticmethod
    def authorize_by_url(login, password, url):
        url = url[:8] + login + ':' + password + '@' + url[8:]
        LOG.info(f'Authorizing by URL "{url}".')
        browser = BrowserFactory()
        browser.get_driver().get(url)

    @staticmethod
    def get_current_url():
        browser = BrowserFactory()
        return browser.get_driver().current_url

    @staticmethod
    def choose_file(element, filename):
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, filename)
        element.send_keys(file_path)

    @staticmethod
    def infinite_scrolling(element, iterations):
        counter = len(element.wait_for_elements())  # if number of elements is already equals to iterations
        while counter < iterations:
            Actions.press_key_down()
            counter = len(element.wait_for_elements())
