from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromOpts
from selenium.webdriver.firefox.options import Options as FfOpts
from config.config import TestConfig


class BrowserFactory:
    """
    Prepares, sets and returns webdriver
    """
    TIMEOUT = TestConfig.EXPLICIT_WAIT_TIME
    _instance = None

    def __new__(cls, *args, **kwargs):
        """Checks if instance is not presence already"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(BrowserFactory, cls).__new__(cls)
        return cls.instance

    def __init__(self, timer=TIMEOUT):
        self.timer = timer

    @staticmethod
    def init_driver():
        """Sets and return webdriver with defined parameters"""
        browser_name = TestConfig.BROWSER_NAME
        user_language = TestConfig.BROWSER_LOCALE
        if browser_name == 'chrome':
            print('\nstart browser chrome for test...')
            options = ChromOpts()
            options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
            options.add_argument('window-size=1024,768')
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                      options=options)
        elif browser_name == 'firefox':
            print('\nstart browser firefox for test...')
            profile = webdriver.FirefoxProfile()
            profile.set_preference('intl.accept_languages', user_language)
            options = FfOpts()
            options.add_argument('--width=1024')
            options.add_argument('--height=768')
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                                       firefox_profile=profile,
                                       firefox_options=options)
        else:
            print(f'Browser {browser_name} still is not implemented')
        yield
        print('\nquit browser...')
        driver.quit()
