from utils.engine import Engine


class BaseForm:
    def __init__(self, element, name):
        self.element = element
        self.name = name

    def is_displayed(self):
        return self.element.is_displayed()


'''   @staticmethod
    def wait_for_open():
        Engine.wait_for_element()
'''
