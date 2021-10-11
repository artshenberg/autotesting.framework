from base.base_form import BaseForm
from selenium.webdriver.common.by import By

from tests.test_data import TestData


class MainPage(BaseForm):

    locators = {'link_basic_auth': (By.PARTIAL_LINK_TEXT, 'basic_auth'),
                'link_javascript_alerts': (By.PARTIAL_LINK_TEXT, 'javascript_alerts'),
                'link_horizontal_slider': (By.PARTIAL_LINK_TEXT, 'horizontal_slider'),
                'link_hovers': (By.PARTIAL_LINK_TEXT, 'hovers'),
                'link_iframe': (By.PARTIAL_LINK_TEXT, 'iframe')
                }

    def should_be_main_page(self):
        return self.current_url() == TestData.BASE_URL

    def go_to_page(self, page):
        pass
