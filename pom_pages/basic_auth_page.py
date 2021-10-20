from pom_pages.base_form import BaseForm
from pom_elements.page_text import PageText
from selenium.webdriver.common.by import By
from utils.engine import Engine
from utils.reader import DataLoader


class BasicAuthPage(BaseForm):

    DATA = DataLoader.open_file('/tests/test_data.json')['basic_auth_page']
    BASIC_AUTH_CONGRATS = PageText((By.XPATH, '//*[@class="example"]//*[contains(text(),'
                                                 '"Congratulations! You must have the proper credentials.")]'),
                                      'BASIC_AUTH_CONGRATS')

    def __init__(self, element, name):
        super(BaseForm, self).__init__(self, element, name)

    def authorizing(self, login, password):
        Engine.authorize(login, password)

    def should_be_autorized(self):
        pass
