from behave import given, when, then
from pages.login import login_page

"""Hooks for interacting with main page login"""


@when(u'I input username "{username}"')
def input_username(context, username):
    login_page.input_username(username)

@when(u'I input captcha "{captcha}"')
def input_captcha(context, captcha):
    login_page.input_captcha(captcha)

@when(u'I input validation code "{validation_code}"')
def input_validation_code(context, validation_code):
    login_page.input_validation_code(validation_code)

@when(u'I press the login button')
def click_login_button(context):
    login_page.login()

@then(u'I should see content "{content}" in the results')
def results(context, content):
    login_page.verify_login_results(content)