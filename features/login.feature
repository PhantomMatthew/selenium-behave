@FRONT_END
Feature: Login

    Scenario: Login
        Given I load the plaform main page
        When I input username ""
        When I input captcha ""
        When I input validation code ""
        When I press the login button
        Then I should see content "" in the results
