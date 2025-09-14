Feature: Data Validation
  As a developer
  I want to validate data inputs
  So that the system maintains data integrity

  Scenario: Validate user email format
    Given the validation system is active
    When I validate email "test@example.com"
    Then the validation should pass

  Scenario: Reject invalid email format
    Given the validation system is active
    When I validate email "invalid-email"
    Then the validation should fail
    And an appropriate error message should be returned