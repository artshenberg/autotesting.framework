from pages.base_form import BaseForm
from selenium.webdriver.common.by import By

from tests.test_data import TestData


class BasicAuthPage(BaseForm):

    basic_auth_congrats = (By.XPATH, '//*[@class="example"]//*[contains(text(),'
                                     '"Congratulations! You must have the proper credentials.")]')

    def should_be_basic_auth_page(self):
        return self.driver.current_url() == TestData.LINK_BASIC_AUTH
