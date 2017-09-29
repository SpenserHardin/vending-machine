Feature: Vending Machine accepts Quarters, Dimes, and Nickles. It does not accept pennies

  Scenario: Vending Machine accepts quarters
    Given I have a "Quarter"
    When I insert a "Quarter" into the vending machine
    Then the vending machine accepts the "Quarter"

  Scenario: Vending Machine accepts quarters
    Given I have a "Dime"
    When I insert a "Dime" into the vending machine
    Then the vending machine accepts the "Dime"

  Scenario: Vending Machine accepts quarters
    Given I have a "Nickle"
    When I insert a "Nickle" into the vending machine
    Then the vending machine accepts the "Nickle"  