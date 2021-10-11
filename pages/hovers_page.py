from base.base_form import BaseForm
from selenium.webdriver.common.by import By

from tests.test_data import TestData


class HoversPage(BaseForm):

    user_labels = (By.XPATH, '//*[@class="figure"]')
    user_name = (By.XPATH, '//*[@class="figure"]//*[contains(text(),": ")]')
    profile_links = (By.XPATH, '//*[@class="figcaption"]//a')

    def should_be_hovers_page(self):
        return self.driver.current_url() == TestData.LINK_HOVERS
