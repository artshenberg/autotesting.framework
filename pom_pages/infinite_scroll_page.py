from pom_pages.base_form import BaseForm
from pom_elements.paragraph import Paragraph
from pom_elements.footer import Footer
from selenium.webdriver.common.by import By
from utils.engine import Engine


class InfiniteScrollPage(BaseForm):

    PAGE_NAME = 'infinite_scroll_page'

    # Elements:
    JSCROLL_ADDED_ELEMENTS = Paragraph((By.CLASS_NAME, 'jscroll-added'), 'JSCROLL_ADDED_ELEMENTS')
    FOOTER = Footer((By.ID, 'page-footer'), 'FOOTER')

    def __init__(self):
        super(BaseForm, self).__init__()
        self.element = self.FOOTER
        self.name = self.PAGE_NAME

    def should_be_infinite_scroll_page(self, url):
        return Engine.get_current_url() == url

    def do_infinite_scroll(self, iterations):
        Engine.infinite_scrolling(self.JSCROLL_ADDED_ELEMENTS, iterations)

    def should_be_same_number(self, age):
        return len(self.JSCROLL_ADDED_ELEMENTS.wait_for_elements()) == age
