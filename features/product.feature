Feature: Product Feature
  Acceptance criteria for selecting various products from the vending machine

  Scenario: Customer orders Chips
    Given I order a "Chips"
    When I select the respective button
    And I have inserted "2" "Quarter"
    Then the product is dispensed
    And the machine displays "Thank you"

  Scenario: Customer orders Cola
    Given I order a "Cola"
    When I select the respective button
    And I have inserted "4" "Quarter"
    Then the product is dispensed
    And the machine displays "Thank you"
