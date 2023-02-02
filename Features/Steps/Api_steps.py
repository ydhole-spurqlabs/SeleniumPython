from behave import *
from Utility.API_Utility import API_Utility
use_step_matcher("re")

api_utility = API_Utility()


@when(': I request GET call using endpoint "(?P<endpoint>.+)"')
def step_impl(context,endpoint):
    global response
    response = api_utility.GET_Call(endpoint)
    print(response.status_code)


@then(': I verify the status code with "(?P<status_code>.+)"')
def step_impl(context,status_code):
    if response.status_code == 200:
        print("Pass")

    else:
        print("Fail")


