Feature: Performance Testing
  As a system administrator
  I want to test system performance
  So that I can ensure the system meets performance requirements

  Scenario: Response time for user creation
    Given the system is under normal load
    When I create 100 users simultaneously
    Then the average response time should be less than 500ms
    And no errors should occur

  Scenario: Database query performance
    Given the database contains 10000 users
    When I query for users by email
    Then the query should complete in less than 100ms