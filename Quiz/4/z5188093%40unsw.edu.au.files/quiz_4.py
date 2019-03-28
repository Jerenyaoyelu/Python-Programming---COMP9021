# Randomly fills an array of size 10x10 with True and False, and outputs the number of blocks
# in the largest block construction, determined by rows of True's that can be stacked
# on top of each other. 
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randrange
import sys


dim = 10


def display_grid():
    for i in range(dim):
        print('     ', end = '')
        print(' '.join(f'{int(e)}' for e in grid[i]))
    print()
# If j1 <= j2 and the grid has a 1 at the intersection of row i and column j
# for all j in {j1, ..., j2}, then returns the number of blocks in the construction
# built over this line of blocks.
def construction_size(i, l):
    s=0
    k=0
    max_size=0
    for j in range(len(l[i])):
        if l[i][j]==True:
            s +=1
            k=i-1
            while k>=0:
                if l[k][j]==True:
                    s +=1
                    k -=1
                else:
                    break
            if max_size<s:
                max_size=s
        else:
            s=0
    return max_size
def size_of_largest_construction(l):
    largest_c=0
    for i in range(len(l)-1,-1,-1):
        if largest_c<construction_size(i,l):
            largest_c=construction_size(i,l)
    return largest_c
     
try:
    for_seed, n = input('Enter two integers, the second one being strictly positive: ').split()
    for_seed = int(for_seed)
    n = int(n)
    if n <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[bool(randrange(n)) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()

size = size_of_largest_construction(grid)
if not size:
    print(f'The largest block construction has no block.')  
elif size == 1:
    print(f'The largest block construction has 1 block.')  
else:
    print(f'The largest block construction has {size} blocks.')
