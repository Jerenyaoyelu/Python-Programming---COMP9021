

def f(n, d):
    '''
    >>> f(2, 1)
    1 is not a proper factor of 2.
    >>> f(2, 2)
    2 is not a proper factor of 2.
    >>> f(16, 2)
    2 is a proper factor of 16 of mutiplicity 4.
    >>> f(100, 20)
    20 is a proper factor of 100 of mutiplicity 1.
    >>> f(8 ** 7 * 3 ** 5 * 11 ** 2, 8)
    8 is a proper factor of 61662560256 of mutiplicity 7.
    >>> f(3 ** 3 * 11 * 13 ** 2 * 40 ** 6, 8)
    8 is a proper factor of 205590528000000 of mutiplicity 6.
    '''
    multiplicity = 0
    # Insert your code here
    count=0
    nb=n
    while nb%d==0:
        count +=1
        nb=nb/d
    multiplicity=count
    if not multiplicity:
        print(f'{d} is not a proper factor of {n}.')
    else:
        print(f'{d} is a proper factor of {n} of mutiplicity {multiplicity}.')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
