Feature: Regression Suite
  As a QA engineer
  I want to run regression tests
  So that I can ensure new changes don't break existing functionality

  Scenario: User workflow regression
    Given a clean test environment
    When I execute the complete user workflow
    Then all user operations should work correctly
    And the data should be persisted properly

  Scenario: Integration points regression
    Given all services are running
    When I test all integration points
    Then all integrations should work correctly
    And no service should fail