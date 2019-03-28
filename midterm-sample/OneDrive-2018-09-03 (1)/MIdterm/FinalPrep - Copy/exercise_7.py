
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
    a = ord('a')
    z = ord('z')
    total = width * height
    for h in range(1, height+1):
        line = []
        for i in range(width):
            if a>z:
                a = ord('a')
            line.append(chr(a))
          
            a+=1
            
        # if odd number, print in normal order
        if h%2:
            print(''.join(line))
        else:
            line = reversed(line)
            print(''.join(line))
        


if __name__ == '__main__':
    import doctest
    doctest.testmod()
