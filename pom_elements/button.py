from pom_elements.base_element import BaseElement


class Button(BaseElement):

    def __init__(self, locator, name):
        super(BaseElement, self).__init__()
        self.locator = locator
        self.name = name
