
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

    sums = set()
    for row in square:
        if sum(row) in sums:
            return False
        sums.add(sum(row))

    cols = get_column_lists(square)
    for col in cols:
        if sum(col) in sums:
            return False
        sums.add(sum(col))

    first, second = get_diag(square)
    if sum(first) in sums:
        return False
    sums.add(sum(first))

    if sum(second) in sums:
        return False
    sums.add(sum(second))
    return True


def get_diag(square):
    n = len(square)
    first_diag = []
    for i in range(n):
        first_diag.append(square[i][i])

    second_diag = []
    for i in range(n-1,-1,-1):
        second_diag.append(square[n-i-1][i])
    return first_diag, second_diag

def get_column_lists(square):
    n = len(square)
    columns = []
    for i in range(n):
        cols = []
        for j in square:
            cols.append(j[i])
        columns.append(cols)
    return columns
    



    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
