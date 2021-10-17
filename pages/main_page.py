from pages.base_form import BaseForm
from selenium.webdriver.common.by import By

from tests.test_data import TestData


class MainPage(BaseForm):

    link_basic_auth = (By.PARTIAL_LINK_TEXT, 'basic_auth')
    link_javascript_alerts = (By.PARTIAL_LINK_TEXT, 'javascript_alerts')
    link_horizontal_slider = (By.PARTIAL_LINK_TEXT, 'horizontal_slider')
    link_hovers = (By.PARTIAL_LINK_TEXT, 'hovers')
    link_iframe = (By.PARTIAL_LINK_TEXT, 'iframe')
    footer = (By.ID, 'page-footer')

    basic_auth_congrats = (By.XPATH, '//*[@class="example"]//*[contains(text(),"Congrat")]')

    def wait_for_open_main_page(self):
        return self.wait_for_open(*self.footer) and self.current_url() == TestData.BASE_URL

    def go_to_basic_auth(self):
        self.get_url(f'{TestData.LINK_BASIC_AUTH[:8]}{TestData.USER_NAME}:'
                     f'{TestData.USER_PASSWORD}@{TestData.LINK_BASIC_AUTH[8:]}')

    def should_be_authorized(self):
        element = self.find_element(*self.basic_auth_congrats)
        text = self.get_text(element)
        return text == TestData.BASIC_AUTH_CONGRATS
