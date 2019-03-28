import sys


def f(n):
    '''
    A pair of natural numbers (p, q) is a Betrothed pair if:
    - the sum of the proper divisors of p is one more than q;
    - the sum of the proper divisors of q is one more than p.
    For instance, (48, 75) is a Betrothed pair since
    - the proper divisors of 48 are 1, 2, 3, 4, 6, 8, 12, 16 and 24
    - the proper divisors of 75 are 1, 3, 5, 15 and 25
    - 1 + 2 + 3 + 4 + 6 + 8 + 12 + 16 + 24 = 76
    - 1 + 3 + 5 + 15 + 25 = 49

    Won't be tested for n greater than 10_000
    
    >>> f(0)
    The least number >= 0 that is the first member of a Betrothed pair is 48
    The Betrothed pair itself is (48, 75)
    >>> f(50)
    The least number >= 50 that is the first member of a Betrothed pair is 75
    The Betrothed pair itself is (75, 48)
    >>> f(100)
    The least number >= 100 that is the first member of a Betrothed pair is 140
    The Betrothed pair itself is (140, 195)
    '''
    if n < 0:
        sys.exit()
    p = max(n, 1)
    while True:
        q = sum_of_divisors_minus_1(p)
        if sum_of_divisors_minus_1(q) == p:
            break
        p += 1
    print('The least number >=', n, 'that is the first member of a Betrothed pair is', p)
    print(f'The Betrothed pair itself is ({p}, {q})')

def sum_of_divisors_minus_1(n):
    return sum(d for d in range(2, n // 2 + 1) if n % d == 0)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
