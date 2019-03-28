
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

    N = len(square)
    sums = set()
    for row in square:
        if sum(row) in sums:
            return False
        sums.add(sum(row))

    for col in range(len(square)):
        new_sum = 0
        for row in range(len(square)):
            new_sum += square[row][col]
        if new_sum in sums:
            return False
        sums.add(new_sum)

    new_sum = 0
    for i in range(len(square)):
        new_sum += square[i][i]
    if new_sum in sums:
        return False
    sums.add(new_sum)
    new_sum = 0
    for i in range(len(square)):
        new_sum += square[i][N-i-1]
    if new_sum in sums:
        return False
    return True
    
    

    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
