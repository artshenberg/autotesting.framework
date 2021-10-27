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
    TEST_DATA = DATA['java_script_alerts_page']
    Engine.get_url(TEST_DATA['URL'])
    page = JavaScriptAlertsPage()
    assert page.wait_for_open(), \
        'Javascript Alerts page is not opened'
    page.do_click_on_button_jsalert_via_js()
    assert Alerts.get_alert_text(Alerts.wait_for_alert('alert')) == TEST_DATA['ALERT_TEXT'], \
        'JS Alert is not valid'
    Alerts.alert_accept(Alerts.wait_for_alert('alert'))
    assert page.should_be_same_alert_text(TEST_DATA['ALERT_RESULT']), \
        'JS Alert returns wrong result'
    page.do_click_on_button_jsconfirm_via_js()
    assert page.get_jsconfirm(TEST_DATA['CONFIRM_TEXT']), \
        'JS Confirm is not valid'
    Alerts.alert_accept(Alerts.wait_for_alert('confirm'))
    assert page.should_be_same_alert_text(TEST_DATA['CONFIRM_RESULT']), \
        'JS Confirm returns wrong result'
    page.do_click_on_button_jsprompt_via_js()
    assert page.get_jsprompt(TEST_DATA['PROMPT_TEXT']), \
        'JS Prompt is not valid'
    RANDOM_TEXT = random_text()
    Alerts.alert_send_keys(Alerts.wait_for_alert('prompt'), RANDOM_TEXT)
    Alerts.alert_accept(Alerts.wait_for_alert('prompt'))
    assert page.should_be_same_alert_text(TEST_DATA['PROMPT_RESULT'] + RANDOM_TEXT), \
        'JS Prompt returns wrong result'


# @pytest.mark.skip
def test_infinite_scroll():
    TEST_DATA = DATA['infinite_scroll_page']
    Engine.get_url(TEST_DATA['URL'])
    page = InfiniteScrollPage()
    page.wait_for_open()
    page.do_infinite_scroll(TEST_DATA['AGE_ENGINEER'])
    assert page.should_be_same_number(TEST_DATA['AGE_ENGINEER']), \
        'The number of paragraphs is not equal to the age of the engineer'


# @pytest.mark.skip
@pytest.mark.usefixtures('set_up')
def test_upload():
    TEST_DATA = DATA['upload_page']
    Engine.get_url(TEST_DATA['URL'])
    page = UploadPage()
    page.wait_for_open()
    page.do_upload_file(TEST_DATA['FILENAME'])
    assert page.should_be_refreshed_page(), \
        'The page is not refreshed'
    assert page.should_be_success_text(TEST_DATA['UPLOAD_FILE_SUCCESS_TEXT']), \
        'The success text is not present on a page'
    assert page.should_be_file_name_presence(TEST_DATA['FILENAME']), \
        'The filename is not present on a page'
