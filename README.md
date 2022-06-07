# A* Search
solving the 8-tile puzzle we have discussed in class. The 8-tile puzzle was invented and popularized by Noyes Palmer Chapman in the 1870s. It is played on a 3x3 grid with 8 tiles labeled 1 through 8 and an empty grid. The goal is to rearrange the tiles so that they are in order.

You solve the puzzle by moving the tiles around. For each step, you can only move one of the neighbor tiles (left, right, top, bottom) into an empty grid. And all tiles must stay in the 3x3 grid. An example is shown in the picture below. In this example, there are only 2 valid moves, i.e., either moving 6 down or moving 1 right.

![image](https://user-images.githubusercontent.com/54726422/172276771-5cb7e13a-0a94-4652-80e5-85e04627d847.png)

## Program Specification

### Goal State
The goal state of the puzzle is [1, 2, 3, 4, 5, 6, 7, 8, 0], or visually:
![image](https://user-images.githubusercontent.com/54726422/172276834-bd73cfd2-db70-4067-b931-080f3a4fce5e.png)

### Heuristic
use the sum of Manhattan distance of each tile to its goal position as our heuristic function

### Functions
1. print_succ(state) — given a state of the puzzle, represented as a single list of integers with a 0 in the empty space, print to the console all of the possible successor states
2. solve(state) — given a state of the puzzle, perform the A* search algorithm and print the path from the current state to the goal state
