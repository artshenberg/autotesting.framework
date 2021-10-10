from tests.test_data import TestData


class BaseTest:
    def __init__(self):
        self.driver = driver

    def set_up(self, driver):
        self.driver.get(TestData.BASE_URL)

    def tear_down(self):
        self.driver.quite()
