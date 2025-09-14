Feature: API Testing
  As a developer
  I want to test the REST API endpoints
  So that I can ensure they work correctly

  Scenario: Get user information
    Given the API is running
    When I send a GET request to "/users/1"
    Then the response status should be 200
    And the response should contain user data

  Scenario: Create a new user via API
    Given the API is running
    When I send a POST request to "/users" with data:
      | username | email           |
      | testuser | test@example.com |
    Then the response status should be 201
    And the response should contain the created user ID