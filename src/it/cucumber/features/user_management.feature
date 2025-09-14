Feature: User Management
  As a system administrator
  I want to manage users
  So that I can control access to the system

  Scenario: Create a new user
    Given the system is running
    When I create a user with username "testuser" and email "test@example.com"
    Then the user should be created successfully
    And the user should have ID assigned

  Scenario: Login with valid credentials
    Given a user exists with username "testuser" and email "test@example.com"
    When I attempt to login with username "testuser"
    Then the login should be successful