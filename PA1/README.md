# PA1 Part 1 by Brandon Cartwright, Johnatan Garcia, Dario Vasquez

Brandon Cartwright:

Contributed to loop structures in node traversal.
-Managed node creation and pathfinding logic.
-Collaborated in debugging sessions.
-Coded majority of A* algorithm

Dario Vazquez:

-Integrated file reading functionalities.
-Chose appropriate data structures (deque, sets).
-Assisted in refining code documentation and outputs.
-Coded majority of IDS algorithm

Johnatan Garcia:

-Led initial design of BFS algorithm.
-Managed edge case handling for grid boundaries.
-Led testing with various test cases.
-Coded majority of BFS algorithm

## Short Description and Instructions
For part 1 of this assignment, we have only implemented BFS by using a node class and some helper methods to aid with reading the test files and printing out relevant information. This code is written in Python.

To run this, you can use a standard "python3 PA1Part1V2.py" command. Once running, the program will ask which test file you would like to run i.e. "Test1.txt".

For Part 2 of this assignment, we have implemented IDS and A* in addition to the already implemented BFS. WE have also added several more test cases. To run this, the standard
"python3 PAPart2.py" command should work. As before, the program will ask which test file you would like to run i.e. "Test2.txt".

## Algorithm comparison
As far as total cost, A* was the most expensive in our testing, with IDS and BFS following respectively. However, BFS was the algorithm that expanded the most nodes followed closely by A*. IDS was considerably more efficient
in terms of node expansion. For nodes stored in memory, A* had the most, with IDS and BFS having considerably less. Finally, for time, IDS was the fastest with A* and BFS performing quite similarly. Each algorithm has its
advantages and disadvantages, but for our test cases, IDS seems to be the most balanced approach. 
