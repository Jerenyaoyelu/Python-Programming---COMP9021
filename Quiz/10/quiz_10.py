# Randomly generates a binary search tree with values from 0 up to 9, and displays it growing up.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, choice
from binary_tree_adt import *

def visit_tree(tree,height,d,direction = ''):
    if tree is not None and tree.value is not None:
        d[direction] = tree.value
        visit_tree(tree.left_node,height,d,direction + 'L')
        visit_tree(tree.right_node,height,d,direction + 'R')
    
def calculate_index(s,h):
    length = len(s)
    i = h - length
    if s == '':
        j = 2**h-1
        return i,j
    j = 2**h-1
    k = 0
    while k < length:
        if s[k] == 'R':
            j += 2**(h-k-1)
        else:
            j -= 2**(h-k-1)
        k +=1
    return i,j 
def record_tree(n_d,h):
    location = {}
    for e in n_d:
        i,j = calculate_index(e,h)
        location[(j,n_d[e])] = i
    return location

def print_growing_up(tree,n_d):
    height = tree.height()
    tree_d = record_tree(n_d,height)
    print(tree_d)
    for i in range(height+1):
        t = 0
        for e in tree_d:
            if tree_d[e] == i:
                print(' '*(e[0]-t-1),e[1], end = '')
                t = e[0] +1
        print()
try:
    seed_arg, nb_of_nodes = (int(x) for x in
                              input('Enter two integers, with the second one between 0 and 10: '
                                   ).split()
                            )
    if nb_of_nodes < 0 or nb_of_nodes > 10:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(seed_arg)
data_pool = list(range(nb_of_nodes))
tree = BinaryTree()
for _ in range(nb_of_nodes):
    datum = choice(data_pool)
    tree.insert_in_bst(datum)
    data_pool.remove(datum)
node_d={}
visit_tree(tree,tree.height(),node_d)
print_growing_up(tree,node_d)
