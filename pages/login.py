import time
from context.driver import driver
from pages.locators import LoginPageLocators
from pages.page import Page
from selenium.webdriver.common.keys import Keys
from context.config import settings


class LoginPage(Page):
    """Object to represent the login page"""
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = LoginPage()
        return cls.instance

    def __init__(self):
        super().__init__()


    def input_username(self, username):
        element = super().get_element(LoginPageLocators.LOGIN_USERNAME)
        element.clear()
        element.send_keys(username)


    def input_captcha(self, captcha):
        element = super().get_element(LoginPageLocators.LOGIN_CAPTCHA)
        element.clear()
        element.send_keys(captcha)


    def input_validation_code(self, validation_code):
        element = super().get_element(LoginPageLocators.LOGIN_VALIDATION_CODE)
        element.clear()
        element.send_keys(validation_code)


    def login(self):
        element = super().get_element(LoginPageLocators.LOGIN_BUTTON)
        # element.clear()
        # element.send_keys(Keys.ENTER)
        element.click()
        time.sleep(3)
        # super()._execute_with_wait()


    def verify_login_results(self, content):
        time.sleep(3)
        LoginPageLocators.LOGIN_RESULT.parameterize(content)
        assert super().element_exists(LoginPageLocators.LOGIN_RESULT) is True, (
            "Expected search result was not found on the search page"
        )

login_page = LoginPage.get_instance()
