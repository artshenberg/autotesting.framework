from pom_pages.base_form import BaseForm
from pom_elements.button import Button
from pom_elements.drag_n_drop_field import DragNDropField
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
    DRAG_DROP_UPLOAD_FIELD = DragNDropField((By.ID, 'drag-drop-upload'), 'DRAG_DROP_UPLOAD_FIELD')

    def __init__(self):
        super(UploadPage, self).__init__(self.DRAG_DROP_UPLOAD_FIELD, self.PAGE_NAME)

    def do_upload_file(self, filename):
        Engine.choose_file(self.CHOOSE_FILE_BUTTON, filename)
        self.UPLOAD_BUTTON.click()

    def should_be_refreshed_page(self):
        return bool(not(self.UPLOAD_BUTTON.wait_for_element()))

    def should_be_success_text(self, text):
        return self.FILE_UPLOAD_SUCCESS.get_text() == text

    def should_be_file_name_presence(self, filename):
        return self.UPLOADED_FILENAME_PRESENCE.get_text() == filename

