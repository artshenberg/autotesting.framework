from pom_elements.base_element import BaseElement


class Section(BaseElement):

    def __init__(self, locator, name):
        super(Section, self).__init__(locator, name)
