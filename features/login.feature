Feature: Login
  As a User, I want to login to the website,
      so that I can access the products.


  Scenario: User can login with valid credentials
    Given user is already on the login page
    When user enters username standard_user into username input
    And user enters password secret_sauce into password input
    And user clicks on login button
    Then user is on the home page


  Scenario: User cannot login with invalid credentials
    Given user is already on the login page
    When user enters username not-valid-username into username input
    And user enters password not-valid-password into password input
    And user clicks on login button
    Then user remained on the login page