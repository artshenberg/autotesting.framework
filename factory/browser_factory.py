from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOpts
from selenium.webdriver.firefox.options import Options as FfOpts
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from utils.logger import use_logger
from utils.reader import DataLoader
import logging

CONFIG = DataLoader.open_file('/config/config.json')


class BrowserFactory:
    """
    Prepares, sets and returns webdriver
    """

    def driver(self):
        """Sets and return webdriver with defined parameters"""
        USER_LANGUAGE = CONFIG['BROWSER_LOCALE']
        BROWSER = CONFIG['BROWSER_NAME']
        LOG = use_logger(logging.DEBUG)

        if BROWSER == 'chrome':
            return self._chrome(USER_LANGUAGE, BROWSER, LOG)
        elif BROWSER == 'firefox':
            return self._firefox(USER_LANGUAGE, BROWSER, LOG)
        else:
            # Sets default browser
            return self._chrome(USER_LANGUAGE, BROWSER, LOG)

    @staticmethod
    def _chrome(user_language, browser, log):
        log.info(f'Start browser {browser.upper()}...')
        options = ChromeOpts()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                  options=options)
        return driver

    @staticmethod
    def _firefox(user_language, browser, log):
        log.info(f'Start browser {browser.upper()}...')
        profile = webdriver.FirefoxProfile()
        profile.set_preference('intl.accept_languages', user_language)
        options = FfOpts()
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                                   firefox_profile=profile,
                                   firefox_options=options)
        return driver

    @staticmethod
    def get_driver():
        if not BrowserFactory().instance:
            return BrowserFactory().driver()

