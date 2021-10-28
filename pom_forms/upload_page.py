from pom_forms.base_form import BaseForm
from pom_elements.button import Button
from pom_elements.drag_n_drop_field import DragNDropField
from pom_elements.text_field import TextField
from pom_elements.page_text import PageText
from selenium.webdriver.common.by import By


class UploadPage(BaseForm):

    PAGE_NAME = 'upload_page'

    # Elements:
    CHOOSE_FILE = TextField((By.ID, 'file-upload'), 'CHOOSE_FILE')
    UPLOAD_BUTTON = Button((By.ID, 'file-submit'), 'UPLOAD_BUTTON')
    FILE_UPLOAD_SUCCESS = PageText((By.XPATH, '//*[contains(text(),"File Uploaded!")]'), 'FILE_UPLOAD_SUCCESS')
    UPLOADED_FILENAME_PRESENT = PageText((By.ID, 'uploaded-files'), 'UPLOADED_FILENAME_PRESENT')
    DRAG_DROP_UPLOAD_FIELD = DragNDropField((By.ID, 'drag-drop-upload'), 'DRAG_DROP_UPLOAD_FIELD')

    def __init__(self):
        super(UploadPage, self).__init__(self.DRAG_DROP_UPLOAD_FIELD, self.PAGE_NAME)

    def do_upload_file(self, filepath):
        self.CHOOSE_FILE.send_keys(filepath)
        self.UPLOAD_BUTTON.click()

    def should_be_refreshed_page(self):
        return not bool((self.UPLOAD_BUTTON.wait_for_element()))

    def should_be_success_text(self, text):
        return self.FILE_UPLOAD_SUCCESS.get_text() == text

    def should_be_file_name_presence(self, filepath):
        return self.UPLOADED_FILENAME_PRESENT.get_text() == filepath[-8:]

