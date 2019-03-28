'''
Prompts the user for a strictly positive integer, nb_of_elements,
generates a list of nb_of_elements random integers between 0 and 19, prints out the list,
computes the number of elements strictly less 5, 10, 15 and 20, and prints those out.
'''


from random import seed, randrange
import sys


# Insert your code here
while 1:
    try:
        s=int(input('Input a seed for the random number generator: '))
        break
    except ValueError:
        print('This is an illegal input, please input a number.')

while 1:
    try:
        n_elemts=int(input('How many elements do you want to generate? '))
        if n_elemts>=0:
            break
        else:
            print('This is an illegal input, please input an strict positive integer.')
    except ValueError:
        print('This is an illegal input, please input an strict positive integer.')

seed(s)
L=[randrange(0,20) for i in range(n_elemts)]
print('\nThe list is:',L)
count0,count1,count2,count3=0,0,0,0
for i in range(len(L)):
    if 0<=L[i]<=4:
        count0 +=1
    if 5<=L[i]<=9:
        count1 +=1
    if 10<=L[i]<=14:
        count2 +=1
    if 15<=L[i]<=19:
        count3 +=1
count_list=[count0,count1,count2,count3]
print()
for i in range(4):
    if count_list[i]==0:
        print('There is no element between %s and %s.'%(i*5,i*5+4))
    elif count_list[i]>1:
        print('There are %s elements between %s and %s.'%(count_list[i],i*5,i*5+4))
    else:
        print('There is %s element between %s and %s.'%(count_list[i],i*5,i*5+4))
