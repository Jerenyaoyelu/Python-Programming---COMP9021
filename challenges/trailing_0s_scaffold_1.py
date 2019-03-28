# Prompts the user to input an integer N at least equal to 10 and computes N!
# in three different ways.


import sys
from math import factorial


def first_computation(x):
    pass
    # Replace pass above with your code 

def second_computation(x):
    pass
    # Replace pass above with your code 

def third_computation(x):
    pass
    # Replace pass above with your code 

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
