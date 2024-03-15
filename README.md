****Pichu Pathfinding Solver****

**Problem Description**

In this problem, Pichu needs to navigate through a map with walls represented as "X" and possible paths represented as ".". Pichu starts at position P and needs to reach the destination "@" while avoiding obstacles. The goal is to find the shortest path for Pichu to reach the destination.
* **Initial State:** Pichu starts at position P on the map.
* **Goal State:** Pichu reaches the destination "@".
* **Successor States:** Pichu can move up, down, left, or right, traversing through the dots on the map to reach the goal state.
* **State Space:** Set of all possible states Pichu traverses before reaching the goal state.
  
***Programming Modifications***

**Moves Function:**
* Added moves "U" (up), "D" (down), "L" (left), and "R" (right) to the moves function to simplify checking Pichu's movement direction.

**Search Function:**
* Implemented Breadth First Search (BFS) algorithm to find the shortest path for Pichu.
* Added a list named "traversed" to keep track of visited nodes/states, preventing Pichu from moving indefinitely.
* Appended an extra string in the fringe list to keep track of the path Pichu is traveling.

**Heuristic Function**

A heuristic function based on Euclidean distance/Manhattan distance is calculated to increase Pichu's efficiency in reaching the goal state. This function ensures that Pichu always chooses the minimal distance as the next move.

****Pichu Placement Puzzle Solver****

**Problem Description**

In this puzzle, there are K number of Pichus on a map, and none of them can be situated such that one Pichu may be seen by another in the same row, column, or diagonal. The goal is to find valid positions to place the Pichus on the map.

* **Initial State:** Map with walls represented as "X" and possible paths represented as ".".
* **Goal State:** All Pichus are placed on the map without any being visible to another in the same row, column, or diagonal.
* **Successor Function:** Returns feasible states from a given state, adhering to the restrictions of rows, columns, and diagonals.
* **State Space:** Set of all possible valid placements for Pichus on the map.

***Programming Modifications***

**RowCol_check and Diag_check Functions:**

Implemented recursive functions to check for valid successor states, ensuring no Pichu is in the same row, column, or diagonal.

**Solve Function:**

Included the "traversed" list in the successor function to keep track of visited states, preventing infinite loops.

**Conclusion**

The modifications made to the program ensure efficient pathfinding and valid placement of Pichus on the map, providing optimal solutions to the respective puzzles.

