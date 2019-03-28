from random import seed, randint
import sys


def f(arg_for_seed, nb_of_elements, max_element):
    '''
    >>> f(0, 0, 10)
    Here is L: []
    The decomposition of L into longest sublists of even numbers is: []
    >>> f(0, 1, 10)
    Here is L: [6]
    The decomposition of L into longest sublists of even numbers is: [[6]]
    >>> f(0, 2, 10)
    Here is L: [6, 6]
    The decomposition of L into longest sublists of even numbers is: [[6, 6]]
    >>> f (0, 2, 2)
    Here is L: [1, 1]
    The decomposition of L into longest sublists of even numbers is: []
    >>> f(1, 2, 10)
    Here is L: [2, 9]
    The decomposition of L into longest sublists of even numbers is: [[2]]
    >>> f(1, 4, 10)
    Here is L: [2, 9, 1, 4]
    The decomposition of L into longest sublists of even numbers is: [[2], [4]]
    >>> f(1, 8, 8)
    Here is L: [2, 1, 4, 1, 7, 7, 7, 6]
    The decomposition of L into longest sublists of even numbers is: [[2], [4], [6]]
    >>> f(1, 10, 20)
    Here is L: [4, 18, 2, 8, 3, 15, 14, 15, 20, 12]
    The decomposition of L into longest sublists of even numbers is: [[4, 18, 2, 8], [14], [20, 12]]
    '''
    if nb_of_elements < 0:
        sys.exit()
    seed(arg_for_seed)
    L = [randint(0, max_element) for _ in range(nb_of_elements)]
    print('Here is L:', L)
    R = []
    # Insert your code here
    t_r=[]
    for e in L:
        if e%2==0:
            t_r.append(e)
        elif len(t_r)>0:
            R.append(t_r)
            t_r=[]
    if len(t_r)>0:
        R.append(t_r)
    print('The decomposition of L into longest sublists of even numbers is:', R)    


if __name__ == '__main__':
    import doctest
    doctest.testmod()
