from utils.driver_util import DriverUtil


class JSExecutor:

    @staticmethod
    def js_click(element):
        DriverUtil().get_driver().execute_script("return arguments[0].click();", element)
