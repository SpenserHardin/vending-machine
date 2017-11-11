Feature: Product Feature
  Acceptance criteria for selecting various products from the vending machine

  Scenario: Customer orders Chips
    Given I order "Chips" for ".50"
    When I select the respective button
    And I have inserted "2" "Quarter"
    Then the product is dispensed
    And the machine displays "Thank you"

  Scenario: Customer orders Cola
    Given I order "Cola" for "1.00"
    When I select the respective button
    And I have inserted "4" "Quarter"
    Then the product is dispensed
    And the machine displays "Thank you"

  Scenario: Customer orders Candy
    Given I order "Candy" for ".65"
    When I select the respective button
    And I have inserted "2" "Quarter"
    And I have inserted "1" "Dime"
    And I have inserted "1" "Nickle"
    Then the product is dispensed
    And the machine displays "Thank you"

  Scenario: Customer does not have enough coins to complete transaction
    Given I order "Candy" for ".65"
    When I select the respective button
    And I have inserted "2" "Quarter"
    Then the machine displays "Insert Coins"
