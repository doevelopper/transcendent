import json
import yaml
import os

class TestHelpers:
    """Helper utilities for integration tests."""
    
    def __init__(self):
        self.fixtures_dir = os.path.join(os.path.dirname(__file__), '..', 'fixtures')
    
    def load_test_data(self, filename):
        """Load test data from JSON file."""
        filepath = os.path.join(self.fixtures_dir, filename)
        with open(filepath, 'r') as f:
            return json.load(f)
    
    def load_config(self, filename):
        """Load configuration from YAML file."""
        filepath = os.path.join(self.fixtures_dir, filename)
        with open(filepath, 'r') as f:
            return yaml.safe_load(f)
    
    def cleanup_test_data(self):
        """Clean up test data after tests."""
        # Implementation to clean up test database
        pass
    
    def generate_test_user(self, index=1):
        """Generate test user data."""
        return {
            'username': f'testuser_{index}',
            'email': f'test_{index}@example.com'
        }
    
    def generate_test_transaction(self, user_id, amount=100.0):
        """Generate test transaction data."""
        return {
            'user_id': user_id,
            'amount': amount,
            'type': 'credit' if amount > 0 else 'debit'
        }