## Tennis Game Kata



### Rules:
1. A game is won by the first player to have won at least four points in total and at least two points more than the opponent.

2. The running score of each game is described in a manner peculiar to tennis: scores from zero to three points are described as “Love”, “Fifteen”, “Thirty”, and “Forty” respectively.

3. If at least three points have been scored by each player, and the scores are equal, the score is “Deuce”.

4. If at least three points have been scored by each side and a player has one more point than his opponent, the score of the game is “Advantage” for the player in the lead.


Create an application with more than one class. The application allows the user to score a point in a game, and produces an updated display of the score in words.

Persist the score in filesystem (or something similarly easy), and set it up for each `Given` step.

Use *Behat* or *Cucumber-js* to execute scenarios.

`bin/behat` 

(with docker: `docker-compose exec php bin/behat`)

or

`node_modules/.bin/cucumber-js`

(with docker: `docker-compose exec node node_modules/.bin/cucumber-js`)

Examples:

```gherkin
Feature: Displaying correct scoreboard in a tennis game

    Scenario: Displaying Love All when neither players have scored a point
        Given neither player have scored a point
        When the game is started
        Then the scoreboard should display "Love All" 
        
    Scenario: Showing Fifteen - Love when one players scores a point
        Given neither player have scored a point
        When "Player One" scores a point
        Then the scoreboard should display "Fifteen - Love" 

    Scenario: Showing Fifteen - All when both players score a point
        Given "Player One" has already scored one point
        When "Player Two" scores a point
        Then the scoreboard should display "Fifteen - All" 
```