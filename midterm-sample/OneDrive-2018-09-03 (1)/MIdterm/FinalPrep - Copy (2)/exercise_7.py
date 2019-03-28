
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

    a_code = ord('a')
    z_code = ord('z')
    lines = []
    for h in range(1, height+1):
        line = []
        for w in range(width):
            if h%2:
                line.append(chr(a_code))
                a_code += 1
                if a_code > z_code:
                    a_code = ord('a')
                if a_code < ord('a'):
                    a_code = ord('z')
                
            else:
                line.append(chr(a_code))
                a_code += 1
                if a_code > z_code:
                    a_code = ord('a')
                if a_code < ord('a'):
                    a_code = ord('z')
            
        if not h%2:
            line = line[::-1]
        lines.append(line)
                
    for i in lines:
        print(''.join(i))
                
       
        
        


if __name__ == '__main__':
    import doctest
    doctest.testmod()
