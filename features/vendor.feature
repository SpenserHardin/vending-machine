Feature: Vendor Feature
  Acceptance criteria for the vending machine

  Scenario: Customer orders a coke
    Given I am a vendor
    When I order a "Coke"
    Then the displays says "Insert Coins"

  Scenario: Customer pays for item
    Given I am a vendor
    And order a "Coke" for "1" dollar
    When I insert "1"
    Then the displays says "Thank you"

  Scenario: Customer pays for item
    Given I am a vendor
    And order a "Coke" for "1" dollar
    When I insert ".50"
    Then the displays says "Insert Coins"

  Scenario: Customer pays for item
    Given I purchase a "Coke" for "1"
    And I have inserted ".50"
    And display says "Insert Coins"
    When I insert another ".50"
    Then the displays says "Thank you"

  Scenario: Customer pays for item
    Given I purchase a "Coke" for "1"
    And I have inserted ".75"
    And display says "Insert Coins"
    When I insert another ".50"
    Then the displays says "Thank you"
    And ".25" cents is returned

