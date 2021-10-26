class BaseForm:
    """
    Provides Base class for the Web Page
    """
    def __init__(self, element, name):
        """Constructor for BaseForm class"""
        self.element = element
        self.name = name

    def is_displayed(self):
        """Check if page is presence"""
        return self.element.is_displayed()

    def wait_for_open(self):
        """Waiting for open page (waiting for element-indicator)"""
        return self.element.wait_for_element()
