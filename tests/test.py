from pom_pages.java_script_alerts_page import JavaScriptAlertsPage
from pom_pages.infinite_scroll_page import InfiniteScrollPage
from pom_pages.upload_page import UploadPage
import pytest

from factory.browser_factory import BrowserFactory

import logging
from utils.logger import use_logger
from utils.reader import DataLoader
from utils.engine import Engine
from utils.alerts import Alerts
from utils.randomizer import random_text

LOG = use_logger(logging.DEBUG)
DATA = DataLoader.open_file('/tests/test_data.json')


# @pytest.mark.skip
@pytest.mark.usefixtures('set_up')
def test_javascript_alerts_via_js():
    TEST_DATA = DATA['java_script_alerts_page']
    Engine.get_url(TEST_DATA['URL'])
    page = JavaScriptAlertsPage()
    assert page.is_displayed(), \
        'Javascript Alerts page is not opened'
    page.do_click_on_button_jsalert_via_js()
    assert Alerts.get_alert_text(Alerts.switch_to_alert()) == TEST_DATA['ALERT_TEXT'], \
        'JS Alert text is not displayed/valid'
    Alerts.alert_accept(Alerts.switch_to_alert())
    assert not Alerts.switch_to_alert()
    assert page.should_be_same_alert_text(TEST_DATA['ALERT_RESULT']), \
        'JS Alert returns wrong result'
    page.do_click_on_button_jsconfirm_via_js()
    assert Alerts.get_alert_text(Alerts.switch_to_alert()) == TEST_DATA['CONFIRM_TEXT'], \
        'JS Confirm text is not displayed/valid'
    Alerts.alert_accept(Alerts.switch_to_alert())
    assert not Alerts.switch_to_alert()
    assert page.should_be_same_alert_text(TEST_DATA['CONFIRM_RESULT']), \
        'JS Confirm returns wrong result'
    page.do_click_on_button_jsprompt_via_js()
    assert Alerts.get_alert_text(Alerts.switch_to_alert()) == TEST_DATA['PROMPT_TEXT'], \
        'JS Prompt text is not displayed/valid'
    RANDOM_TEXT = random_text()
    Alerts.alert_send_keys(Alerts.switch_to_alert(), RANDOM_TEXT)
    Alerts.alert_accept(Alerts.switch_to_alert())
    assert not Alerts.switch_to_alert()
    assert page.should_be_same_alert_text(TEST_DATA['PROMPT_RESULT'] + RANDOM_TEXT), \
        'JS Prompt returns wrong result'


@pytest.mark.skip
def test_infinite_scroll():
    TEST_DATA = DATA['infinite_scroll_page']
    Engine.get_url(TEST_DATA['URL'])
    page = InfiniteScrollPage()
    page.do_infinite_scroll(TEST_DATA['AGE_ENGINEER'])
    assert page.should_be_same_number(TEST_DATA['AGE_ENGINEER']), \
        'The number of paragraphs is not equal to the age of the engineer'


@pytest.mark.skip
def test_upload():
    TEST_DATA = DATA['upload_page']
    Engine.get_url(TEST_DATA['URL'])
    page = UploadPage()
    page.do_upload_file(TEST_DATA['FILENAME'])
    assert page.should_be_refreshed_page(), \
        'The page is not refreshed'
    assert page.should_be_success_text(TEST_DATA['UPLOAD_FILE_SUCCESS_TEXT']), \
        'The success text is not present on a page'
    assert page.should_be_file_name_presence(TEST_DATA['FILENAME']), \
        'The filename is not present on a page'
