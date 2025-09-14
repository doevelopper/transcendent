from behave import given, when, then
import requests
from utils.api_client import ApiClient

@given('the API is running')
def step_api_running(context):
    context.api_client = ApiClient(context.config['api_base_url'])
    context.api_running = context.api_client.health_check()
    assert context.api_running, "API is not running"

@when('I send a GET request to "{endpoint}"')
def step_send_get_request(context, endpoint):
    context.response = context.api_client.get(endpoint)

@when('I send a POST request to "{endpoint}" with data')
def step_send_post_request_with_data(context, endpoint):
    data = {}
    for row in context.table:
        data[row['username']] = row['email']
    context.response = context.api_client.post(endpoint, data)

@then('the response status should be {status:d}')
def step_response_status(context, status):
    assert context.response.status_code == status, f"Expected {status}, got {context.response.status_code}"

@then('the response should contain {content}')
def step_response_contains(context, content):
    response_data = context.response.json()
    assert content.replace(' ', '_').lower() in str(response_data).lower()