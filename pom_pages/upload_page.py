from pom_pages.base_form import BaseForm
from pom_elements.button import Button
from pom_elements.footer import Footer
from pom_elements.text_field import TextField
from pom_elements.page_text import PageText
from selenium.webdriver.common.by import By
from utils.engine import Engine


class UploadPage(BaseForm):

    PAGE_NAME = 'upload_page'

    # Elements:
    CHOOSE_FILE_BUTTON = TextField((By.ID, 'file-upload'), 'CHOOSE_FILE_BUTTON')
    UPLOAD_BUTTON = Button((By.ID, 'file-submit'), 'UPLOAD_BUTTON')
    FILE_UPLOAD_SUCCESS = PageText((By.XPATH, '//*[contains(text(),"File Uploaded!")]'), 'FILE_UPLOAD_SUCCESS')
    UPLOADED_FILENAME_PRESENCE = PageText((By.ID, 'uploaded-files'), 'UPLOADED_FILENAME_PRESENCE')
    FOOTER = Footer((By.ID, 'page-footer'), 'FOOTER')

    def __init__(self):
        super(BaseForm, self).__init__()
        self.element = self.FOOTER
        self.name = self.PAGE_NAME

    def do_upload_file(self, filename):
        Engine.choose_file(self.CHOOSE_FILE_BUTTON, filename)
        self.UPLOAD_BUTTON.click()

    def should_be_refreshed_page(self):
        return bool(not(self.UPLOAD_BUTTON.wait_for_element()))

    def should_be_success_text(self, text):
        return self.FILE_UPLOAD_SUCCESS.get_text() == text

    def should_be_file_name_presence(self, filename):
        return self.UPLOADED_FILENAME_PRESENCE.get_text() == filename

