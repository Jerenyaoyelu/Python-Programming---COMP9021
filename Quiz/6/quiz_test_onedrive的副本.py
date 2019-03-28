# Randomly fills an array of size 10x10 True and False, displayed as 1 and 0,
# and outputs the number chess knights needed to jump from 1s to 1s
# and visit all 1s (they can jump back to locations previously visited).
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randrange
import sys

def explore_board(pts):
    x=pts[0]
    y=pts[1]
    pts_set=[{}]*8
    if (x<0 or x>9) or (y<0 or y>9):
        return {()}
    elif grid[x][y]==False:
        return {()}
    else:
        grid[x][y]=False
        pts_set[0]=explore_board((x-1,y-2))
        pts_set[1]=explore_board((x+1,y-2))
        pts_set[2]=explore_board((x+2,y-1))
        pts_set[3]=explore_board((x+2,y+1))
        pts_set[4]=explore_board((x+1,y+2))
        pts_set[5]=explore_board((x-1,y+2))
        pts_set[6]=explore_board((x-2,y-1))
        pts_set[7]=explore_board((x-2,y+1))
        s={(x,y)}
        for e in pts_set:
            if e!={()}:
                s = s|e
        #print(s)
        return s

dim=50
for_seed=2
n=-3
seed(for_seed)
if n > 0:
    grid = [[randrange(n) > 0 for _ in range(dim)] for _ in range(dim)]
else:
    grid = [[randrange(-n) == 0 for _ in range(dim)] for _ in range(dim)]    
paths_l=[]
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j]==True:
            ts=explore_board((i,j))
            if ts!={()}:
                paths_l.append(ts)
nb_of_knights=len(paths_l)
print(paths_l)
print(f'dim: {dim:<4},   for_seed: {for_seed},   n: {n:2} ---> knights: {nb_of_knights}')

