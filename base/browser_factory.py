from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromOpts
from selenium.webdriver.firefox.options import Options as FfOpts
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from tests.test_data import TestData
from config.config import TestConfig
from utils.singleton import Singleton


class BrowserFactory(Singleton):
    """
    Prepares, sets and returns webdriver
    """
    def __init__(self, browser):
        self.browser = browser

    def get_driver(self):
        """Sets and return webdriver with defined parameters"""
        USER_LANGUAGE = TestConfig.BROWSER_LOCALE
        WAIT_TIME = TestConfig.WAIT_TIME
        BASE_URL = TestData.BASE_URL
        if self.browser == 'chrome':
            print('\nstart browser chrome for test...')
            options = ChromOpts()
            options.add_experimental_option('prefs', {'intl.accept_languages': USER_LANGUAGE})
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                      options=options)
        elif self.browser == 'firefox':
            print('\nstart browser firefox for test...')
            profile = webdriver.FirefoxProfile()
            profile.set_preference('intl.accept_languages', USER_LANGUAGE)
            options = FfOpts()
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                                       firefox_profile=profile,
                                       firefox_options=options)
        else:
            # Sets default brouser
            print('\nstart browser chrome for test...')
            options = ChromOpts()
            options.add_experimental_option('prefs', {'intl.accept_languages': USER_LANGUAGE})
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                      options=options)
        driver.implicitly_wait(WAIT_TIME)
        driver.maximize_window()
        driver.get(BASE_URL)
        yield driver
        print('\nquit browser...')
        driver.quit()
