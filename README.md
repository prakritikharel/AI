# AI
AI Projects

Project 1: AI Puzzle: A game of Cat and Mouse

 The aim of the puzzle is for the Cat to catch the mouse before the mouse eats all the cheese. 
The number of cheese and the initial position of the cat and mouse are randomly determined. 

The mouse moves are similar to those of the king in a game of chese, it can move in all 8 directons, but can only move one square at
a time. It will find the closest chess and move towards it. 

The cat's moves are similar to those of the knight in a game of chess. 

Every time, a mouse makes a move, the cat makes a move. The mouse's moves are predetermined, the cat's moves are determined by the AI

There are 5 implementations: 
1. BFS
2. DFS
3. A* with 3 heuristics descibes below. 


My state space is a double array of 0 and the chars (H, C, M), H represents the cheese, C represents the cat and M represents the mouse.
The position of all three chars are randomly chosen. Through all the states, the position of H remains the same, 
unless the mouse eats it, the mouse moves in a king-like (from chess) pattern and the cat moves in a knight-like pattern
depending on the algorithm used. 

Heuristic 1— Calculating the distance

As mentioned above the cat can move in 8 different positions. The production system is [left, topleft, topright, up, down bottom left, right, bottomright]. 

I wanted to figure a way to put the production system in a prioritized order, so that the first couple of moves are the ones that are closer to where the mouse is.

 I accomplished this by calculating the distance and reordering the array based on their distance from shortest distance to largest distance. The first item in the array is where the cat is moved since it is the next best move. 

The algorithm
First I check where the current cat is, If the mouse is where the current cat is, then exit. If not, then expand that node, this will return an array with the next possible steps. 
 
Calculate the distance from each node in the array to the position of the mouse. Sort that array so that it is in increasing order. 

Remove the first element and set the current cat to be the node in pos 1 and restart the cycle. 
 

Heuristic 2 — Dividing the production system into 4 quadrants
For this heuristic, instead of taking into account all the elements in the production system, I wanted to take into account just the ones that are necessary. 

The production system is divided into 4 different quadrants. 

               Quadrant 1 consists of the left and top-left  moves 
  1 | 2       Quadrant 2 consists of the top-right and up moves
  3 | 4      Quadrant 3 consists of the down and bottom-left moves
               Quadrant 4 consists of the right and bottom-right moves

Depending on the x and the y coordinates of the cat’s current position and the mouse’s current position, only the two nodes in one of the 4 quadrants is expanded.

Algorithm
Compare the x coordinates and the y coordinates of the current cat’s position and the current mouse position. Only examines the quadrant where the mouse is the closest. 

For example, if the mouse is at position 3,4 and the cat is at position  2 3. Then compare the x values, since the x coordinate of the cat is less than the x coordinate of the mouse, we know that we need to examine either quadrant 3 or quadrant 4. 

Next compare the y coordinate of the cat and mouse. The y coordinate of cat < y coordinate of the mouse, therefore, we know we only need to examine quadrant 4 since it is the closes to the mouse. So we do a DFS search with 2 items in our production system instead of 8. 

Heuristic 3 — A mix of heuristic 1 and 2

Heuristic 3 is a combination of heuristic 1 and heuristic 2. The aim was to reduce the production system to 1 instead of 2 as done in heuristic 2.

It first figures out what quadrant is the closest to the mouse, after this we will have reduced to the production system to two items (as discussed in heuristic 2)

Next, it checks the distance of those two items (for example if in quadrant 4, then it checks the distance of right and bottom-right pos), 
the item with the least distance is the only one in our production system, so the cat is moved to the position. This cycle is repeated until the mouse is caught. 


