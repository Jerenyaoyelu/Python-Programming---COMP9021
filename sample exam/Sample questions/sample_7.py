'''
Tries and find a word in a text file that represents a grid of words, all of the same length.
There is only one word per line in the file.
The letters that make up a word can possibly be separated by an arbitrary number of spaces,
and there can also be spaces at the beginning or at the end of a word,
and there can be lines consisting of nothing but spaces anywhere in the file.
Assume that the file stores data as expected.

A word can be read horizontally from left to right,
or vertically from top to bottom,
or diagonally from top left to bottom right
(this is more limited than the lab exercise).
The locations are represented as a pair (line number, column number),
starting the numbering with 1 (not 0).
'''


def find_word(filename, word):
    '''
    >>> find_word('word_search_1.txt', 'PLATINUM')
    PLATINUM was found horizontally (left to right) at position (10, 4)
    >>> find_word('word_search_1.txt', 'MANGANESE')
    MANGANESE was found horizontally (left to right) at position (11, 4)
    >>> find_word('word_search_1.txt', 'LITHIUM')
    LITHIUM was found vertically (top to bottom) at position (2, 14)
    >>> find_word('word_search_1.txt', 'SILVER')
    SILVER was found vertically (top to bottom) at position (2, 13)
    >>> find_word('word_search_1.txt', 'SODIUM')
    SODIUM was not found
    >>> find_word('word_search_1.txt', 'TITANIUM')
    TITANIUM was not found
    >>> find_word('word_search_2.txt', 'PAPAYA')
    PAPAYA was found diagonally (top left to bottom right) at position (1, 9)
    >>> find_word('word_search_2.txt', 'RASPBERRY')
    RASPBERRY was found vertically (top to bottom) at position (5, 14)
    >>> find_word('word_search_2.txt', 'BLUEBERRY')
    BLUEBERRY was found horizontally (left to right) at position (13, 5)
    >>> find_word('word_search_2.txt', 'LEMON')
    LEMON was not found
    '''
    with open(filename) as file:
        grid = None
        # Insert your code here
        grid_s = file.readlines()
        grid = [[s for s in e if s <= 'Z'and s >= 'A'] for e in grid_s if [s for s in e if s <= 'Z'and s >= 'A'] != []]
        # A one liner that sets grid to the appropriate value is enough.
        location = find_word_horizontally(grid, word)
        found = False
        if location:
            found = True
            print(word, 'was found horizontally (left to right) at position', location)
        location = find_word_vertically(grid, word)
        if location:
            found = True
            print(word, 'was found vertically (top to bottom) at position', location)
        location = find_word_diagonally(grid, word)
        if location:
            found = True
            print(word, 'was found diagonally (top left to bottom right) at position', location)
        if not found:
            print(word, 'was not found')

def find_word_horizontally(grid, word):
    word_l = [letter for letter in word]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j:j+len(word)] == word_l:
                return i+1,j+1
    # Replace pass above with your code


def find_word_vertically(grid, word):
    word_l = [letter for letter in word]
    for j in range(len(grid[0])):
        k = 0
        for i in range(len(grid)):
            if k > len(word)-1:
                return i-k+1,j+1
            if grid[i][j] == word_l[k]:
                k += 1
            else:
                if k > 0:
                    k = 0
                continue
    # Replace pass above with your code

def find_word_diagonally(grid, word):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            k = i
            l = j
            p = 0
            while True:
                if p > len(word) - 1:
                    return i+1,j+1
                if k > len(grid) - 1 or l > len(grid[i]) - 1:
                    break
                if grid[k][l] == word[p]:
                    k += 1
                    l += 1
                    p += 1
                else:
                    break
    # Replace pass above with your code
if __name__ == '__main__':
    import doctest
    doctest.testmod()   
