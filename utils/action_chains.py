from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from factory.browser_factory import BrowserFactory


class Actions:

    @staticmethod
    def press_key_down():
        move = webdriver.ActionChains(BrowserFactory.get_driver())
        move.key_down(Keys.ARROW_DOWN).perform()