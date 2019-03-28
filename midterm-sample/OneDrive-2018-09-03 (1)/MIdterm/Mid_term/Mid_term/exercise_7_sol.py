
# ord(c) returns the encoding of character c.
# chr(e) returns the character encoded by e.


def f(width, height):
    '''
    Displays a rectangle by outputting lowercase letters, starting with a,
    in a "snakelike" manner, from left to right, then from right to left,
    then from left to right, then from right to left, wrapping around when z is reached.
    
    >>> f(1, 1)
    a
    >>> f(2, 3)
    ab
    dc
    ef
    >>> f(3, 2)
    abc
    fed
    >>> f(17, 4)
    abcdefghijklmnopq
    hgfedcbazyxwvutsr
    ijklmnopqrstuvwxy
    ponmlkjihgfedcbaz
    '''
    if width <= 0 or height <= 0:
        sys.exit()
    for i in range(1, height + 1):
        if i % 2:
            for j in range(width):
                print(chr(((i - 1) * width + j) % 26 + ord('a')), end = '')
        else:
            for j in range(width):
                print(chr(((i - 1) * width + width - j - 1) % 26 + ord('a')), end = '')
        print()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
