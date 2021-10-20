from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromOpts
from selenium.webdriver.firefox.options import Options as FfOpts
import pytest


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help='Choose lang')
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose browser: chrome or firefox')


@pytest.fixture(scope='module')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    if browser_name == 'chrome':
        print('\nstart browser chrome for test...')
        options = ChromOpts()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        options.add_argument('window-size=1024,768')
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                  options=options)
        driver.implicitly_wait(10)
        driver.maximize_window()
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
        driver.implicitly_wait(10)
        driver.maximize_window()
    else:
        print(f'Browser {browser_name} still is not implemented')
    yield driver
    print('\nquit browser...')
    driver.quit()
