import collections

def greedyAlgorithm () :
    grid = [[0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]]

    for i in len(grid):
        for j in len(grid):
            print(grid[i][j])
            j=j+1
        i=i+1

    