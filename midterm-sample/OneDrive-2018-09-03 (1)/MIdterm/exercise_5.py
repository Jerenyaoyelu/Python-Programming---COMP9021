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
    # Insert your code here
    gap = 0
    gap_array = [0]*len(range(a,b+1))
    
    for pos, n in enumerate(range(a,b+1)):
        
        if isprime(n):
            gap_array[pos] = 1
   
    count = []
    old_i = -1
    gap_arraycopy = gap_array.copy()
    
    for n in gap_array:
        if n==1:
            
            i = gap_arraycopy.index(1)
            
            gap_arraycopy.remove(1)
            if old_i>=0:
                gap = i-old_i
                
            
            old_i = i
        if gap>max_gap:
            max_gap = gap
        

    
    print('The maximum gap between successive prime numbers in that interval is', max_gap)

def isprime(n):
    prime = True
    for i in range(2,n):
        if n%i == 0:
            prime =False

    return prime


if __name__ == '__main__':
    import doctest
    doctest.testmod()
