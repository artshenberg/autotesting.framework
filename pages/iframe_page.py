from base.base_form import BaseForm
from selenium.webdriver.common.by import By

from tests.test_data import TestData


class IFramePage(BaseForm):

    menubar_buttons = (By.XPATH, '//*[@role="menubar"]//button')
    align_left_button = (By.XPATH, '//*[@aria-label="Align left"]')
    iframe_content_body = (By.XPATH, '*[@id="tinymce"]')

    def should_be_iframe_page(self):
        return self.driver.current_url() == TestData.LINK_IFRAME
