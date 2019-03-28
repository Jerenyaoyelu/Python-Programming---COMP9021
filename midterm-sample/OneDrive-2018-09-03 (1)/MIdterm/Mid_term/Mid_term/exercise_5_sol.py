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
    N = b
    primes_sieve = [True] * (N + 1)
    for n in range(2, round(sqrt(N)) + 1):
        if primes_sieve[n]:
            for i in range(n * n, N + 1, n):
                primes_sieve[i] = False
    primes = [i for i in range(a, b + 1) if primes_sieve[i]]
    if len(primes) > 1:
        max_gap = max(primes[i + 1] - primes[i] for i in range(len(primes) - 1)) - 1
    print('The maximum gap between successive prime numbers in that interval is', max_gap)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
