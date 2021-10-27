from pom_elements.base_element import BaseElement


class TextField(BaseElement):

    def __init__(self, locator, name):
        super(TextField, self).__init__(locator, name)

    def send_keys(self, text):
        self.find_element().send_keys(text)
