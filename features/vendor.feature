Feature: Vendor Feature
  Acceptance criteria for the vending machine

  Scenario: Customer orders a coke
    Given I am a vendor
    When I order a "Coke"
    Then the displays says "Insert Coins"

  Scenario: Customer pays for item
    Given I am a vendor
    And order a "Coke" for ".25" dollar
    When I insert ".25"
    Then the displays says "Thank you"

  Scenario: Customer pays for item
    Given I am a vendor
    And order a "Coke" for ".50" dollar
    When I insert ".25"
    Then the displays says "Insert Coins"

  Scenario: Customer pays for item
    Given I purchase a "Coke" for ".50"
    And I have inserted ".25"
    And display says "Insert Coins"
    When I insert another ".25"
    Then the displays says "Thank you"

  Scenario: Customer pays for item
    Given I purchase a "Coke" for ".50"
    And I have inserted ".30"
    And display says "Insert Coins"
    When I insert another ".25"
    Then the displays says "Thank you"
    And ".05" cents is returned

