# Prompts the user to input an integer N at least equal to 10 and computes N!
# in three different ways.


import sys
from math import factorial


def first_computation(x):
    nb_of_trailing_0s = 0
    # Insert code here
    return nb_of_trailing_0s

def second_computation(x):
    pass
    # Replace pass above with code that uses x[-i] for i in range(1, len(x))

def third_computation(x):
    nb_of_trailing_0s = 0
    power_of_five = 5
    # Here insert a loop where at every iteration,
    # nb_of_trailing_0s is updated and then power_of_five is changed to the next power of 5
    return nb_of_trailing_0s

try:
    the_input = int(input('Input a nonnegative integer: '))
    if the_input < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

the_input_factorial = factorial(the_input)
print(f'Computing the number of trailing 0s in {the_input}! by dividing by 10 for long enough:',
      first_computation(the_input_factorial))
print(f'Computing the number of trailing 0s in {the_input}! by converting it into a string:',
      second_computation(str(the_input_factorial)))
print(f'Computing the number of trailing 0s in {the_input}! the smart way:',
      third_computation(the_input))
