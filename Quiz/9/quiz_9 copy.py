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

move_dict={'E':(0,1),'S':(1,0),'W':(0,-1), 'N':(-1,0)}
def display_grid():
    for row in grid:
        print('    ', *row)

# def walking(point,parent):
#     x,y = point
#     pts_set = [[]]*3
#     move = [move_dict[grid[x][y][0]],move_dict[grid[x][y][1]],
#     (move_dict[grid[x][y][0]][0]+move_dict[grid[x][y][1]][0],move_dict[grid[x][y][0]][1]+move_dict[grid[x][y][1]][1])]
#     next_point = [(x + e[0], y+e[1]) for e in move]
#     if x in [0,dim-1] or y in [0,dim-1]:
#         return {(x,y):parent}
#     else:
#         path = {point:parent}
#         for i in range(len(next_point)):
#             if next_point[i] in path.values():
#                 return {next_point[i]:parent}
#             else:
#                 pts_set[i] = walking(next_point[i])
#                 for e in pts_set:
#                     path_list.append(path + e)
#                 return path_list
def get_key(dic):
    #dic has only one key
    l = list(dic.keys())
    if len(l) > 1:
        return l
    return l[0]
def display(path_l):
    if path_l == None:
        return
    t_d = path_l.pop()
    node = get_key(t_d)
    parent = t_d[node]
    path = [node]
    while path_l:
        t = path_l.pop()
        t_node = get_key(t)
        if t_node == parent:
            path.append(t_node)
            parent = t[t_node]
    return list(path.__reversed__())

# breadth first exploring trees by using queue
def breadth_first(parent,point,target):
    level =  Queue()
    path = []
    if parent == point:
        level.enqueue({point:parent})
    while not level.is_empty():
        node_d = level.dequeue()
        node = get_key(node_d)
        if path:
            node_l = display(path)
        else:
            node_l = []
        #print(node_l)
        if node in node_l:
            continue
        path.append(node_d)
        x,y = node
        if node == target:
            print('p',path)
            return path
        move = [move_dict[grid[x][y][0]],move_dict[grid[x][y][1]],
        (move_dict[grid[x][y][0]][0]+move_dict[grid[x][y][1]][0],move_dict[grid[x][y][0]][1]+move_dict[grid[x][y][1]][1])]
        next_point = []
        for e in move:
            if (x + e[0] < 0 or x + e[0] > dim - 1) or (y+e[1] < 0 or y+e[1]  > dim - 1):
                continue
            else:
                next_point.append((x + e[0], y+e[1]))
        if next_point == []:
            continue
        else:
            for i in range(len(next_point)):
                level.enqueue({next_point[i]:node})
    if level.is_empty():
        return
    # level.enqueue({point:parent})
    # if point == target:
    #     return t_path
    # if x in [0,dim-1] or y in [0,dim-1]:
    #     return
    # move = [move_dict[grid[x][y][0]],move_dict[grid[x][y][1]],
    # (move_dict[grid[x][y][0]][0]+move_dict[grid[x][y][1]][0],move_dict[grid[x][y][0]][1]+move_dict[grid[x][y][1]][1])]
    # next_point = [(x + e[0], y+e[1]) for e in move]
    # for e in next_point:
    #     level.enqueue({e:point})
    #     if e == target:
    #         return level
    #     else:
    #         sub_que = breadth_first(point, e, target)
    #         if sub_que == None:
    #             level.dequeue()
    #             continue
    #         level.dequeue()
    #         while sub_que:
    #             level.enqueue(sub_que.dequeue())
    #         return level

def preferred_paths_to_corners():
    pt0 = (dim//2, dim//2)
    paths = {}
    for target in corners:
        paths[target] = display(breadth_first(pt0,pt0,target))
    return paths

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
print('Here is the grid that has been generated:')
display_grid()

corners = (0, 0), (dim - 1, 0), (dim - 1, dim - 1), (0, dim - 1)
paths = preferred_paths_to_corners()
if not paths:
    print('There is no path to any corner')
    sys.exit()
for corner in corners:
    if corner not in paths:
        print(f'There is no path to {corner}')
    else:
        print(f'The preferred path to {corner} is:')
        print('  ', paths[corner])
