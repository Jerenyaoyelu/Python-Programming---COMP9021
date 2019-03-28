# Randomly fills an array of size 10x10 True and False, displayed as 1 and 0,
# and outputs the number chess knights needed to jump from 1s to 1s
# and visit all 1s (they can jump back to locations previously visited).
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randrange
import sys


dim = 10


def display_grid():
    for i in range(dim):
        print('     ', end = '')
        print(' '.join(grid[i][j] and '1' or '0' for j in range(dim)))
    print()


def explore_board(pts):
    x=pts[0]
    y=pts[1]
    pts_set=[{}]*8
    if (x<0 or x>dim-1) or (y<0 or y>dim-1):
        return {()}
    elif grid[x][y]==0:
        return {()}
    else:
        grid[x][y]=0
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
            if e !={()}:
                s = s|e
        return s

try:
    for_seed, n = (int(i) for i in input('Enter two integers: ').split())
    if not n:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
if n > 0:
    grid = [[randrange(n) > 0 for _ in range(dim)] for _ in range(dim)]
else:
    grid = [[randrange(-n) == 0 for _ in range(dim)] for _ in range(dim)]    
print('Here is the grid that has been generated:')
display_grid()
paths_l=[]
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j]==1:
            ts=explore_board((i,j))
            if ts!={()}:
                paths_l.append(ts)
nb_of_knights=len(paths_l)
if not nb_of_knights:
    print('No chess knight has explored this board.')
elif nb_of_knights == 1:
    print(f'At least 1 chess knight has explored this board.')
else:
    print(f'At least {nb_of_knights} chess knights have explored this board')


