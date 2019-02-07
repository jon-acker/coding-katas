Feature: Displaying correct scoreboard in a tennis game

  Scenario: Displaying Love All when neither players have scored a point
    Given neither player have scored a point
    When the game is started
    Then the scoreboard should display "Love All"

  Scenario: Showing Fifteen - Love when one players has scored a point
    Given neither player have scored a point
    When "Player One" scores a point
    Then the scoreboard should display "Fifteen - Love"