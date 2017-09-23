Feature: Vendor Feature
  Acceptance criterai for the vending machine

  Scenario: Accepts Coins
    Given I am a vendor
    When I give the vending machine coins
    Then the machine collects the money