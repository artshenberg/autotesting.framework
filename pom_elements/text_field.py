from pom_elements.base_element import BaseElement


class TextField(BaseElement):

    def __init__(self, locator, name):
        super(BaseElement, self).__init__()
        self.locator = locator
        self.name = name

    def send_keys(self, text):
        self.find_element().send_keys(text)
