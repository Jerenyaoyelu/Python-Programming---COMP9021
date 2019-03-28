import sys
from math import gcd
from random import seed, randrange
from extended_linked_list import ExtendedLinkedList

from extended_linked_list import ExtendedLinkedList

def test(arg_for_seed, length, step):
    seed(arg_for_seed)

    L = [randrange(100) for _ in range(length)]

    LL = ExtendedLinkedList(L)
    LL.print()

    LL.rearrange(step)
    LL.print()

if __name__ == '__main__':
    for length in range(3, 15):
        for step in range(length-2, length*3):
            if gcd(length, step) == 1:
                for arg_seed in [1, 2]:
                    print()
                    print(arg_seed, length, step)
                    test(arg_seed, length, step)
