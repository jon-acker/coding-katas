#### Rules

 - A `game` starts with an empty 3x3 `grid`
 - Two `players`, one plays `symbol` X the other plays `symbol` O
 - `player` can place symbol in any `square` that's not taken
 - If `player` tried to place `symbol` in already taken `squares`, they are told "cannot play that position"
 - When all 9 `squares` are full - the game is over and ends with `tie`
 - The first player to have 3 of their symbols in a diagonal, row or column wins


```gherkin
    Scenario: Placing a symbol in square that is free
        Given the square 1,1 is free
        When player X plays the square 1,1
        Then the grid should have an X in square 1,1
      
    Scenario: Being told cannot place symbol in already taken square
        Given the square 1,1 has already been taken
        When player X plays the square 1,1
        Then player should be told "square has already been taken"
    
    Scenario: Being told the same symbol cannot be played twice
        Given player X has just played
        When a player tries to play an X
        Then the player should be told "same symbol cannot be played twice"
        
    Scenario: Player X wins when they have 3 in a diagonal
        Given the state of the grid is:
"""
X _ _
_ X _
_ _ _
""" 
        When player places an X in square 3,3
        Then player X should have won
        And player O should have lost
        
alternaltely:

  Scenario: Player X wins when they have 3 in a diagonal
    Given the following moves have been played:
      | Player | Square |
      | X      | 1,1    |
      | O      | 1,2    |
      | X      | 2,2    |
      | O      | 2,3    |
    When player plays an X in square 1,3
    Then player X should have won


    Scenario: Player X wins when they have 3 in a row
        Given the state of the grid is:
"""
X X _
_ _ _
_ _ _
""" 
        When player places an X in square 1,3
        Then player X should have won
        And player O should have lost    
```
