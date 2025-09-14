from behave import given, when, then
from utils.api_client import ApiClient

@when('I send a POST request with SQL injection payload to "{endpoint}"')
def step_sql_injection_attempt(context, endpoint):
    malicious_data = {
        'username': "admin'; DROP TABLE users; --",
        'email': 'test@example.com'
    }
    context.api_client = ApiClient(context.config['api_base_url'])
    context.response = context.api_client.post(endpoint, malicious_data)

@when('I send a GET request to "{endpoint}" without authentication')
def step_request_without_auth(context, endpoint):
    context.api_client = ApiClient(context.config['api_base_url'])
    context.response = context.api_client.get(endpoint, auth=False)

@then('the request should be rejected')
def step_request_rejected(context):
    assert context.response.status_code >= 400, f"Request was not rejected, got status {context.response.status_code}"

@then('no database modification should occur')
def step_no_db_modification(context):
    # Check that database structure is intact
    health_response = context.api_client.get('/health')
    assert health_response.status_code == 200, "Database appears to be compromised"

@then('an authentication error should be returned')
def step_auth_error_returned(context):
    assert context.response.status_code == 401, f"Expected 401, got {context.response.status_code}"
    response_data = context.response.json()
    assert 'authentication' in str(response_data).lower() or 'unauthorized' in str(response_data).lower()