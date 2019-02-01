## Tennis Game Kata



### Rules:
1. A game is won by the first player to have won at least four points in total and at least two points more than the opponent.

2. The running score of each game is described in a manner peculiar to tennis: scores from zero to three points are described as “Love”, “Fifteen”, “Thirty”, and “Forty” respectively.

3. If at least three points have been scored by each player, and the scores are equal, the score is “Deuce”.

4. If at least three points have been scored by each side and a player has one more point than his opponent, the score of the game is “Advantage” for the player in the lead.


Create a `Game` class with a method that allows each player to `score` a point, and another method that returns a string representing the current score: 

Examples:
 - No players have scored:
 
 `$game->displayScore()`: `Love all`

- One player has scored:

 `$game->scorePoint('player1')`
 
 `$game->displayScore()`: `Fifteen - Love`
 
- Both players have scored:

 `$game->scorePoint('player1')`
 
 `$game->scorePoint('player2')`
    
 `$game->displayScore()`: `Fifteen all`

