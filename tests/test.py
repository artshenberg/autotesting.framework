from pom_forms.java_script_alerts_page import JavaScriptAlertsPage
from pom_forms.infinite_scroll_page import InfiniteScrollPage
from pom_forms.upload_page import UploadPage
import pytest

from factory.browser_factory import BrowserFactory

import logging
from utils.logger import use_logger
from utils.reader import DataLoader
from utils.engine import Engine
from utils.alerts import Alerts
from utils.randomizer import random_text

LOG = use_logger(logging.DEBUG)
DATA = DataLoader.open_file('a.shenberg', 'tests/test_data.json')


# @pytest.mark.skip
@pytest.mark.usefixtures('set_up')
def test_javascript_alerts_via_js():
    TEST_DATA = DATA['java_script_alerts_page']
    Engine.get_url(TEST_DATA['URL'])
    page = JavaScriptAlertsPage()
    assert page.is_displayed(), \
        'Text editor page is not opened'
    page.do_click_on_button_jsalert_via_js()
    assert Alerts.get_alert_text(Alerts.switch_to_alert()) == TEST_DATA['ALERT_TEXT'], \
        '"I am a JS Alert" text is not displayed'
    Alerts.alert_accept(Alerts.switch_to_alert())
    assert not Alerts.switch_to_alert(), \
        'Alert is not closed'
    assert page.should_be_same_alert_text(TEST_DATA['ALERT_RESULT']), \
        '"You successfully clicked an alert" text is not displayed in Result section'
    page.do_click_on_button_jsconfirm_via_js()
    assert Alerts.get_alert_text(Alerts.switch_to_alert()) == TEST_DATA['CONFIRM_TEXT'], \
        '"I am a JS Confirm" text is not displayed'
    Alerts.alert_accept(Alerts.switch_to_alert())
    assert not Alerts.switch_to_alert(), \
        'Alert is not closed'
    assert page.should_be_same_alert_text(TEST_DATA['CONFIRM_RESULT']), \
        '"You clicked: Ok" text is not displayed in Result section'
    page.do_click_on_button_jsprompt_via_js()
    assert Alerts.get_alert_text(Alerts.switch_to_alert()) == TEST_DATA['PROMPT_TEXT'], \
        '"I am a JS prompt" alert is not displayed'
    RANDOM_TEXT = random_text()
    Alerts.alert_send_keys(Alerts.switch_to_alert(), RANDOM_TEXT)
    Alerts.alert_accept(Alerts.switch_to_alert())
    assert not Alerts.switch_to_alert(), \
        'Alert is not closed'
    assert page.should_be_same_alert_text(TEST_DATA['PROMPT_RESULT'] + RANDOM_TEXT), \
        f'"You entered: <{RANDOM_TEXT}>" text is not displayed'


# @pytest.mark.skip
@pytest.mark.usefixtures('set_up')
def test_infinite_scroll():
    TEST_DATA = DATA['infinite_scroll_page']
    Engine.get_url(TEST_DATA['URL'])
    page = InfiniteScrollPage()
    assert page.is_displayed(), \
        'Pag is not open'
    page.do_infinite_scroll(TEST_DATA['AGE_ENGINEER'])
    assert page.should_be_same_number(TEST_DATA['AGE_ENGINEER']), \
        'Number of paragraphs is not equal to the age of the engineer'


# @pytest.mark.skip
@pytest.mark.usefixtures('set_up')
def test_upload():
    TEST_DATA = DATA['upload_page']
    Engine.get_url(TEST_DATA['URL'])
    page = UploadPage()
    assert page.is_displayed(), \
        'Page is not opened'
    page.do_upload_file(DataLoader.get_filepath('a.shenberg') + TEST_DATA['FILEPATH'])
    assert not page.is_displayed(), \
        'Page is not refreshed'
    assert page.should_be_success_text(TEST_DATA['UPLOAD_FILE_SUCCESS_TEXT']), \
        '"File uploaded!" text is not present on the page'
    assert page.should_be_file_name_presence(TEST_DATA['FILEPATH']), \
        'Filename is not present on the page'
