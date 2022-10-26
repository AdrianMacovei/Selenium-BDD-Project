Feature: Login Page

#  Scenario: Login with valid credentials
#    Given I am on login page
#    When I enter username "tomsmith"
#    And I enter password "SuperSecretPassword!"
#    And I press login button
#    Then I will <action> the secure page
#    And A message with text <text_message> appears

    Scenario Outline: Login with valid/invalid credentials
      Given I am on login page
      When I enter "username" <username>
      And I enter "password" <password>
      And I press login button
      Then I will <action> the <page_name> page
      And A message with text "<text_message>" appears

    Examples: Login with invalid credentials

      |username|password            |text_message                  |action          |page_name|
      |tomsmith|SuperSecretPassword!|You logged into a secure area!|be redirected to|secure   |
      |tomsmith|something           |Your password is invalid!     |remain on       |login    |
      |tomsmith|423432452           |Your password is invalid!     |remain on       |login    |
      |tomsmith|something!342       |Your password is invalid!     |remain on       |login    |
      |tomsmith|None                |Your password is invalid!     |remain on       |login    |
      |None    |SuperSecretPassword!|Your username is invalid!     |remain on       |login    |
      |username|SuperSecretPassword!|Your username is invalid!     |remain on       |login    |
      |13213213|SuperSecretPassword!|Your username is invalid!     |remain on       |login    |
      |username|something           |Your username is invalid!     |remain on       |login    |


    Scenario: Message x close button work correctly on login page
      Given ALl steps in scenario "Login with valid/invalid credentials" are done
      When I press x button on the message
      Then Message will not be displayed

