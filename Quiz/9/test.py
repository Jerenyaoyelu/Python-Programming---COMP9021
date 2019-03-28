# Randomly fills a grid of size 7 x 7 with NE, SE, SW, NW,
# meant to represent North-East, South-East, North-West, South-West,
# respectively, and starting from the cell in the middle of the grid,
# determines, for each of the 4 corners of the grid, the preferred path amongst
# the shortest paths that reach that corner, if any. At a given cell, it is possible to move
# according to any of the 3 directions indicated by the value of the cell;
# e.g., from a cell storing NE, it is possible to move North-East, East, or North.
# At any given point, one prefers to move diagonally, then horizontally,
# and vertically as a last resort.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, choice
from queue_adt import *

move_dict={'E':(1,0),'S':(0,1),'W':(-1,0), 'N':(0,-1)}
move_priority = {'E':2,'S':1,'W':2, 'N':1}
def display_grid():
    for row in grid:
        print('    ', *row)

def build_tree(grid):
    tree = {}
    for x in range(dim):
        for y in range(dim):
            point = grid[x][y]
            if move_priority[point[0]] > move_priority[point[1]]:
                move = [(move_dict[point[0]][0]+move_dict[point[1]][0],move_dict[point[0]][1]+move_dict[point[1]][1]),
                         move_dict[point[0]],move_dict[point[1]]]
            else:
                move = [(move_dict[point[0]][0]+move_dict[point[1]][0],move_dict[point[0]][1]+move_dict[point[1]][1]),
                        move_dict[point[1]],move_dict[point[0]]]
                leaves = []
            #print(f'({x},{y}) of {point} is {move}')
            for i,j in move:
                if (0 <= (x + i) < dim) and (0 <= (y + j) < dim):
                    leaves.append((x + i, y + j))
            tree[(x,y)] = leaves
    return tree

# breadth first exploring trees by using queue
def breadth_first(point):
    tree = build_tree(grid)
    level =  Queue()
    all_paths = []
    level.enqueue([point])
    while not level.is_empty():
        path = level.dequeue()
        print(path)
        all_paths.append(path)
        if path[-1] in path[:-1]:
            continue
        if path[-1] in tree:
            for leaf in tree[path[-1]]:
                level.enqueue(path+[leaf])
    return all_paths


try:
    seed_arg = int(input('Enter an integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(seed_arg)
size = 3
dim = 2 * size + 1
grid = [[0] * dim for _ in range(dim)]
directions = 'NE', 'SE', 'SW', 'NW'

grid = [[choice(directions) for _ in range(dim)] for _ in range(dim)]


corners = (0, 0), (dim - 1, 0), (dim - 1, dim - 1), (0, dim - 1)
print(breadth_first((3,3)))
