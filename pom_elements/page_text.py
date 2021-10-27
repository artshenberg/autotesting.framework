from pom_elements.base_element import BaseElement


class PageText(BaseElement):
    def __init__(self, locator, name):
        super(PageText, self).__init__(locator, name)