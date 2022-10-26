Feature: Secure Page

  Scenario: Secure page right redirect
    Given I am on the secure page
    When Page finish to load
    Then A message with text "You logged into a secure area!" appears
    And The title text is Secure Area

  Scenario: Secure page logout successfully
    Given I am on the secure page
    When I press logout button
    Then I am redirected to login page
    And A message with text "You logged out of the secure area!" appears
    And The title text is "Login Page"

  Scenario: Secure page x button close massage
    Given I am on the secure page
    And A message with text "You logged into a secure area!" appears
    When I press x button on the message
    Then Message will not be displayed



