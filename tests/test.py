from pom_pages.java_script_alerts_page import JavaScriptAlertsPage
from pom_pages.infinite_scroll_page import InfiniteScrollPage
from pom_pages.upload_page import UploadPage
import pytest

import logging
from utils.logger import use_logger
from utils.reader import DataLoader
from utils.engine import Engine
from utils.alerts import Alerts
from utils.randomizer import random_text

LOG = use_logger(logging.DEBUG)
DATA = DataLoader.open_file('/tests/test_data.json')


# @pytest.mark.skip
def test_javascript_alerts_via_js():
    page = JavaScriptAlertsPage()
    Engine.get_url(DATA['java_script_alerts_page']['URL'])
    assert page.wait_for_open(), \
        'Javascript Alerts page is not opened'
    page.do_click_on_button_jsalert_via_js()
    assert page.get_jsalert(DATA['java_script_alerts_page']['ALERT_TEXT']), \
        'JS Alert is not valid'
    Alerts.alert_accept(Alerts.wait_for_alert('alert'))
    assert page.should_be_same_alert_text(DATA['java_script_alerts_page']['ALERT_RESULT']), \
        'JS Alert returns wrong result'
    page.do_click_on_button_jsconfirm_via_js()
    assert page.get_jsconfirm(DATA['java_script_alerts_page']['CONFIRM_TEXT']), \
        'JS Confirm is not valid'
    Alerts.alert_accept(Alerts.wait_for_alert('confirm'))
    assert page.should_be_same_alert_text(DATA['java_script_alerts_page']['CONFIRM_RESULT']), \
        'JS Confirm returns wrong result'
    page.do_click_on_button_jsprompt_via_js()
    assert page.get_jsprompt(DATA['java_script_alerts_page']['PROMPT_TEXT']), \
        'JS Prompt is not valid'
    RANDOM_TEXT = random_text()
    Alerts.alert_send_keys(Alerts.wait_for_alert('prompt'), RANDOM_TEXT)
    Alerts.alert_accept(Alerts.wait_for_alert('prompt'))
    assert page.should_be_same_alert_text(DATA['java_script_alerts_page']['PROMPT_RESULT']
                                          + RANDOM_TEXT), \
        'JS Prompt returns wrong result'


# @pytest.mark.skip
def test_infinite_scroll():
    page = InfiniteScrollPage()
    Engine.get_url(DATA['infinite_scroll_page']['URL'])
    page.wait_for_open()
    page.do_infinite_scroll(DATA['infinite_scroll_page']['AGE_ENGINEER'])
    assert page.should_be_same_number(DATA['infinite_scroll_page']['AGE_ENGINEER']), \
        'The number of paragraphs is not equal to the age of the engineer'


# @pytest.mark.skip
def test_upload():
    page = UploadPage()
    Engine.get_url(DATA['upload_page']['URL'])
    page.wait_for_open()
    page.do_upload_file(DATA['upload_page']['FILENAME'])
    assert page.should_be_refreshed_page(), \
        'The page is not refreshed'
    assert page.should_be_success_text(DATA['upload_page']['UPLOAD_FILE_SUCCESS_TEXT']), \
        'The success text is not present on a page'
    assert page.should_be_file_name_presence(DATA['upload_page']['FILENAME']), \
        'The filename is not present on a page'
