from behave import *

use_step_matcher("re")

@given(': I enter the "(?P<Age>.+)"')
def step_impl(context, Age):
    context.bmipage.age_input(Age)


@when(': I Click on "(?P<Gender>.+)"')
def step_impl(context, Gender):
    context.bmipage.gender_radio(Gender)

@step(': I Enter a "(?P<height>.+)"')
def step_impl(context, height):
    context.bmipage.height_input(height)

@step(': I Enter the "(?P<weight>.+)"')
def step_impl(context, weight):
    context.bmipage.weight_input(weight)

@step(": I Click on Calculate btn")
def step_impl(context):
    context.bmipage.calculatebtn_click()

@step(': I Verify Result with "(?P<expresult>.+)"')
def step_impl(context, expresult):
    context.bmipage.result_validation(expresult)