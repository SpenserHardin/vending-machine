Feature: Payment Feature
  Acceptance criteria for the vending machine

  Scenario: Customer orders an item
    Given I am a vendor
    When I order an item
    Then the displays says "Insert Coins"

  Scenario: Customer pays for item
    Given I am a vendor
    And order an item for ".25" dollar
    When I insert ".25"
    Then the displays says "Thank you"

  Scenario: Customer pays for item
    Given I am a vendor
    And order an item for ".50" dollar
    When I insert ".25"
    Then the displays says "Insert Coins"

  Scenario: Customer pays for item
    Given I purchase an item for ".50"
    And I have inserted ".25"
    And display says "Insert Coins"
    When I insert another ".25"
    Then the displays says "Thank you"

  Scenario: Customer pays for item
    Given I purchase an item for ".50"
    And I have inserted ".30"
    And display says "Insert Coins"
    When I insert another ".25"
    Then the displays says "Thank you"
    And ".05" cents is returned

