To run the program, execute the MCO1.exe
This was compiled in a windows environment. 

The program will ask a path to graph file. This could either be absolute or relative file path.
For relative file path, since the file is already in the same folder as the executable, you may enter: graph.txt

Enter the correct file. If not, the program will exit.

To create your own graph STRICTLY follow the format below (without the < >)

<name of node> : (<name of neighbor node>,<edge weight>) (<name of neighbor node>,<edge weight>)

As seen in the format, a neighboring node is represented with a parenthesis (). Neighbors are separated with a WHITESPACE.

There is NO WHITESPACE in-between the comma separating the name of neighbor node and edge weight

Also notice the space between the colon " : "

With nodes without neighbors, put an empty parenthesis ()

For additional nodes, enter a new line
Example:
S : (A,5) (D,6) (B,9)
A : (B,3) (G1,9)
B : ()

With node S having 3 neighbors and Node A having 2 neighbors