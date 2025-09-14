from behave import given, when, then
from utils.api_client import ApiClient
from utils.test_helpers import TestHelpers

@given('a clean test environment')
def step_clean_environment(context):
    context.test_helpers = TestHelpers()
    context.test_helpers.cleanup_test_data()
    context.api_client = ApiClient(context.config['api_base_url'])

@when('I execute the complete user workflow')
def step_complete_user_workflow(context):
    # Create user
    create_response = context.api_client.post('/users', {
        'username': 'workflow_user',
        'email': 'workflow@example.com'
    })
    context.user_id = create_response.json().get('id')
    
    # Update user
    update_response = context.api_client.put(f'/users/{context.user_id}', {
        'email': 'updated@example.com'
    })
    
    # Get user
    get_response = context.api_client.get(f'/users/{context.user_id}')
    
    context.workflow_results = {
        'create': create_response,
        'update': update_response,
        'get': get_response
    }

@then('all user operations should work correctly')
def step_all_operations_work(context):
    for operation, response in context.workflow_results.items():
        assert response.status_code < 400, f"{operation} operation failed with status {response.status_code}"

@then('the data should be persisted properly')
def step_data_persisted(context):
    get_response = context.api_client.get(f'/users/{context.user_id}')
    user_data = get_response.json()
    assert user_data['email'] == 'updated@example.com', "Data was not persisted correctly"