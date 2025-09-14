def before_all(context):
    """Setup before all tests."""
    context.config = {
        'api_base_url': 'http://localhost:8080/api',
        'timeout': 30
    }

def before_scenario(context, scenario):
    """Setup before each scenario."""
    context.test_data = {}

def after_scenario(context, scenario):
    """Cleanup after each scenario."""
    if hasattr(context, 'test_data'):
        context.test_data.clear()

def after_all(context):
    """Cleanup after all tests."""
    pass