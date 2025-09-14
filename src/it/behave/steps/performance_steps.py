from behave import given, when, then
import time
import threading
from concurrent.futures import ThreadPoolExecutor
from utils.api_client import ApiClient

@given('the system is under normal load')
def step_system_normal_load(context):
    context.load_level = 'normal'
    context.api_client = ApiClient(context.config['api_base_url'])

@when('I create {count:d} users simultaneously')
def step_create_users_simultaneously(context, count):
    def create_user(index):
        start_time = time.time()
        data = {'username': f'user_{index}', 'email': f'user_{index}@example.com'}
        response = context.api_client.post('/users', data)
        end_time = time.time()
        return {
            'response': response,
            'duration': end_time - start_time
        }
    
    context.start_time = time.time()
    with ThreadPoolExecutor(max_workers=10) as executor:
        context.results = list(executor.map(create_user, range(count)))
    context.end_time = time.time()

@then('the average response time should be less than {max_time:d}ms')
def step_average_response_time(context, max_time):
    durations = [result['duration'] for result in context.results]
    avg_duration = sum(durations) / len(durations)
    avg_ms = avg_duration * 1000
    assert avg_ms < max_time, f"Average response time {avg_ms}ms exceeds {max_time}ms"

@then('no errors should occur')
def step_no_errors(context):
    error_count = sum(1 for result in context.results if result['response'].status_code >= 400)
    assert error_count == 0, f"Found {error_count} errors"