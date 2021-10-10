from base.base_form import BaseForm
from .locators import MainPageLocators
from tests.test_data import TestData


class MainPage(BaseForm):
    def shoud_be_main_page(self):
        current_url = self.driver.get_current_url()
        assert current_url == TestData.BASE_URL,\
            f'\nMain page is not loaded. \nCurrent page URL is {current_url}'

    def go_to_basic_auth(self):
        self.driver
        self.driver.get(TestData.LINK_BASIC_AUTH)

    def should_be_basic_auth_page(self):
        current_url = self.driver.get_current_url()
        assert current_url == TestData.LINK_BASIC_AUTH, \
            f'\nBasic auth page is not loaded. \nCurrent page URL is {current_url}'
