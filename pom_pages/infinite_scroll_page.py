from pom_pages.base_form import BaseForm
from pom_elements.base_element import BaseElement
from selenium.webdriver.common.by import By
from utils.reader import DataLoader
from utils.engine import Engine


class InfiniteScrollPage(BaseForm):

    PAGE_NAME = 'infinite_scroll_page'
    DATA = DataLoader.open_file('/tests/test_data.json')['infinite_scroll_page']
    # Elements:
    JSCROLL_ADDED_ELEMENTS = BaseElement((By.CLASS_NAME, 'jscroll-added'), 'JSCROLL_ADDED_ELEMENTS')

    def __init__(self, element, name):
        super(BaseForm, self).__init__(self, element, name)

    def should_be_infinite_scroll_page(self):
        Engine.get_url(self.DATA['URL'])
        self(self.JSCROLL_ADDED_ELEMENTS).wait_for_open()

    def do_infinite_scroll(self,iterations):
        self.infinite_scrolling(*self.jscroll_added_elements, iterations)

    def check_if_number_of_paragraphs_is_equal_to_age(self, age):
        print(len(self.wait_for_elements(*self.jscroll_added_elements)))
        return len(self.wait_for_elements(*self.jscroll_added_elements)) == age
