Feature: Home page

  Background: Start from home page
    Given I am on home page

#  Scenario: Login page link work correctly
#    When I press "login" link
#    Then I am redirected to "login" page
#    And The title text is "Login Page"
#
#  Scenario: Forgot password link work correctly
#    When I press "forgot password" link
#    Then I am redirected to "forgot password" page
#    And The title text is "Forgot Password"
#
#  Scenario: Dropdown link work correctly
#    When I press "dropdown" link
#    Then I am redirected to "dropdown" page
#    And The title text is "Dropdown List"
#
  Scenario Outline: Home page links works correctly
    When I press <name_link> link
    Then I am redirected to <name_page> page
    And The title text is <page_title>

    Examples:
    |name_link           |name_page      |page_title     |
    |Form Authentication |login          |Login Page     |
    |Forgot Password     |forgot_password|Forgot Password|
    |Dropdown            |dropdown       |Dropdown List  |
