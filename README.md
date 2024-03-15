#route_pichu.py:

#PROGRAMMING MODIFICATIONS:
moves function:
- add U,D,L,R in the moves function so that it makes it easier to check in which direction pichu is moving.
- in moves function moves is defined is a tuple.

search function:
- here in the function already given, the pichu is moving without stop since it is not keeping track of the already visited nodes/states. So, I have initialized a new list traversed to keep track of the visited nodes and also appended an extra string in the fringe list to keep track of the path in which pichu is travelling.
 
#INFERENCE:

Initial State : Map has walls represented as "X" and possible path repredented as ".". P is the initial state of Pichu.
Goal State: "@" is the destination for pichu. Thus, when pichu reaches @, that is the goal state.
Successor states: Pichu will follow the dots checking all the 4 directions up, down,left and right and then traverse through the dots to reach the goal state in a direction which satisfies the problem conditions.
State Space: Set of all the states in the map that pitchu traverses before reaching the goal state @

The logic used here is Breadth First Search since it gives us the most optimum solution to find the shortest path in which pichu can reach its goal state as BFS implements its searching algorithm moving ahead in all the successor states/nodes to find the goal state(i.e., "@"). Heuristic functions which include Euclidean distance/Manhattan distance is calculated here to increase the efficieny of Pichu to reach its goal state. This method is generally considered as an admissable function since it moves ahead to the next move based on its distance from the goal state and always chooses the minimal one as next move.

#arrange_pichus.py:

#PROGRAMMING MODIFICATIONS:
RowCol_check and Diag_check functions):
- I have implemented different function to check the valid successor state for a pichu.
-Each of these function are recursive and will keep calling themselvs each time they didn't find a correct possible successor state i.e., position which has no pitchu in the same row,column and diagonal. 
(Ucheck, Dcheck, Lcheck and Rcheck for rows and columns)
(UpperLeft, UpperRight,LowerLeft and LowerRight for diagonals)

solve function:
- I have also included the traversed list in the successor function to keep track of the already visited states so they are not tested again which saves us from infinite loop.

#INFERENCE:

Initial State : Map has walls represented as "X" and possible path repredented as ".". P is the initial state of Pichu.
Goal State: There are K number of pichus on the map, and none of them are situated so that one of them may be seen by another in the same row, column, or diagonal.
Successor function: By adhering to the restrictions of rows, columns, and diagonals, this function returns all feasible states from a given state, i.e., states where another pichu can be inserted.
State Space: Pichu is placed wherever it can be in the house_map in all of the states in this set.

The traversal technique used here is BFS which can let us traverse through all the nodes in an order. A heuristic function which is distance of the pitchu from its goal position is used. this will help us increase the efficiency since while checking the states the once with the least distance from the goal state in the fringe are popped first and visited.



##I have discussed the solution with my classmate Thumma Prathyusha Reddy - pthumma
