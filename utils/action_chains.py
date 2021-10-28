from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from utils.driver_util import DriverUtil


class Actions:

    @staticmethod
    def press_key_down():
        move = webdriver.ActionChains(DriverUtil().get_driver())
        move.key_down(Keys.ARROW_DOWN).perform()