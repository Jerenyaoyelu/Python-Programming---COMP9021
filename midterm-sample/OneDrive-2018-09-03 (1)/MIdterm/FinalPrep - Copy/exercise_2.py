from random import seed, randint, randrange
import sys
from collections import defaultdict


def f(arg_for_seed, nb_of_elements, max_size):
    '''
    >>> f(10, 0, 1)
    Here is L: []
    >>> f(0, 1, 1)
    Here is L: [6]
    List members of length 1 with no successive occurrences of the same digit:
        6
    >>> f(8, 6, 4)
    Here is L: [5, 129, 0, 0, 8, 6]
    List members of length 1 with no successive occurrences of the same digit:
        5 0 0 8 6
    List members of length 3 with no successive occurrences of the same digit:
        129
    >>> f(20, 8, 5)
    Here is L: [89948, 4, 83325, 0, 2775, 0, 76, 0]
    List members of length 1 with no successive occurrences of the same digit:
        4 0 0 0
    List members of length 2 with no successive occurrences of the same digit:
        76
    >>> f(30, 10, 7)
    Here is L: [492, 263, 0, 672743, 10, 127618, 26, 2, 872293, 70150]
    List members of length 1 with no successive occurrences of the same digit:
        0 2
    List members of length 2 with no successive occurrences of the same digit:
        10 26
    List members of length 3 with no successive occurrences of the same digit:
        492 263
    List members of length 5 with no successive occurrences of the same digit:
        70150
    List members of length 6 with no successive occurrences of the same digit:
        672743 127618
    >>> f(30, 12, 5)    
    Here is L: [4738, 492, 3440, 6, 385, 17572, 0, 0, 0, 9, 6582, 45665]
    List members of length 1 with no successive occurrences of the same digit:
        6 0 0 0 9
    List members of length 3 with no successive occurrences of the same digit:
        492 385
    List members of length 4 with no successive occurrences of the same digit:
        4738 6582
    List members of length 5 with no successive occurrences of the same digit:
        17572
    '''
    if nb_of_elements < 0 or max_size <= 0:
        sys.exit()
    seed(arg_for_seed)
    L = [randrange(0, 10 ** randint(0, max_size)) for _ in range(nb_of_elements)]
    print('Here is L:', L)
    
    succssive_occurence_lenghts = defaultdict(list)

    for members in L:
        if len(str(members)) == len(set(str(members))):
            length = len(str(members))
            succssive_occurence_lenghts[length].append(members)
            continue
        members_string = str(members)
        succsive = False
        for pos in range(len(members_string)-1):
            if pos == 0 and members_string[0] == members_string[1]:
                succsive = True
                break
            if members_string[pos] == members_string[pos-1] or members_string[pos] == members_string[pos+1]:
                succsive = True
                break
        if not succsive:
            length = len(str(members))
            succssive_occurence_lenghts[length].append(members)
            

    for length in succssive_occurence_lenghts:
        print(("List members of length {} with no successive occurrences of the same digit:").format(length))
        print('    ', end = '')
        print(' '.join(str(n) for n in succssive_occurence_lenghts[length]))
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()