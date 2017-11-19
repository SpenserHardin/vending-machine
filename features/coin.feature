Feature: Vending Machine accepts Quarters, Dimes, and Nickles. It does not accept pennies

  Scenario: Vending Machine accepts quarters
    Given I have a "Quarter"
    When I insert a "Quarter" into the vending machine
    Then the vending machine accepts the "Quarter"

  Scenario: Vending Machine accepts Dimes
    Given I have a "Dime"
    When I insert a "Dime" into the vending machine
    Then the vending machine accepts the "Dime"

  Scenario: Vending Machine accepts Nickels
    Given I have a "Nickel"
    When I insert a "Nickel" into the vending machine
    Then the vending machine accepts the "Nickel"

  Scenario: Vending Machine does not accept Pennies
    Given I have a "Penny"
    When I insert a "Penny" into the vending machine
    Then the vending machine does not accepts the coin