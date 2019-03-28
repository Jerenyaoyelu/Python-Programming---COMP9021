# Written by Eric Martin for COMP9021


'''
Prompts the user for a strictly positive integer, nb_of_elements,
generates a list of nb_of_elements random integers between -50 and 50, prints out the list,
computes the mean, the median and the standard deviation in two ways,
that is, using or not the functions from the statistics module, and prints them out.
'''


from random import seed, randint
from math import sqrt
from statistics import mean, median, pstdev
import sys


# Insert your code here
while 1:
    try:
        s=int(input('Input a seed for the random number generator: '))
        break
    except ValueError:
        print('This is an illegal input, input again.')
while 1:
    try:
        n_elemts=int(input('How many elements do you want to generate? '))
        if n_elemts<0:
            print('This is an illegal input, input a strictly positive integer.')
        break
    except ValueError:
        print('This is an illegal input, input again.')

seed(s)
L=[randint(-50,50) for i in range(n_elemts)]
print('The list is: ',L)
L.sort()
sum_l=int(0)
for i in range(n_elemts):
    sum_l +=int(L[i])
m=sum_l/int(n_elemts)
print('The mean is %.2f'%m)
if n_elemts%2==0:
    md=(L[int(n_elemts/2)]+L[int(n_elemts/2)-1])/2
else:
    md=L[int(n_elemts//2)]
print('The median is %.2f'%md)
sum_sd=int(0)
for i in range(n_elemts):
    sum_sd +=(L[i]-sum_l/n_elemts)**2
print('The standard deviation is %.2f'%sqrt(sum_sd/n_elemts))

print('Confirming with functions from the statistics module:\n')
print('The mean is %.2f'%mean(L))
print('The median is %.2f'%median(L))
print('The standard deviation is %.2f'%pstdev(L))
