from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOpts
from selenium.webdriver.firefox.options import Options as FfOpts
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from traceback import print_stack
import logging

from utils.logger import use_logger
from config.config import TestConfig


class BrowserFactory:
    """
    Prepares, sets and returns webdriver
    """
    @staticmethod
    def get_driver(browser):
        """Sets and return webdriver with defined parameters"""
        user_language = TestConfig.BROWSER_LOCALE
        log = use_logger(logging.DEBUG)

        if browser == 'chrome':
            try:
                print('\nstart browser chrome for test...')
                options = ChromeOpts()
                options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
                driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                          options=options)
                log.info(f'Start browser {browser.upper()}...')
                return driver
            except Exception:
                log.error(f' ### Exception occurred while starting browser {browser.upper()}.')
                print_stack()
        elif browser == 'firefox':
            try:
                print('\nstart browser firefox for test...')
                profile = webdriver.FirefoxProfile()
                profile.set_preference('intl.accept_languages', user_language)
                options = FfOpts()
                driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                                           firefox_profile=profile,
                                           firefox_options=options)
                log.info(f'Start browser {browser.upper()}...')
                return driver
            except Exception:
                log.error(f' ### Exception occurred when starting browser {browser.upper()}.')
                print_stack()
        else:
            # Sets default browser
            try:
                print('\nstart browser chrome for test...')
                options = ChromeOpts()
                options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
                driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                          options=options)
                log.info(f'Start browser {browser.upper()}...')
                return driver
            except Exception:
                log.error(f' ### Exception occurred when starting browser {browser.upper()}.')
                print_stack()
