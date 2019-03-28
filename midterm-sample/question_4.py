import sys
from math import sqrt


def is_prime(n):
    if n ==1 or n==2 or n==3:
        return True
    else:
        for d in range(3, round(sqrt(n))+1):
            if n%d==0:
                return False
            elif d>=round(sqrt(n)):
                return True
def f(n):
    '''
    Won't be tested for n greater than 10_000_000
    
    >>> f(3)
    The largest prime strictly smaller than 3 is 2.
    >>> f(10)
    The largest prime strictly smaller than 10 is 7.
    >>> f(20)
    The largest prime strictly smaller than 20 is 19.
    >>> f(210)
    The largest prime strictly smaller than 210 is 199.
    >>> f(1318)
    The largest prime strictly smaller than 1318 is 1307.
    '''
    if n <= 2:
        sys.exit()
    largest_prime_strictly_smaller_than_n = 0
    # Insert your code here
    for i in range(n-1,0,-1):
        if i==2:
            largest_prime_strictly_smaller_than_n = i
            break
        elif i%2!=0 and is_prime(i)==True:
            largest_prime_strictly_smaller_than_n = i
            break
    print(f'The largest prime strictly smaller than {n} is {largest_prime_strictly_smaller_than_n}.')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
