from pom_elements.base_element import BaseElement


class Button(BaseElement):

    def __init__(self, locator, name):
        super(Button, self).__init__(locator, name)
