import requests
import json

class ApiClient:
    """HTTP client for API testing."""
    
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    
    def get(self, endpoint, auth=True, **kwargs):
        """Send GET request."""
        url = f"{self.base_url}{endpoint}"
        if auth:
            self._add_auth_headers()
        return self.session.get(url, **kwargs)
    
    def post(self, endpoint, data=None, auth=True, **kwargs):
        """Send POST request."""
        url = f"{self.base_url}{endpoint}"
        if auth:
            self._add_auth_headers()
        json_data = json.dumps(data) if data else None
        return self.session.post(url, data=json_data, **kwargs)
    
    def put(self, endpoint, data=None, auth=True, **kwargs):
        """Send PUT request."""
        url = f"{self.base_url}{endpoint}"
        if auth:
            self._add_auth_headers()
        json_data = json.dumps(data) if data else None
        return self.session.put(url, data=json_data, **kwargs)
    
    def delete(self, endpoint, auth=True, **kwargs):
        """Send DELETE request."""
        url = f"{self.base_url}{endpoint}"
        if auth:
            self._add_auth_headers()
        return self.session.delete(url, **kwargs)
    
    def health_check(self):
        """Check if API is healthy."""
        try:
            response = self.get('/health', auth=False)
            return response.status_code == 200
        except requests.exceptions.ConnectionError:
            return False
    
    def _add_auth_headers(self):
        """Add authentication headers."""
        # In real implementation, add proper auth headers
        self.session.headers.update({
            'Authorization': 'Bearer test_token'
        })