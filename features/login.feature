@FRONT_END
Feature: Login

    Scenario: Login
        Given I load the plaform main page
        When I input username ""
        When I input captcha "0"
        When I input validation code ""
        When I press the login button
        Then I should see content "您已进入培训系统，所有的业务操作仅供培训及模拟操作使用，不会生效" in the results
