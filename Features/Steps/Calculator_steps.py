from behave import *
from selenium import webdriver
import json

data = json.load(open("Resources/config.json"))
use_step_matcher("re")


# @given(": User is on calculator page")
# def step_impl(context):
#     # context.driver.get(data['WEBURL'])
#     context.driver.implicitly_wait(5)


@when(": User enters following inputs")
def step_impl(context):
    context.calpage.enter_number(context.table)


@step(": User click on calculate button")
def step_impl(context):
    context.calpage.calculatebtn_click()


@then(": User verifies the actual result with expected result")
def step_impl(context):
    context.calpage.verify_result()
