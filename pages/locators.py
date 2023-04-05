from selenium.webdriver.common.by import By


class Locator:
    """Locator objects for finding Selenium WebElements"""
    def __init__(self, l_type, selector):
        self.l_type = l_type
        self.selector = selector

    def parameterize(self, *args):
        self.selector = self.selector.format(*args)


class SearchPageLocators:
    """Class for google search page selectors"""
    SEARCH_BAR = Locator(By.XPATH, "//input[@type='text']")
    SEARCH_RESULT = Locator(By.XPATH, "//a[@href='{}']")


class LoginPageLocators:
    """Class for login page selectors"""
    LOGIN_USERNAME = Locator(By.XPATH, "//input[@name='verificationPhone']")
    LOGIN_CAPTCHA = Locator(By.XPATH, "//input[@name='imageVerifyCode']")
    LOGIN_VALIDATION_CODE = Locator(By.XPATH, "//input[@name='verificationCode']")
    # LOGIN_BUTTON = Locator(By.XPATH, "//button[contains(text(), 'login-button')]")
    LOGIN_BUTTON = Locator(By.XPATH, "//span[contains(text(), '登录')]")
    LOGIN_RESULT = Locator(By.XPATH, "//div[contains(text(), '您已进入培训系统，所有的业务操作仅供培训及模拟操作使用，不会生效')]")


    