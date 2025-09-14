Feature: Transaction Processing
  As a user
  I want to process transactions
  So that I can manage my finances

  Scenario: Process a valid transaction
    Given I have a user account
    When I process a transaction of amount 100.50 with type "credit"
    Then the transaction should be processed successfully
    And the transaction should be recorded in the database

  Scenario: Reject invalid transaction
    Given I have a user account
    When I process a transaction of amount -50.00 with type "debit"
    Then the transaction should be rejected
    And an error message should be displayed