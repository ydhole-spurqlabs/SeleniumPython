Feature: Calculator Functionality

  @cal
  Scenario: Validate functionality of calculator using data table
    When  : User enters following inputs
      | num1   | Operator | num2 |
      | 352454 | +        | 2    |
    And   : User click on calculate button
    Then  : User verifies the actual result with expected result