"""
This is a locator's list for whole project.
"""
from selenium.webdriver.common.by import By


class MainPageLocators:
    """
    Stores main page's locators.
    """
    link_basic_auth = (By.PARTIAL_LINK_TEXT, 'basic_auth')
    link_javascript_alerts = (By.PARTIAL_LINK_TEXT, 'javascript_alerts')
    link_horizontal_slider = (By.PARTIAL_LINK_TEXT, 'horizontal_slider')
    link_hovers = (By.PARTIAL_LINK_TEXT, 'hovers')
    link_iframe = (By.PARTIAL_LINK_TEXT, 'iframe')


class JavaScriptAlertsPageLocators:
    """
    Stores javascript alerts page's locators.
    """
    button_bjsAlert = (By.XPATH, '//*[contains(@onclick,"jsAlert")]')
    button_jsConfirm = (By.XPATH, '//*[contains(@onclick,"jsConfirm")]')
    button_jsPrompt = (By.XPATH, '//*[contains(@onclick,"jsPrompt")]')


class HorizontalSliderPageLocators:
    """
    Stores horizontal slider page's locators.
    """
    horizontal_slider = (By.XPATH, '//*[contains(@type,"range")]')
    slider_value = (By.ID, '#range')


class HoversPageLocators:
    """
    Stores hovers page's locators.
    """
    user_labels = (By.XPATH, '//*[@class="figure"]')
    user_name = (By.XPATH, '//*[@class="figure"]//*[contains(text(),": ")]')
    profile_links = (By.XPATH, '//*[@class="figcaption"]//a')

class IFramePageLocators:
    """
    Stores iframe page's locators.
    """
    menubar_buttons = (By.XPATH, '//*[@role="menubar"]//button')
    align_left_button = (By.XPATH, '//*[@aria-label="Align left"]')
    iframe_content_body = (By.XPATH, '*[@id="tinymce"]')
    # TODO another locators
