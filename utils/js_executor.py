from factory.browser_factory import BrowserFactory


class JSExecutor:

    @staticmethod
    def js_click(element):
        browser = BrowserFactory()
        browser.get_driver().execute_script("return arguments[0].click();", element)
