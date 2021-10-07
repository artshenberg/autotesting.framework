class BaseForm:
    def __init__(self, element, name):
        self.element = element
        self.name = name

    def is_displayed(self):
        return self.element.is_displayed

    def wait_for_open(self):
        pass