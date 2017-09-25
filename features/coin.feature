Feature: Vending Machine accepts Quarters, Dimes, and Nickles. It does not accept pennies

  Scenario: Vending Machine accepts quarters
    Given I have a "Quarter"
    When I insert a "Quarter" into the vending machine
    Then the vending machine accepts the "Quarter"