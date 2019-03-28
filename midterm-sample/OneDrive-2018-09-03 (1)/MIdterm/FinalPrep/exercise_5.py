import sys
from math import sqrt


def f(a, b):
    '''
    The prime numbers between 2 and 12 (both included) are: 2, 3, 5, 7, 11
    The gaps between successive primes are: 0, 1, 1, 3.
    Hence the maximum gap is 3.
    
    Won't be tested for b greater than 10_000_000
    
    >>> f(3, 3)
    The maximum gap between successive prime numbers in that interval is 0
    >>> f(3, 4)
    The maximum gap between successive prime numbers in that interval is 0
    >>> f(3, 5)
    The maximum gap between successive prime numbers in that interval is 1
    >>> f(2, 12)
    The maximum gap between successive prime numbers in that interval is 3
    >>> f(5, 23)
    The maximum gap between successive prime numbers in that interval is 3
    >>> f(20, 106)
    The maximum gap between successive prime numbers in that interval is 7
    >>> f(31, 291)
    The maximum gap between successive prime numbers in that interval is 13
    '''
    if a <= 0 or b < a:
        sys.exit()
    max_gap = 0

    gap_list = [None] * (b+1)
    for n in range(a, b+1):
        if is_prime(n):
            gap_list[n] = 1

    ones = [i for i, val in enumerate(gap_list) if val]
    if len(ones)>0:
        for ind in range(1, len(ones)):
            gap = ones[ind]-ones[ind-1]
            if gap-1 > max_gap:
                max_gap = gap-1

    print('The maximum gap between successive prime numbers in that interval is', max_gap)
                
            
    
def is_prime(n):
    if n > 2:
        return all(n%i for i in range(2,n))
    return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()
