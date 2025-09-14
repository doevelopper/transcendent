import json
import random
import string
from datetime import datetime

class DataGenerators:
    """Generators for test data."""
    
    @staticmethod
    def random_string(length=10):
        """Generate random string."""
        return ''.join(random.choices(string.ascii_lowercase, k=length))
    
    @staticmethod
    def random_email():
        """Generate random email."""
        username = DataGenerators.random_string(8)
        domain = random.choice(['example.com', 'test.com', 'demo.org'])
        return f"{username}@{domain}"
    
    @staticmethod
    def random_user():
        """Generate random user data."""
        return {
            'username': DataGenerators.random_string(8),
            'email': DataGenerators.random_email(),
            'created_at': datetime.now().isoformat()
        }
    
    @staticmethod
    def random_transaction(user_id=None):
        """Generate random transaction data."""
        return {
            'id': f"tx_{DataGenerators.random_string(6)}",
            'user_id': user_id or random.randint(1, 1000),
            'amount': round(random.uniform(10.0, 1000.0), 2),
            'type': random.choice(['credit', 'debit']),
            'timestamp': datetime.now().isoformat()
        }
    
    @staticmethod
    def generate_bulk_users(count=100):
        """Generate bulk user data."""
        return [DataGenerators.random_user() for _ in range(count)]
    
    @staticmethod
    def generate_bulk_transactions(count=100, user_ids=None):
        """Generate bulk transaction data."""
        if user_ids:
            return [DataGenerators.random_transaction(random.choice(user_ids)) for _ in range(count)]
        return [DataGenerators.random_transaction() for _ in range(count)]