Breadth-first search (BFS) Algorithm is used

UASGE:

spath.py -i <inputfile> -o <outputfile> <start> <end>

OR

spath.py -i <inputfile> <start> <end>

Example:

inputfile:

1,2
1,6
2,3
2,4
4,5
3,5
3,9
9,10
9,11
10,11
9,8
6,5
6,7
5,7
7,8
8,12
11,12

> python paths.py -i graph.csv 1 12

1, 6, 7, 8, 12
1, 2, 3, 9, 8, 12
1, 2, 3, 9, 11, 12
1, 6, 5, 7, 8, 12
1, 2, 3, 5, 7, 8, 12
1, 2, 3, 9, 10, 11, 12
1, 2, 4, 5, 7, 8, 12
