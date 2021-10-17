from pages.main_page import MainPage
import pytest
from tests.test_data import TestData

# @pytest.mark.skip
def test_basic_auth(browser):
    page = MainPage(browser)
    page.get_url()
    assert page.wait_for_open_main_page(), 'Main page is not opened'
    page.go_to_basic_auth()
    assert page.should_be_authorized(), 'Text is not valid'

# @pytest.mark.skip
def test_javascript_alerts(browser):
    page = MainPage(browser)
    page.go_to_js_alert_page()
    assert page.wait_for_open_js_alert_page(), 'Javascript Alerts page is not opened'
    page.do_click_on_js_alerts()
    assert page.get_js_alert(), 'JS Alert is not valid'
    page.accept_js_alert()
    assert page.check_js_alert_result(), 'JS Alert returns wrong result'
    page.do_click_on_js_confirm()
    assert page.get_js_confirm(), 'JS Confirm is not valid'
    page.accept_js_alert()
    assert page.check_js_confirm_result(), 'JS Confirm returns wrong result'
    page.do_click_on_js_prompt()
    assert page.get_js_prompt(), 'JS Prompt is not valid'
    page.input_random_text_into_js_prompt()
    page.accept_js_alert()
    assert page.check_js_prompt_result(), 'JS Prompt returns wrong result'

# @pytest.mark.skip
def test_horizontal_slider(browser):
    page = MainPage(browser)
    page.go_to_horizontal_slider_page()
    assert page.wait_for_open_horizontal_slider_page(), 'Horizontal slider page is not opened'
    page.move_slider_to_random_position()
    assert page.check_slider_value_after_move(), 'Slider value is not equal to random choice position'

# @pytest.mark.skip
@pytest.mark.parametrize('username', TestData.HOVER_PAGE_USER_NAMES)
def test_hovers(browser, username):
    page = MainPage(browser)
    page.go_to_hovers_page()
    assert page.wait_for_open_hovers_page() , 'Hovers page is not opened'
    page.move_cursor_to_user_label(username)
    assert page.check_if_user_name_is_correct(username), f'Username of user{username} is incorrect'
    assert page.check_if_link_to_profile_is_displayed(username), f'Link to user{username} profile is not displayed'
    assert page.click_on_user_label_and_check_url(username)
    page.go_to_previous_page()
    assert page.wait_for_open_hovers_page() , 'Hovers page is not opened'

# @pytest.mark.skip
def test_iframe(browser):
    page = MainPage(browser)
    page.go_to_iframe_page()
    assert page.wait_for_open_text_editor(), 'Text editor is nod loaded'
    page.align_text_left()
    assert page.check_if_iframe_text_is_aligned_left(), 'IFrame text is not aligned left'
    page.change_iframe_text_font_size()
    assert page.check_if_iframe_text_font_size_is_correct(), 'Font size changed incorrect'
    page.make_new_document()
    assert page.chek_if_document_is_new(), 'New document format is default'


