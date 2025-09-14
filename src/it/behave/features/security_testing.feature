Feature: Security Testing
  As a security engineer
  I want to test security features
  So that I can ensure the system is secure

  Scenario: SQL injection prevention
    Given the API is running
    When I send a POST request with SQL injection payload to "/users"
    Then the request should be rejected
    And no database modification should occur

  Scenario: Authentication required
    Given the API is running
    When I send a GET request to "/protected-endpoint" without authentication
    Then the response status should be 401
    And an authentication error should be returned