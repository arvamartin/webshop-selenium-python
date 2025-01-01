Feature: Logout
  As a User, I want to logout from the website,
    so that I can sign out from my account

  Background:
    Given user is already on the login page
    When user enters username standard_user into username input
    And user enters password secret_sauce into password input
    And user clicks on login button


  Scenario:
    When user clicks on the menu button
    And user clicks on the logout button
    Then user is redirected to the login page