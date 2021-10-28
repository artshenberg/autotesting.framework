from singleton_decorator import singleton
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOpts
from selenium.webdriver.firefox.options import Options as FfOpts
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from utils.logger import use_logger
from utils.reader import DataLoader
import logging

CONFIG = DataLoader.open_file('/config/config.json')


@singleton
class BrowserFactory:
    """
    Prepares, sets and returns webdriver
    """
    @staticmethod
    def get_driver():
        """Sets and return webdriver with defined parameters"""
        USER_LANGUAGE = CONFIG['BROWSER_LOCALE']
        BROWSER = CONFIG['BROWSER_NAME']
        LOG = use_logger(logging.DEBUG)

        if BROWSER == 'chrome':
            LOG.info(f'Start browser {BROWSER.upper()}...')
            options = ChromeOpts()
            options.add_experimental_option('prefs', {'intl.accept_languages': USER_LANGUAGE})
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                      options=options)
            return driver
        elif BROWSER == 'firefox':
            LOG.info(f'Start browser {BROWSER.upper()}...')
            profile = webdriver.FirefoxProfile()
            profile.set_preference('intl.accept_languages', USER_LANGUAGE)
            options = FfOpts()
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                                       firefox_profile=profile,
                                       firefox_options=options)
            return driver
        else:
            # Sets default browser
            LOG.info(f'Start browser {BROWSER.upper()}...')
            options = ChromeOpts()
            options.add_experimental_option('prefs', {'intl.accept_languages': USER_LANGUAGE})
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                      options=options)
            return driver
