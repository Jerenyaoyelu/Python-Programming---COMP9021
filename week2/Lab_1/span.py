
'''
Prompts the user for a seed for the random number generator,
and for a strictly positive number, nb_of_elements.
Generates a list of nb_of_elements random integers between 0 and 99, prints out the list,
computes the difference between the largest and smallest values in the list without using
the builtins min() and max(), prints it out, and check that the result is correct using
the builtins.
'''


from random import seed, randint
import sys


# Insert your code here
L=[]
try:
    s=float(input('Please input a seed for the random number generator:'))
except ValueError:
    print('this is an illegal seed, the system is shutting down')
    #'exit()'function will just exit this command，the rest commands still will be executed.
    # So here should be 'sys.exit()' to stop the system.
    sys.exit()

try:
    n_elements=int(input('How many elements do you want to generate?\n'))
except ValueError:
    print('this is an illegal number，the system is shutting down.')
    sys.exit()

seed(s)
for i in range(n_elements):
    L.append(randint(0,99))
# L=[randint(0,99) for _ in range(n_elements)] same outputs within one line of code.
print('The list is:',L)

max_n=L[0]
min_n=L[0]
for i in range(len(L)):
    if max_n<=L[i]:
        max_n=L[i]
    if min_n>=L[i]:
        min_n=L[i]
print('The maximum difference between largest and smallest values in the list is:',max_n-min_n)
print('Confirming with builtin operations:',max(L)-min(L))
