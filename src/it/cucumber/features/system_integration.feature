Feature: System Integration
  As a system architect
  I want to test system components integration
  So that I can ensure the system works as a whole

  Scenario: Database connection integration
    Given the application is started
    When I attempt to connect to the database
    Then the connection should be established successfully

  Scenario: Service layer integration
    Given the database is connected
    When I call the data service to save data
    Then the data should be persisted correctly
    And the service should return success status