import logging
from utils.driver_util import DriverUtil
from utils.logger import use_logger
from utils.action_chains import Actions
import os

LOG = use_logger(logging.DEBUG)


class Engine:

    @staticmethod
    def get_url(url):
        LOG.info(f'Getting URL "{url}".')
        DriverUtil().get_driver().get(url)

    @staticmethod
    def authorize_by_url(login, password, url):
        url = url[:8] + login + ':' + password + '@' + url[8:]
        LOG.info(f'Authorizing by URL "{url}".')
        DriverUtil().get_driver().get(url)

    @staticmethod
    def get_current_url():
        return DriverUtil().get_driver().current_url

    @staticmethod
    def infinite_scrolling(element, iterations):
        counter = len(element.wait_for_elements())  # if number of elements is already equals to iterations
        while counter < int(iterations):
            Actions.press_key_down()
            counter = len(element.wait_for_elements())
