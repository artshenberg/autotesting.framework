from base.base_form import BaseForm
from selenium.webdriver.common.by import By

from tests.test_data import TestData


class HorizontalSliderPage(BaseForm):

    horizontal_slider = (By.XPATH, '//*[contains(@type,"range")]')
    slider_value = (By.ID, '#range')

    def should_be_horizontal_slider_page(self):
        return self.driver.current_url() == TestData.LINK_HORIZONTAL_SLIDER
