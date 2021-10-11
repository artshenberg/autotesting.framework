from base.base_element import BaseElement


class TextField(BaseElement):

    def __init__(self,locator, name):
        super(TextField, self).__init__(locator, name)

    def send_text(self, text):
        self._find_element().send_keys(text)
