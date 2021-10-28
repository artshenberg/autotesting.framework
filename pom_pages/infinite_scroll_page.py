from pom_pages.base_form import BaseForm
from pom_elements.paragraph import Paragraph
from pom_elements.section import Section
from selenium.webdriver.common.by import By
from utils.engine import Engine


class InfiniteScrollPage(BaseForm):

    PAGE_NAME = 'infinite_scroll_page'

    # Elements:
    JSCROLL_ADDED_ELEMENTS = Paragraph((By.CLASS_NAME, 'jscroll-added'), 'JSCROLL_ADDED_ELEMENTS')
    JSCROLL_INNER = Section((By.CLASS_NAME, 'jscroll-inner'), 'JSCROLL_INNER')

    def __init__(self):
        super(InfiniteScrollPage, self).__init__(self.JSCROLL_INNER, self.PAGE_NAME)

    def do_infinite_scroll(self, iterations):
        Engine.infinite_scrolling(self.JSCROLL_ADDED_ELEMENTS, iterations)

    def should_be_same_number(self, age):
        return len(self.JSCROLL_ADDED_ELEMENTS.wait_for_elements()) == age
