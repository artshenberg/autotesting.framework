class TestData:
    """
    Provides the project constants
    """

    '''Project's URLs and other necessary data'''
    BASE_URL = 'https://the-internet.herokuapp.com/'
    LINK_BASIC_AUTH = BASE_URL + 'basic_auth'
    LINK_JAVASCRIPT_ALERTS = BASE_URL + 'javascript_alerts'
    LINK_HORIZONTAL_SLIDER = BASE_URL + 'horizontal_slider'
    LINK_HOVERS = BASE_URL + 'hovers'
    LINK_IFRAME = BASE_URL + 'iframe'

    '''Basic Authorization'''
    USER_NAME = 'admin'
    USER_PASSWORD = 'admin'
    BASIC_AUTH_CONGRATS = 'Congratulations! You must have the proper credentials.'

    '''JS Alerts'''
    ALERT_TEXT = 'I am a JS Alert'
    ALERT_RESULT = 'You successfully clicked an alert'
    CONFIRM_TEXT = 'I am a JS Confirm'
    CONFIRM_RESULT = 'You clicked: Ok'
    PROMPT_TEXT = 'I am a JS prompt'
    PROMPT_RESULT = 'You entered: '

    '''Hovers'''
    HOVER_PAGE_USER_NAMES = [1, 3]
    HOVER_PAGE_CORRECT_USER_NAME = 'user'

    '''IFrame'''
    IFRAME_TEXT_ALIGN_TO_CHANGE = 'text-align: left;'
    MENU_BUTTONS = {'File': 0,
                    'Edit': 1,
                    'View': 2,
                    'Format': 3}
    NUMBER_OF_SYMBOLS_TO_CHANGE = float(1 / 2) # it means a half of string length
    IFRAME_FONT_SIZE_TO_CHANGE = 'font-size: 12pt;'
