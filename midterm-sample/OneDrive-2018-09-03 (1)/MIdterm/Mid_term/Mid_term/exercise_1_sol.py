from random import seed, randint
import sys


def f(arg_for_seed, nb_of_elements, max_element):
    '''
    >>> f(0, 0, 10)
    Here is L: []
    The decomposition of L into increasing sublists is: []
    >>> f(0, 1, 10)
    Here is L: [6]
    The decomposition of L into increasing sublists is: [[6]]
    >>> f(0, 2, 10)
    Here is L: [6, 6]
    The decomposition of L into increasing sublists is: [[6], [6]]
    >>> f(1, 2, 10)
    Here is L: [2, 9]
    The decomposition of L into increasing sublists is: [[2, 9]]
    >>> f(0, 3, 10)
    Here is L: [6, 6, 0]
    The decomposition of L into increasing sublists is: [[6], [6], [0]]
    >>> f(1, 4, 10)
    Here is L: [2, 9, 1, 4]
    The decomposition of L into increasing sublists is: [[2, 9], [1, 4]]
    >>> f(20, 5, 10)
    Here is L: [10, 2, 4, 10, 10]
    The decomposition of L into increasing sublists is: [[10], [2, 4, 10], [10]]
    >>> f(1, 10, 20)
    Here is L: [4, 18, 2, 8, 3, 15, 14, 15, 20, 12]
    The decomposition of L into increasing sublists is: [[4, 18], [2, 8], [3, 15], [14, 15, 20], [12]]
    '''
    if nb_of_elements < 0:
        sys.exit()
    seed(arg_for_seed)
    L = [randint(0, max_element) for _ in range(nb_of_elements)]
    print('Here is L:', L)
    R = []
    if L:
        S = [L[0]]
        for e in L[1: ]:
            if e > S[-1]:
                S.append(e)
            else:
                R.append(S)
                S = [e]
        R.append(S)
    print('The decomposition of L into increasing sublists is:', R)
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
