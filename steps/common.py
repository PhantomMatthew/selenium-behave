from behave import given, when, then
from context.config import settings
from context.driver import driver

"""Common hooks for any scenerio"""


@given(u'I load the website')
def load_website(context):
    driver.navigate(settings.url)


@given(u'I load the plaform main page')
def load_website(context):
    driver.navigate(settings.platform_url)
