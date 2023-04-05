import time
from pages.locators import LoginPageLocators
from pages.page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



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
        time.sleep(3)
        element = super().get_element(LoginPageLocators.LOGIN_USERNAME)
        element.clear()
        element.send_keys(username)
        element.send_keys(Keys.ENTER)

    def input_captcha(self, captcha):
        element = super().get_element(LoginPageLocators.LOGIN_CAPTCHA)
        element.clear()
        element.send_keys(captcha)
        element.send_keys(Keys.ENTER)

    def input_validation_code(self, validation_code):
        element = super().get_element(LoginPageLocators.LOGIN_VALIDATION_CODE)
        element.clear()
        element.send_keys(validation_code)
        element.send_keys(Keys.ENTER)

    def login(self):
        element = super().get_element(LoginPageLocators.LOGIN_BUTTON)
        # element.clear()
        element.click()
        # element.send_keys(Keys.ENTER)
        # actions = ActionChains(self.driver)
        # actions.click(element).perform()
        # time.sleep(10)
        # self.driver.switch_to.window(self.driver.window_handles[0])

    def verify_login_results(self, content):
        time.sleep(15)
        # self.driver.switch_to.window(self.driver.window_handles[-1])
        #
        # super()._execute_with_wait(EC.new_window_is_opened)
        # self.driver.get("https://dev.morewithcore.cn/home")
        # time.sleep(10)

        LoginPageLocators.LOGIN_RESULT.parameterize(content)
        assert super().element_exists(LoginPageLocators.LOGIN_RESULT) is True, (
            "Expected search result was not found on the search page"
        )


login_page = LoginPage.get_instance()
