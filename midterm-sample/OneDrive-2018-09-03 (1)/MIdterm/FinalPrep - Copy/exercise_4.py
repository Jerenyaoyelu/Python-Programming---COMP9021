import sys

def f(n):
    '''
    A pair of natural numbers (m, n) is a Betrothed pair if:
    - the sum of the proper divisors of n is one more than m;
    - the sum of the proper divisors of m is one more than n.
    For instance, (48, 75) is a Betrothed pair since
    - the proper divisors of 48 are 1, 2, 3, 4, 6, 8, 12, 16 and 24
    - the proper divisors of 75 are 1, 3, 5, 15 and 25
    - 1 + 2 + 3 + 4 + 6 + 8 + 12 + 16 + 24 = 76
    - 1 + 3 + 5 + 15 + 25 = 49
    
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

    p = max(n,1)
    while True:
        q = sum_of_divisors_minus_1(p)
        if p == sum_of_divisors_minus_1(q):
            print(('The least number >= {} that is the first member of a Betrothed pair is {}').format(n, p))
            print(('The Betrothed pair itself is ({}, {})').format(p,q))
            return
        p += 1
    '''
    for i in range(n,10001):
        if i >= n:
            i_divisors = divsiors(i)
            for j in range(n,10001):
                j_divisors = divsiors(j)
                if (sum(i_divisors) == j+1) and (sum(j_divisors) == i+1):
                    print(('The least number >= {} is the first member of a Betrothed pair is {}').format(n, i))
                    print(('The Betrothed pair itself is ({}, {})').format(i,j))
                   return
    '''
def sum_of_divisors_minus_1(a):
    divs = divsiors(a)
    
    if divs:
        return sum(divs) - 1
    return
            
            
def divsiors(a):
    
    divisors = []
    if a:
        for i in range(1, a//2 + 1):
            if not a%i:
                divisors.append(i)
    return divisors


if __name__ == '__main__':
    import doctest
    doctest.testmod()

