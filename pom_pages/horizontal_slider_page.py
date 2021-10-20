from pom_pages.base_form import BaseForm
from pom_elements.base_element import BaseElement
from selenium.webdriver.common.by import By

from tests.test_data import TestData


class HorizontalSliderPage(BaseForm):

    HORIZONTAL_SLIDER = BaseElement((By.XPATH, '//*[contains(@type,"range")]'), 'HORIZONTAL_SLIDER')
    SLIDER_VALUE = BaseElement((By.ID, '#range'), 'SLIDER_VALUE')

    def go_to_horizontal_slider_page(self):
        self.get_url(TestData.LINK_HORIZONTAL_SLIDER)

    def wait_for_open_horizontal_slider_page(self):
        return self.wait_for_open(*self.footer) and self.current_url() == TestData.LINK_HORIZONTAL_SLIDER

    def move_slider_to_random_position(self):
        slider = self.wait_for_open(*self.horizontal_slider)
        minimal = int(float(slider.get_attribute('min')))
        maximal = int(float(slider.get_attribute('max')))
        position = int(RT.random_digit(minimal, maximal))
        self.move_to_the_right(slider, position)
        self.position = position

    def check_slider_value_after_move(self):
        slider_value = int(self.find_element(*self.slider_value).text)
        return slider_value == self.position
