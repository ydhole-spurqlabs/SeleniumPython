
Feature: API Testing
  @api
  Scenario: Verifying API GET response
    When : I request GET call using endpoint "/api/users/2"
    Then : I verify the status code with "200"


