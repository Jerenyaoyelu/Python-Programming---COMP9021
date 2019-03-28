# Finds all sequences of consecutive prime 5-digit numbers,
# say (a, b, c, d, e, f), such that
# b = a + 2, c = b + 4, d = c + 6, e = d + 8, and f = e + 10.


from math import sqrt


def is_prime(n):
    pass
    # Replace pass above with your code


print('The solutions are:\n')
# The list of all even i's such that a + i is one of a, b, c, d, e, f.
good_leaps = tuple(sum(range(0, k, 2)) for k in range(2, 13, 2))

# Write a loop that generates all odd numbers a between 10_000 and 99_999 and tests whether
# for all i = 0, 2, 4, ..., 30, i is in good_leaps iff a + i is prime.

