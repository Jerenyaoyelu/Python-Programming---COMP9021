'''
Will be tested with n at least equal to 2, and "not too large".
'''
from math import sqrt

def prm(n):
    l=[True]*(n+1)
    l[0]=False
    l[1]=False
    p=[]
    for i in range(2,round(sqrt(n))+1):
        for j in range(i+1,n+1):
            if j%i==0:
                l[j]=False
    for k in range(len(l)):
        if l[k]==True:
            p.append(k)
    return p
    
def f(n):
    '''
    >>> f(2)
    The decomposition of 2 into prime factors reads:
       2 = 2
    >>> f(3)
    The decomposition of 3 into prime factors reads:
       3 = 3
    >>> f(4)
    The decomposition of 4 into prime factors reads:
       4 = 2^2
    >>> f(5)
    The decomposition of 5 into prime factors reads:
       5 = 5
    >>> f(6)
    The decomposition of 6 into prime factors reads:
       6 = 2 x 3
    >>> f(8)
    The decomposition of 8 into prime factors reads:
       8 = 2^3
    >>> f(10)
    The decomposition of 10 into prime factors reads:
       10 = 2 x 5
    >>> f(15)
    The decomposition of 15 into prime factors reads:
       15 = 3 x 5
    >>> f(100)
    The decomposition of 100 into prime factors reads:
       100 = 2^2 x 5^2
    >>> f(5432)
    The decomposition of 5432 into prime factors reads:
       5432 = 2^3 x 7 x 97
    >>> f(45103)
    The decomposition of 45103 into prime factors reads:
       45103 = 23 x 37 x 53
    >>> f(45100)
    The decomposition of 45100 into prime factors reads:
       45100 = 2^2 x 5^2 x 11 x 41
    '''
    factors = {}
    # Insert your code here
    prime_l=prm(n)
    if n in prime_l:
        factors[n]=1
    else:
        i=0
        c=0
        while i<len(prime_l):
            if n!=0:
                if n%prime_l[i]==0:
                    n=n%prime_l[i]
                    c +=1
                    factors[i]=c
                else:
                    c=0
                    i+=1
            else:
                break
    print(factors)
    print(f'The decomposition of {n} into prime factors reads:')
    print('  ', n, '=', end = ' ')
    print(' x '.join(factors[x] == 1 and str(x) or f'{x}^{factors[x]}'for x in sorted(factors)))
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
