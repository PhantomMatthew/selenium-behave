from behave import given, when, then
from pages.login import login_page

"""Hooks for interacting with main page login"""


@when(u'I input username "{username}"')
def step_impl(context, username):
    login_page.input_username(username)

@when(u'I input captcha "{captcha}"')
def step_impl(context, captcha):
    login_page.input_captcha(captcha)

@when(u'I input validation code "{validation_code}"')
def step_impl(context, validation_code):
    login_page.input_validation_code(validation_code)

@when(u'I press the login button')
def step_impl(context):
    login_page.login()

@then(u'I should see content "{content}" in the results')
def step_impl(context, content):
    login_page.verify_login_results(content)