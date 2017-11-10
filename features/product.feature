Feature: Product Feature
  Acceptance criteria for selecting various products from the vending machine

  Scenario: Customer orders Chips
    Given I order a "Chips"
    When I select the respective button
    And I have inserted enough money
    Then the product is dispensed
    And the machine displays "Thank you"
