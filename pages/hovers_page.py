from pages.base_form import BaseForm
from selenium.webdriver.common.by import By

from tests.test_data import TestData


class HoversPage(BaseForm):

    user_labels = (By.XPATH, '//*[@class="figure"]')
    user_names = (By.XPATH, '//*[@class="figure"]//*[contains(text(),": ")]')
    profile_links = (By.XPATH, '//*[@class="figcaption"]//a')
    profile_page = (By.XPATH, '//*[contains(text(),"Not Found")]')
    users_page = (By.XPATH, '//*[contains(text(),"Hovers")]')

    def go_to_hovers_page(self):
        self.get_url(TestData.LINK_HOVERS)

    def wait_for_open_hovers_page(self):
        return self.wait_for_open(*self.footer) and self.current_url() == TestData.LINK_HOVERS

    def move_cursor_to_user_label(self, username):
        labels = self.find_elements(*self.user_labels)
        user = labels[username - 1]
        self.move_to_the_element(user)

    def check_if_user_name_is_correct(self, username):
        user_names = self.find_elements(*self.user_names)
        return self.get_text(user_names[username - 1])[-5:] == TestData.HOVER_PAGE_CORRECT_USER_NAME + str(username)

    def check_if_link_to_profile_is_displayed(self, username):
        profile_links = self.find_elements(*self.profile_links)
        return self.is_displayed(profile_links[username - 1])

    def click_on_user_label_and_check_url(self, username):
        profile_links = self.find_elements(*self.profile_links)
        user = profile_links[username - 1]
        profile_url = self.get_attribute(profile_links[username - 1], 'href')
        self.click(user)
        self.wait_for_open(*self.profile_page)
        return self.current_url() == profile_url

    def go_to_users_page(self):
        self.go_to_previous_page()
