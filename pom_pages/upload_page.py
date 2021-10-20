from pom_pages.base_form import BaseForm
from pom_elements.base_element import BaseElement
from selenium.webdriver.common.by import By
from utils.reader import DataLoader


class UploadPage(BaseForm):

    CHOOSE_FILE_BUTTON = BaseElement((By.ID, 'file-upload'), 'CHOOSE_FILE_BUTTON')
    UPLOAD_BUTTON = BaseElement((By.ID, 'file-submit'), 'UPLOAD_BUTTON')
    FILE_UPLOAD_SUCCESS = BaseElement((By.XPATH, '//*[contains(text(),"File Uploaded!")]'), 'FILE_UPLOAD_SUCCESS')
    UPLOADED_FILENAME_PRESENCE = BaseElement((By.ID, 'uploaded-files'), 'UPLOADED_FILENAME_PRESENCE')
    DATA = DataLoader.open_file('/tests/test_data.json')['upload_page']


    def do_upload_file(self, filename):
        choose_file_button = self.wait_for_open(*self.choose_file_button)
        self.choose_file(choose_file_button, filename)
        upload_button = self.find_element(*self.upload_button)
        self.click(upload_button)

    def check_if_page_is_refreshed(self):
        return bool(not(self.is_element_present(*self.upload_button)))

    def check_if_upload_file_success(self, text):
        file_upload_success_text = self.get_text(self.wait_for_open(*self.file_upload_success))
        return file_upload_success_text == text

    def check_if_file_name_is_presence(self, filename):
        filename_is_presence = self.get_text(self.wait_for_open(*self.uploaded_filename_presence))
        return filename_is_presence == filename

