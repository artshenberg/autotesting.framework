from pom_pages.base_form import BaseForm
from pom_elements.base_element import BaseElement
from selenium.webdriver.common.by import By

from tests.test_data import TestData


class IFramePage(BaseForm):

    ALIGN_LEFT_BUTTON = BaseElement((By.XPATH, '//*[@aria-label="Align left"]'), 'ALIGN_LEFT_BUTTON')
    IFRAME = BaseElement((By.TAG_NAME, 'iframe'), 'IFRAME')
    IFRAME_CONTENT_BODY = BaseElement((By.XPATH, '//*[@id="tinymce"]'), 'IFRAME_CONTENT_BODY')
    IFRAME_CONTENT_TEXT = BaseElement((By.XPATH, '//p'), 'IFRAME_CONTENT_TEXT')
    MENUBAR_BUTTONS = BaseElement((By.XPATH, '//*[@role="menubar"]//button'), 'MENUBAR_BUTTONS')
    MENU_FORMAT_FONT_SIZES= BaseElement((By.XPATH, '//*[contains(@title,"Font sizes")]'),
                                        'MENU_FORMAT_FONT_SIZES')
    MENU_FORMAT_FONT_SIZES_12PT = BaseElement((By.XPATH, '//*[contains(@title,"12pt")]'),
                                              'MENU_FORMAT_FONT_SIZES_12PT')
    SYMBOLS = TestData.NUMBER_OF_SYMBOLS_TO_CHANGE
    MUTABLE_SELECTOR = [By.XPATH, '//*[contains(text(),"{}")]']
    MENU_NEW_DOCUMENT_BUTTON = BaseElement((By.XPATH, '//*[contains(@title,"New document")]'),
                                           'MENU_NEW_DOCUMENT_BUTTON')
    NEW_DOCUMENT_MARK = BaseElement((By.XPATH, '//*[contains(@data-mce-bogus,"1")]'),
                                    'NEW_DOCUMENT_MARK')

    def go_to_iframe_page(self):
        self.get_url(TestData.LINK_IFRAME)

    def wait_for_open_text_editor(self):
        element = self.wait_for_open(*self.iframe)
        self.switch_to_iframe(element)
        iframe_text = self.wait_for_open(*self.iframe_content_text)
        iframe_text_is_displayed = self.is_displayed(iframe_text)
        self.leave_iframe()
        return iframe_text_is_displayed

    def align_text_left(self):
        element = self.find_element(*self.align_left_button)
        self.click(element)

    def check_if_iframe_text_is_aligned_left(self):
        element = self.wait_for_open(*self.iframe)
        self.switch_to_iframe(element)
        iframe_content = self.wait_for_open(*self.iframe_content_text)
        iframe_content_text_align = self.get_attribute(iframe_content, 'style')
        self.leave_iframe()
        return TestData.IFRAME_TEXT_ALIGN_TO_CHANGE in iframe_content_text_align

    def change_iframe_text_font_size(self):
        element = self.wait_for_open(*self.iframe)
        self.switch_to_iframe(element)
        iframe_content = self.wait_for_open(*self.iframe_content_text)
        iframe_content_text = self.get_text(iframe_content)
        self.select_text_into_element(iframe_content, round(self.symbols * len(iframe_content_text)))
        self.leave_iframe()
        menu_buttons = self.find_elements(*self.menubar_buttons)
        self.click(menu_buttons[TestData.MENU_BUTTONS['Format']])
        self.click(self.wait_for_open(*self.menu_format_font_sizes))
        self.click(self.wait_for_open(*self.menu_format_font_sizes_12pt))

    def check_if_iframe_text_font_size_is_correct(self):
        element = self.wait_for_open(*self.iframe)
        self.switch_to_iframe(element)
        iframe_content = self.wait_for_open(*self.iframe_content_text)
        iframe_content_text = self.get_text(iframe_content)
        self.mutable_selector[1] = self.mutable_selector[1].format(iframe_content_text[:round(self.symbols * len(iframe_content_text))])
        changed_font_size_text = self.wait_for_open(*self.mutable_selector)
        changed_font_size_value = self.get_attribute(changed_font_size_text, 'style')
        self.leave_iframe()
        return TestData.IFRAME_FONT_SIZE_TO_CHANGE in changed_font_size_value

    def make_new_document(self):
        menu_buttons = self.find_elements(*self.menubar_buttons)
        self.click(menu_buttons[TestData.MENU_BUTTONS['File']])

    def chek_if_document_is_new(self):
        self.click(self.wait_for_open(*self.menu_new_document_button))
        element = self.wait_for_open(*self.iframe)
        self.switch_to_iframe(element)
        is_it_new_document =self.is_element_present(*self.new_document_mark)
        return is_it_new_document
