# Prompts the user for an integer N and finds all perfect numbers up to N.
# Quadratic complexity, can deal with small values only.


import sys


try:
    N = int(input('Input an integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

for i in range(2, N + 1):
    pass
    # Replace pass above with your code to check whether i is perfect,
    # and print out that it is in case it is.
    # 1 divides i, so counts for one divisor.
    # It is enough to look at 2, ..., i // 2 as other potential divisors.
