from tests.test_data import TestData


class BaseTest:
    def set_up(self, driver):
        self.driver = driver
        self.driver.get(TestData.BASE_URL)

    def tear_down(self):
        self.driver.quite()
