
Feature: Create test cases using Selenium with Python to automate below BMI calculator tests

  @bmi
  Scenario Outline: Calculate BMI value by passing the inputs from the table
    Given  : I enter the "<Age>"
    When   : I Click on "<Gender>"
    And   : I Enter a "<Height>"
    And   : I Enter the "<Weight>"
    And   : I Click on Calculate btn
    And   : I Verify Result with "<Expected Result>"
    Examples:

      | Age | Gender  | Height  | Weight  | Expected Result |
      | 20  | Male    |  180    |  60     | BMI = 18.5 kg/m2|
      | 35  | Female  |  160    |  55     | BMI = 21.5 kg/m2|
      | 50  | Male    |  175    |  65     | BMI = 21.2 kg/m2|
      | 45  | Female  |  150    |  52     | BMI = 23.1 kg/m2|
