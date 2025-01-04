Feature: Filter
    As a User, I want to select a filter option,
      so that I can easily find the correct product

  Background:
    Given user is already on the login page
    When user enters username standard_user into username input
    And user enters password secret_sauce into password input
    And user clicks on login button
    Then user is on the home page


    Scenario:
      When user selects hilo option
      Then user sees Sauce Labs Fleece Jacket named product