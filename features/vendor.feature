Feature: Vendor Feature
  Acceptance criteria for the vending machine

  Scenario: Customer orders a coke
    Given I am a vendor
    When I order a "Coke"
    Then the displays says "Insert Coin"