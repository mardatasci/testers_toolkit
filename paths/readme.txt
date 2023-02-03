Usage:
- CSV file contains the edges between vertices.

example input.csv

1,6
1,2
2,3
3,4
4,5
5,6


This CSV file represents a graph with 6 vertices and 5 edges.
The first row 1,6 indicates that the start vertex is 1 and the end vertex is 6.
The remaining rows 1,2, 2,3, 3,4, 4,5, and 5,6 represent the edges between vertices.
In this case, there are multiple paths from vertex 1 to vertex 6,
such as 1 -> 2 -> 3 -> 4 -> 5 -> 6 and 1 -> 2 -> 3 -> 4 -> 5 -> 6.