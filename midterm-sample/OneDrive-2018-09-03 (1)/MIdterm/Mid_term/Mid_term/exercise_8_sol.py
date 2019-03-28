
def is_heterosquare(square):
    '''
    A heterosquare of order n is an arrangement of the integers 1 to n**2 in a square,
    such that the rows, columns, and diagonals all sum to DIFFERENT values.
    In contrast, magic squares have all these sums equal.
    
    
    >>> is_heterosquare([[1, 2, 3],\
                         [8, 9, 4],\
                         [7, 6, 5]])
    True
    >>> is_heterosquare([[1, 2, 3],\
                         [9, 8, 4],\
                         [7, 6, 5]])
    False
    >>> is_heterosquare([[2, 1, 3, 4],\
                         [5, 6, 7, 8],\
                         [9, 10, 11, 12],\
                         [13, 14, 15, 16]])
    True
    >>> is_heterosquare([[1, 2, 3, 4],\
                         [5, 6, 7, 8],\
                         [9, 10, 11, 12],\
                         [13, 14, 15, 16]])
    False
    '''
    n = len(square)
    if any(len(line) != n for line in square):
        return False
    if {number for line in square for number in line} != set(range(1, n ** 2 + 1)):
        return False
    sums = set()
    for row in square:
        if not is_new_sum(sum(row), sums):
            return False
    for j in range(len(square)):
        if not is_new_sum(sum(square[i][j] for i in range(n)), sums):
            return False
    if not is_new_sum(sum(square[i][i] for i in range(n)), sums):
        return False
    if not is_new_sum(sum(square[i][n - 1 - i] for i in range(n)), sums):
        return False
    return True

def is_new_sum(the_sum, sums):
    if the_sum in sums:
        return False
    sums.add(the_sum)
    return True
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
