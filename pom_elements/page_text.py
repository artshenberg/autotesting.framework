from pom_elements.base_element import BaseElement


class PageText(BaseElement):
    def __init__(self, locator, name):
        super(BaseElement, self).__init__(self, locator, name)

    def get_text(self):
        return self.find_element().text
